"""
Model Training Module
Handles data loading, preprocessing, and training of ML models
"""

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
import os
from pathlib import Path

class ModelTrainer:
    """Class to handle model training and management"""
    
    def __init__(self, data_path, models_dir="models"):
        """
        Initialize ModelTrainer
        
        Args:
            data_path: Path to the CSV dataset
            models_dir: Directory to save trained models
        """
        self.data_path = data_path
        self.models_dir = models_dir
        self.models = {}
        self.label_encoder = None
        self.feature_names = None
        self.disease_encoder = None
        self.X_train = None
        self.y_train = None
        self.y_train_original = None
        
        # Create models directory if it doesn't exist
        os.makedirs(models_dir, exist_ok=True)
    
    def load_data(self):
        """Load and preprocess the dataset"""
        print("Loading dataset (FULL DATA)...")
        try:
            # Read CSV file - full dataset
            df = pd.read_csv(self.data_path)
            
            print(f"Dataset shape: {df.shape}")
            
            # Store feature names (all columns except 'diseases')
            self.feature_names = [col for col in df.columns if col.lower() != 'diseases']
            
            # Extract target
            y = df['diseases'] if 'diseases' in df.columns else df.iloc[:, 0]
            
            # Remove rare diseases (< 2 samples) for stratified train-test split
            disease_counts = y.value_counts()
            rare_diseases = disease_counts[disease_counts < 2].index
            
            if len(rare_diseases) > 0:
                print(f"Removing {len(rare_diseases)} rare diseases with < 2 samples...")
                print(f"Diseases removed: {rare_diseases.tolist()}")
                df = df[~df['diseases'].isin(rare_diseases)]
                y = df['diseases']
                print(f"Dataset shape after filtering: {df.shape}")
            
            # Extract features
            X = df[self.feature_names]
            
            # Encode diseases to numeric labels
            self.disease_encoder = LabelEncoder()
            y_encoded = self.disease_encoder.fit_transform(y)
            
            # Store for later use in predictions
            self.y_train_original = y
            
            print(f"Features: {len(self.feature_names)}")
            print(f"Diseases: {len(self.disease_encoder.classes_)}")
            print(f"Disease classes (first 20): {self.disease_encoder.classes_[:20].tolist()}")
            
            return X, y_encoded, y
            
        except Exception as e:
            print(f"Error loading data: {e}")
            raise
    
    def train_models(self, X, y):
        """
        Train all three models
        
        Args:
            X: Feature matrix
            y: Target labels (encoded)
        """
        print("\n" + "="*50)
        print("TRAINING MODELS")
        print("="*50)
        
        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        self.X_train = X_train
        self.y_train = y_train
        
        # 1. Decision Tree Classifier
        print("\n1. Training Decision Tree Classifier...")
        print("   Hyperparameters: max_depth=None (unlimited), min_samples_split=2, min_samples_leaf=1")
        dt_model = DecisionTreeClassifier(max_depth=None, min_samples_split=2, min_samples_leaf=1, 
                                         random_state=42, class_weight='balanced')
        dt_model.fit(X_train, y_train)
        dt_accuracy = dt_model.score(X_test, y_test)
        self.models['decision_tree'] = dt_model
        print(f"   Accuracy: {dt_accuracy:.4f} ({dt_accuracy*100:.2f}%)")
        
        # 2. Random Forest Classifier
        print("\n2. Training Random Forest Classifier...")
        print("   Hyperparameters: n_estimators=100, max_depth=30, min_samples_split=2, min_samples_leaf=1")
        rf_model = RandomForestClassifier(n_estimators=100, max_depth=30, min_samples_split=2,
                                         min_samples_leaf=1, random_state=42, n_jobs=-1,
                                         class_weight='balanced')
        rf_model.fit(X_train, y_train)
        rf_accuracy = rf_model.score(X_test, y_test)
        self.models['random_forest'] = rf_model
        print(f"   Accuracy: {rf_accuracy:.4f} ({rf_accuracy*100:.2f}%)")
        
        print("\n" + "="*50)
        print("MODEL TRAINING COMPLETED")
        print("="*50)
        
        return {
            'decision_tree': dt_accuracy,
            'random_forest': rf_accuracy
        }
    
    def save_models(self):
        """Save trained models to disk using joblib"""
        print("\nSaving models...")
        
        models_file = os.path.join(self.models_dir, 'trained_models.joblib')
        
        # Save all models and encoders in a dictionary
        data_to_save = {
            'models': self.models,
            'feature_names': self.feature_names,
            'disease_encoder': self.disease_encoder
        }
        
        joblib.dump(data_to_save, models_file)
        print(f"Models saved to: {models_file}")
        
        return models_file
    
    def train_and_save(self):
        """Complete pipeline: load data, train models, and save"""
        try:
            # Load data
            X, y_encoded, y_original = self.load_data()
            
            # Train models
            accuracies = self.train_models(X, y_encoded)
            
            # Save models
            self.save_models()
            
            print("\n✓ Training pipeline completed successfully!")
            return True
            
        except Exception as e:
            print(f"\n✗ Error in training pipeline: {e}")
            return False


def main():
    """Main function to run model training"""
    # Get the project root directory
    project_root = Path(__file__).parent.parent
    data_path = os.path.join(project_root, "res", "Disease and symptoms dataset.csv")
    models_dir = os.path.join(project_root, "models")
    
    # Check if data file exists
    if not os.path.exists(data_path):
        print(f"Error: Dataset not found at {data_path}")
        return
    
    # Create and run trainer
    trainer = ModelTrainer(data_path, models_dir)
    trainer.train_and_save()


if __name__ == "__main__":
    main()
