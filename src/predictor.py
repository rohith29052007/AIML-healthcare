"""
Predictor Module
Handles disease prediction using trained models
"""

import numpy as np
import pandas as pd
import joblib
import os
from pathlib import Path
from recommendations import get_disease_solutions


class DiseasePredictor:
    """Class to handle disease predictions using trained models"""
    
    def __init__(self, models_path):
        """
        Initialize DiseasePredictor with trained models
        
        Args:
            models_path: Path to the saved models file
        """
        self.models_path = models_path
        self.models = None
        self.feature_names = None
        self.disease_encoder = None
        self.load_models()
    
    def load_models(self):
        """Load trained models from disk"""
        try:
            if not os.path.exists(self.models_path):
                raise FileNotFoundError(f"Models file not found: {self.models_path}")
            
            data = joblib.load(self.models_path)
            self.models = data['models']
            self.feature_names = data['feature_names']
            self.disease_encoder = data['disease_encoder']
            
            print(f"✓ Models loaded successfully from {self.models_path}")
            print(f"  Features: {len(self.feature_names)}")
            print(f"  Diseases: {len(self.disease_encoder.classes_)}")
            
        except Exception as e:
            print(f"Error loading models: {e}")
            raise
    
    def predict_disease(self, symptoms_dict, model_name='random_forest', duration='3-7'):
        """
        Predict disease based on selected symptoms and duration
        
        Args:
            symptoms_dict: Dictionary with symptoms as keys (0 or 1)
            model_name: Name of model to use ('decision_tree', 'random_forest', 'xgboost')
            duration: Symptom duration ('1-2', '3-7', '1-2w', '2-4w', '4+w')
        
        Returns:
            Dictionary with prediction results
        """
        try:
            # Create feature vector based on selected symptoms
            feature_vector = self._create_feature_vector(symptoms_dict)
            
            # Ensure we use an available model
            if model_name not in self.models:
                model_name = 'random_forest'  # Use RF by default
            
            model = self.models[model_name]
            
            # Make prediction
            prediction = model.predict(feature_vector.reshape(1, -1))
            predicted_disease = self.disease_encoder.inverse_transform(prediction)[0]
            
            # Get prediction probabilities if available
            if hasattr(model, 'predict_proba'):
                probabilities = model.predict_proba(feature_vector.reshape(1, -1))[0]
            else:
                # For SVM without probability, use decision_function
                decision_scores = model.decision_function(feature_vector.reshape(1, -1))
                # Normalize scores to probabilities
                probabilities = self._normalize_scores(decision_scores)
            
            # Adjust probabilities based on symptom duration
            probabilities = self._adjust_by_duration(probabilities, duration)
            
            # Re-sort after adjustment
            top_3_indices = np.argsort(probabilities)[::-1][:3]
            top_3_diseases = [
                (self.disease_encoder.classes_[i], probabilities[i]*100)
                for i in top_3_indices
            ]
            
            result = {
                'predicted_disease': top_3_diseases[0][0],  # Use top disease after duration adjustment
                'model_used': model_name,
                'top_3': top_3_diseases,
                'confidence': probabilities[top_3_indices[0]] * 100,
                'symptom_duration': duration,
                'solutions': get_disease_solutions(top_3_diseases[0][0])
            }
            
            return result
            
        except Exception as e:
            print(f"Error in prediction: {e}")
            return None
    
    def _adjust_by_duration(self, probabilities, duration):
        """
        Adjust disease probabilities based on symptom duration
        
        Args:
            probabilities: Array of disease probabilities
            duration: Duration category ('1-2', '3-7', '1-2w', '2-4w', '4+w')
        
        Returns:
            Adjusted probability array
        """
        # Get all disease names
        diseases = self.disease_encoder.classes_
        
        # Duration-based disease associations
        # Acute conditions (1-2, 3-7 days): cold, flu, gastroenteritis
        acute_keywords = ['cold', 'flu', 'influenza', 'gastroenteritis', 'gastritis', 
                          'acute', 'viral', 'diarrhea', 'vomiting', 'nausea']
        
        # Chronic conditions (2+ weeks): tuberculosis, asthma, diabetes, hypertension
        chronic_keywords = ['tuberculosis', 'asthma', 'diabetes', 'hypertension', 
                            'chronic', 'arthritis', 'cancer', 'pneumonia', 'bronchitis']
        
        # Adjust based on duration
        adjusted = probabilities.copy()
        
        if duration in ['1-2', '3-7']:  # Acute phase (1-7 days)
            # Boost acute diseases, reduce chronic diseases
            for i, disease in enumerate(diseases):
                disease_lower = disease.lower()
                
                # Boost acute conditions
                if any(keyword in disease_lower for keyword in acute_keywords):
                    adjusted[i] *= 1.3  # Boost by 30%
                
                # Reduce chronic conditions
                if any(keyword in disease_lower for keyword in chronic_keywords):
                    adjusted[i] *= 0.6  # Reduce by 40%
        
        elif duration in ['1-2w', '2-4w', '4+w']:  # Chronic phase (1+ weeks)
            # Boost chronic diseases, reduce acute diseases
            for i, disease in enumerate(diseases):
                disease_lower = disease.lower()
                
                # Boost chronic conditions
                if any(keyword in disease_lower for keyword in chronic_keywords):
                    adjusted[i] *= 1.4  # Boost by 40%
                
                # Reduce acute conditions
                if any(keyword in disease_lower for keyword in acute_keywords):
                    adjusted[i] *= 0.5  # Reduce by 50%
        
        # Re-normalize probabilities to sum to 1
        adjusted = adjusted / np.sum(adjusted)
        
        return adjusted
    
    def _create_feature_vector(self, symptoms_dict):
        """
        Create feature vector from symptom selections
        
        Args:
            symptoms_dict: Dictionary with symptoms as keys and 0/1 as values
        
        Returns:
            NumPy array representing the feature vector
        """
        feature_vector = np.zeros(len(self.feature_names))
        
        for i, feature in enumerate(self.feature_names):
            if feature in symptoms_dict:
                feature_vector[i] = symptoms_dict[feature]
        
        return feature_vector
    
    def _normalize_scores(self, scores):
        """
        Normalize decision scores to probabilities
        
        Args:
            scores: Decision function scores
        
        Returns:
            Normalized probability distribution
        """
        # Use softmax-like normalization
        scores = np.asarray(scores).flatten()
        if len(scores) == 1:
            # Binary classification
            sigmoid = 1 / (1 + np.exp(-scores))
            return np.array([1 - sigmoid[0], sigmoid[0]])
        else:
            # Multi-class: use softmax
            exp_scores = np.exp(scores - np.max(scores))
            return exp_scores / np.sum(exp_scores)
    
    def get_all_symptoms(self):
        """
        Get list of all available symptoms
        
        Returns:
            List of symptom names
        """
        return self.feature_names if self.feature_names else []
    
    def get_all_diseases(self):
        """
        Get list of all possible diseases
        
        Returns:
            List of disease names
        """
        return list(self.disease_encoder.classes_) if self.disease_encoder else []


def main():
    """Test the predictor"""
    # Get paths
    project_root = Path(__file__).parent.parent
    models_path = os.path.join(project_root, "models", "trained_models.joblib")
    
    # Initialize predictor
    predictor = DiseasePredictor(models_path)
    
    # Test with random symptoms
    print("\n" + "="*50)
    print("TESTING PREDICTOR")
    print("="*50)
    
    symptoms = predictor.get_all_symptoms()
    diseases = predictor.get_all_diseases()
    
    print(f"\nAvailable symptoms: {len(symptoms)}")
    print(f"Available diseases: {len(diseases)}")
    
    # Create a test case with first 5 symptoms enabled
    test_symptoms = {symptom: 1 if i < 5 else 0 for i, symptom in enumerate(symptoms)}
    
    # Predict
    result = predictor.predict_disease(test_symptoms)
    
    if result:
        print(f"\nPredicted Disease: {result['predicted_disease']}")
        print(f"Confidence: {result['confidence']:.2f}%")
        print("\nTop 3 predictions:")
        for i, (disease, prob) in enumerate(result['top_3'], 1):
            print(f"  {i}. {disease} ({prob:.2f}%)")


if __name__ == "__main__":
    main()
