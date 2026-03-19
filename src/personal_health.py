"""
Personal Health Profile Module
Handles creation and management of personal health profiles
"""

import json
import os
from pathlib import Path
from datetime import datetime


class PersonalHealthProfile:
    """Class to manage personal health profiles"""
    
    def __init__(self, profiles_dir="profiles"):
        """
        Initialize PersonalHealthProfile
        
        Args:
            profiles_dir: Directory to store user profiles
        """
        self.profiles_dir = profiles_dir
        self.current_profile = None
        
        # Create profiles directory if it doesn't exist
        os.makedirs(profiles_dir, exist_ok=True)
    
    def create_profile(self, name, age, previous_diseases):
        """
        Create a new health profile
        
        Args:
            name: User's name
            age: User's age
            previous_diseases: List of previous diseases
        
        Returns:
            Profile dictionary
        """
        profile = {
            "name": name.strip(),
            "age": int(age),
            "previous_diseases": [d.strip().lower() for d in previous_diseases if d.strip()],
            "created_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "predictions_history": []
        }
        
        self.current_profile = profile
        return profile
    
    def save_profile(self, profile=None):
        """
        Save profile to JSON file
        
        Args:
            profile: Profile to save (uses current_profile if None)
        
        Returns:
            Path to saved profile file
        """
        if profile is None:
            profile = self.current_profile
        
        if profile is None:
            print("Error: No profile to save")
            return None
        
        # Create filename from user name
        filename = f"profile_{profile['name'].replace(' ', '_').lower()}.json"
        filepath = os.path.join(self.profiles_dir, filename)
        
        try:
            with open(filepath, 'w') as f:
                json.dump(profile, f, indent=4)
            print(f"✓ Profile saved: {filepath}")
            return filepath
        except Exception as e:
            print(f"Error saving profile: {e}")
            return None
    
    def load_profile(self, filename):
        """
        Load profile from JSON file
        
        Args:
            filename: Name of file to load
        
        Returns:
            Profile dictionary
        """
        filepath = os.path.join(self.profiles_dir, filename)
        
        try:
            with open(filepath, 'r') as f:
                profile = json.load(f)
            self.current_profile = profile
            print(f"✓ Profile loaded: {filepath}")
            return profile
        except Exception as e:
            print(f"Error loading profile: {e}")
            return None
    
    def get_available_profiles(self):
        """
        Get list of available profile files
        
        Returns:
            List of profile filenames
        """
        try:
            profiles = [f for f in os.listdir(self.profiles_dir) if f.endswith('.json')]
            return sorted(profiles)
        except:
            return []
    
    def calculate_risk_score(self, predicted_disease, previous_diseases):
        """
        Calculate risk score based on disease history
        
        Args:
            predicted_disease: Newly predicted disease
            previous_diseases: List of previous diseases
        
        Returns:
            Risk score (0-100) and risk level (LOW/MEDIUM/HIGH)
        """
        risk_score = 50  # Base score
        
        # Check if predicted disease is in history
        predicted_lower = predicted_disease.lower()
        
        for prev_disease in previous_diseases:
            prev_disease_lower = prev_disease.lower()
            
            # Increase risk if disease was previously diagnosed
            if prev_disease_lower in predicted_lower or predicted_lower in prev_disease_lower:
                risk_score += 30
                break
        
        # Determine risk level
        if risk_score < 40:
            risk_level = "LOW"
        elif risk_score < 70:
            risk_level = "MEDIUM"
        else:
            risk_level = "HIGH"
        
        return risk_score, risk_level
    
    def add_prediction_to_history(self, predicted_disease, confidence, risk_level, duration='3-7'):
        """
        Add prediction to history
        
        Args:
            predicted_disease: Disease prediction
            confidence: Confidence percentage
            risk_level: Risk level
            duration: Duration of symptoms
        """
        if self.current_profile is None:
            return
        
        prediction_record = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "disease": predicted_disease,
            "confidence": confidence,
            "risk_level": risk_level,
            "symptom_duration": duration
        }
        
        self.current_profile["predictions_history"].append(prediction_record)
    
    def get_prediction_history(self):
        """
        Get prediction history for current profile
        
        Returns:
            List of predictions
        """
        if self.current_profile is None:
            return []
        
        return self.current_profile.get("predictions_history", [])
    
    def validate_profile(self, name, age):
        """
        Validate profile input
        
        Args:
            name: User's name
            age: User's age
        
        Returns:
            Tuple (is_valid, error_message)
        """
        if not name or not name.strip():
            return False, "Name cannot be empty"
        
        try:
            age_int = int(age)
            if age_int < 0 or age_int > 150:
                return False, "Age must be between 0 and 150"
        except ValueError:
            return False, "Age must be a valid number"
        
        return True, ""
    
    def get_profile_summary(self):
        """
        Get summary of current profile
        
        Returns:
            Dictionary with profile summary
        """
        if self.current_profile is None:
            return None
        
        return {
            "name": self.current_profile["name"],
            "age": self.current_profile["age"],
            "disease_count": len(self.current_profile["previous_diseases"]),
            "prediction_count": len(self.current_profile["predictions_history"]),
            "created_date": self.current_profile["created_date"]
        }


def main():
    """Test the personal health profile module"""
    print("Testing Personal Health Profile Module")
    print("="*50)
    
    # Create profile manager
    manager = PersonalHealthProfile()
    
    # Create a test profile
    profile = manager.create_profile(
        name="John Doe",
        age=40,
        previous_diseases=["diabetes", "hypertension"]
    )
    
    print(f"\nCreated profile for: {profile['name']}")
    print(f"Age: {profile['age']}")
    print(f"Previous diseases: {profile['previous_diseases']}")
    
    # Save profile
    manager.save_profile()
    
    # Test risk calculation
    risk_score, risk_level = manager.calculate_risk_score(
        "diabetes",
        profile["previous_diseases"]
    )
    print(f"\nRisk Score for 'diabetes': {risk_score} ({risk_level})")
    
    # Add prediction to history
    manager.add_prediction_to_history("diabetes", 85.5, "HIGH")
    manager.save_profile()
    
    # Get summary
    summary = manager.get_profile_summary()
    print(f"\nProfile Summary: {summary}")
    
    print("\n✓ Testing completed successfully!")


if __name__ == "__main__":
    main()
