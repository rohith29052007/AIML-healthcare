"""
Web Application for AI Healthcare Assistant
Flask-based healthcare website with symptom search
"""

from flask import Flask, render_template, request, jsonify, session
import os
from pathlib import Path
import sys

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from predictor import DiseasePredictor
from personal_health import PersonalHealthProfile
from google_drive_downloader import ensure_model_exists

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'aihealth_secret_key_2024'

# Get paths
project_root = Path(__file__).parent.absolute()
models_dir = os.path.join(str(project_root), "models")
models_path = os.path.join(models_dir, "trained_models.joblib")
profiles_dir = os.path.join(str(project_root), "profiles")

print(f"Project root: {project_root}")
print(f"Models directory: {models_dir}")

# Google Drive file ID for the trained model
GOOGLE_DRIVE_FILE_ID = "1fwATKeKNIifk3NUz28jeYWRgejbaGmUJ"

# Try to ensure model exists (download from Google Drive if needed)
print("Checking for trained models...")
model_file = ensure_model_exists(models_dir, GOOGLE_DRIVE_FILE_ID)

# Initialize predictor
predictor = None
health_manager = None

try:
    if model_file and os.path.exists(model_file):
        predictor = DiseasePredictor(model_file)
        health_manager = PersonalHealthProfile(profiles_dir)
        print("✓ Models loaded successfully!")
    else:
        print("⚠ Warning: Models file not found and could not be downloaded")
        print("Prediction features will be unavailable")
except FileNotFoundError as e:
    print(f"⚠ Warning: {e}")
    print("Models will be unavailable. Please ensure Google Drive link is accessible.")
except Exception as e:
    print(f"✗ Error loading models: {e}")
    print("Continuing with limited functionality...")


@app.route('/')
def home():
    """Home page"""
    if not predictor:
        return render_template('index.html', symptoms=[], error="Models not loaded. Please upload trained_models.joblib to models/ directory.")
    symptoms = sorted(predictor.get_all_symptoms())
    return render_template('index.html', symptoms=symptoms)


@app.route('/search_symptoms')
def search_symptoms():
    """API endpoint for symptom search"""
    if not predictor:
        return jsonify({'results': [], 'error': 'Models not loaded'})
    
    query = request.args.get('q', '').lower()
    symptoms = predictor.get_all_symptoms()
    
    # Filter symptoms based on search query
    matching = [s for s in symptoms if query in s.lower()][:15]
    
    return jsonify({
        'results': [{'name': s, 'display': s.replace('_', ' ').title()} for s in matching]
    })


@app.route('/predict', methods=['POST'])
def predict():
    """Predict disease based on symptoms"""
    if not predictor:
        return jsonify({
            'success': False,
            'error': 'Models not available. Please upload trained models.'
        }), 503
    
    try:
        data = request.json
        selected_symptoms = data.get('symptoms', {})
        duration = data.get('duration', '3-7')
        
        # Validate input
        if not selected_symptoms or sum(selected_symptoms.values()) == 0:
            return jsonify({
                'success': False,
                'error': 'Please select at least one symptom'
            }), 400
        
        # Make prediction
        result = predictor.predict_disease(selected_symptoms, duration=duration)
        
        if result:
            return jsonify({
                'success': True,
                'predicted_disease': result['predicted_disease'],
                'confidence': round(result['confidence'], 2),
                'duration': duration,
                'top_3': [
                    {'disease': d, 'probability': round(p, 2)}
                    for d, p in result['top_3']
                ],
                'solutions': result.get('solutions', {})
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Prediction failed. Please try again.'
            }), 500
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/general_predict', methods=['GET', 'POST'])
def general_predict():
    """General prediction page"""
    if not predictor:
        return render_template('general_predict.html', symptoms=[], error="Models not loaded. Please check back later.")
    
    if request.method == 'GET':
        symptoms = sorted(predictor.get_all_symptoms())
        return render_template('general_predict.html', symptoms=symptoms)
    
    return predict()


@app.route('/personal_predict', methods=['GET', 'POST'])
def personal_predict():
    """Personal prediction page"""
    if not predictor:
        return render_template('personal_predict.html', symptoms=[], profiles=[], error="Models not loaded. Please check back later.")
    
    if request.method == 'GET':
        symptoms = sorted(predictor.get_all_symptoms())
        profiles = health_manager.get_available_profiles() if health_manager else []
        return render_template('personal_predict.html', symptoms=symptoms, profiles=profiles)
    
    # Handle prediction
    return predict()


@app.route('/profile/create', methods=['POST'])
def create_profile():
    """Create new user profile"""
    try:
        data = request.json
        name = data.get('name', '').strip()
        age = data.get('age', 0)
        previous_diseases = data.get('previous_diseases', '').split(',')
        previous_diseases = [d.strip() for d in previous_diseases if d.strip()]
        
        # Validate
        is_valid, error_msg = health_manager.validate_profile(name, age)
        if not is_valid:
            return jsonify({'success': False, 'error': error_msg}), 400
        
        # Create profile
        profile = health_manager.create_profile(name, age, previous_diseases)
        health_manager.save_profile()
        
        return jsonify({
            'success': True,
            'profile': profile
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/profile/load/<profile_name>', methods=['GET'])
def load_profile(profile_name):
    """Load user profile"""
    try:
        health_manager.load_profile(f'{profile_name}.json')
        profile = health_manager.current_profile
        
        return jsonify({
            'success': True,
            'profile': profile
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/profile/save_prediction', methods=['POST'])
def save_prediction():
    """Save prediction to user profile"""
    try:
        data = request.json
        disease = data.get('disease', '')
        confidence = data.get('confidence', 0)
        duration = data.get('duration', '3-7')
        
        if health_manager.current_profile:
            profile = health_manager.current_profile
            risk_score, risk_level = health_manager.calculate_risk_score(
                disease,
                profile['previous_diseases']
            )
            
            health_manager.add_prediction_to_history(disease, confidence, risk_level, duration=duration)
            health_manager.save_profile()
            
            return jsonify({
                'success': True,
                'risk_level': risk_level,
                'risk_score': risk_score
            })
        
        return jsonify({'success': False, 'error': 'No profile loaded'}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Contact page"""
    return render_template('contact.html')


@app.template_filter('capitalize_words')
def capitalize_words(text):
    """Filter to capitalize words"""
    return text.replace('_', ' ').title()


if __name__ == '__main__':
    print("\n" + "="*60)
    print("AI HEALTHCARE ASSISTANT - WEB SERVER")
    print("="*60)
    print("\nStarting web server...")
    print("📱 Open browser: http://localhost:5000")
    print("="*60 + "\n")
    
    app.run(debug=True, host='localhost', port=5000)
