# AI Healthcare Assistant - Production Deployment

A web-based disease prediction system using trained machine learning models. Users can input symptoms and receive disease predictions.

## 🚀 Features

- **Web Interface**: Flask-based web application
- **Disease Prediction**: Input symptoms → Get predicted diseases with probabilities
- **Top 3 Predictions**: Shows the most likely diseases with confidence scores
- **Personal Health Profiles**: Create user profiles and track prediction history
- **Risk Assessment**: Categorizes risk levels (LOW/MEDIUM/HIGH)

## 📋 Prerequisites

- Python 3.8+
- pip or conda

## 🔧 Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/aiml-healthcare.git
cd aiml-healthcare
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 🎯 Running Locally

### Start Web Application
```bash
python web_app.py
```

Then open your browser and visit:
```
http://localhost:5000
```

## 🌐 Deployment on Render

### 1. Push to GitHub
```bash
git add .
git commit -m "Deploy AI Healthcare Assistant"
git push origin main
```

### 2. Deploy on Render
1. Go to [render.com](https://render.com)
2. Sign in with GitHub
3. Create new **Web Service**
4. Connect your repository
5. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn web_app:app`

### 3. Live Application
Your app will be available at:
```
https://aiml-healthcare-<random>.onrender.com
```

## 📁 Project Structure

```
aiml-healthcare/
├── web_app.py              # Main Flask application
├── requirements.txt        # Python dependencies
├── Procfile                # Deployment configuration
├── render.yaml             # Render service config
├── models/
│   └── trained_models.joblib   # Pre-trained ML models
├── src/
│   ├── predictor.py        # Disease prediction logic
│   ├── personal_health.py  # User profile management
│   └── recommendations.py  # Disease recommendations
├── templates/
│   ├── index.html          # Home page
│   ├── general_predict.html    # Prediction interface
│   ├── personal_predict.html   # Personal predictions
│   └── base.html           # Base template
└── README.md               # This file
```

## 🔮 How It Works

1. **User Input**: Select symptoms from the available list
2. **Model Inference**: Pre-trained ML models process the symptoms
3. **Prediction**: System returns:
   - Top 3 predicted diseases
   - Probability/confidence scores
   - Risk level assessment
4. **Profile Management**: Save predictions to user profile (optional)

## 📊 Models

The system uses pre-trained machine learning models:
- **Decision Tree Classifier**: Fast, interpretable predictions
- **Random Forest**: Ensemble method for robust predictions
- **XGBoost**: Gradient boosting for high accuracy

All models are trained and saved in `models/trained_models.joblib`

## 🎨 Web Interface

### Available Endpoints

| URL | Purpose |
|-----|---------|
| `/` | Home page |
| `/general_predict` | General disease prediction |
| `/personal_predict` | Personal health profile predictions |
| `/search_symptoms` | Symptom search API |
| `/predict` | Prediction API (POST) |
| `/about` | About page |
| `/contact` | Contact page |

## ⚙️ Configuration

### Environment Variables
- `PORT`: Server port (default: 5000)
- `RENDER`: Set automatically by Render

### Model Organization
Models and encoders are stored in `models/trained_models.joblib`:
- Decision Tree model
- Random Forest model
- Feature names
- Disease encoder/decoder

## 📱 User Interface Modes

### 1. General Prediction
- Search and select symptoms from the complete symptom list
- Get instant disease predictions
- View top 3 diseases with probabilities

### 2. Personal Health Profile
- Create and manage user profiles
- Save prediction history
- Track risk scores over time
- Personalized recommendations based on history

## 🐛 Troubleshooting

### Models not loading
```
Error: Models file not found
```
**Solution**: Ensure `models/trained_models.joblib` exists in the project root.

### Port already in use
```
Address already in use
```
**Solution**: Change port or kill existing process:
```bash
# Windows
netstat -ano | findstr :5000
# Kill the process
taskkill /PID <PID> /F
```

### Dependencies missing
```
ModuleNotFoundError
```
**Solution**: Reinstall dependencies:
```bash
pip install -r requirements.txt
```

## 📝 Notes

- This is a **prediction-only** deployment (model inference)
- Model training code is not included (uses pre-trained models)
- User profiles are stored locally in `profiles/` directory

## 🔐 Security

- No sensitive user data is transmitted externally
- All predictions processed locally
- HTTPS recommended for production deployment

## 📄 License

This project is for educational purposes.

---

**Version**: 1.0 (Production)
**Last Updated**: March 2026
TRAINING MODELS
==================================================

1. Training Decision Tree Classifier...
   Accuracy: 0.XXXX (XX.XX%)

2. Training Random Forest Classifier...
   Accuracy: 0.XXXX (XX.XX%)

3. Training Support Vector Machine (SVM)...
   Accuracy: 0.XXXX (XX.XX%)

==================================================
MODEL TRAINING COMPLETED
==================================================

Saving models...
Models saved to: [path]/models/trained_models.joblib

✓ Training pipeline completed successfully!
```

This will:
- Load the dataset from `res/` folder
- Separate features (symptoms) and target (diseases)
- Train three different ML models
- Display accuracy for each model
- Save trained models to `models/trained_models.joblib`

### Step 2: Run the GUI Application

Launch the AI Healthcare Assistant:

```bash
python src/main.py
```

A GUI window will open showing the home screen.

## GUI Application Guide

### Home Screen

The home screen presents three main options:

1. **General Disease Prediction**
   - Select symptoms from a scrollable list
   - Get instant disease predictions
   - View top 3 possible diseases with probabilities
   - No personal information required

2. **Personal Healthcare Prediction**
   - Create or load a personal health profile
   - Enter name, age, and previous diseases
   - Select symptoms
   - Get predictions with risk level assessment
   - Store prediction history

3. **Exit**
   - Close the application

### General Disease Prediction Workflow

1. Click "General Disease Prediction" on home screen
2. Select symptoms using checkboxes
3. Click "Predict Disease" button
4. View results showing:
   - Predicted Disease
   - Confidence percentage
   - Top 3 possible diseases with probabilities

### Personal Healthcare Prediction Workflow

1. Click "Personal Healthcare Prediction" on home screen
2. Choose to load existing profile or create new one
3. If creating new profile:
   - Enter your name
   - Enter your age
   - Enter previous diseases (comma-separated)
   - Click "Save Profile and Continue"
4. Select symptoms
5. Click "Predict Disease" button
6. View results showing:
   - Predicted Disease
   - Confidence percentage
   - **Risk Level: LOW/MEDIUM/HIGH** (based on disease history)
   - Top 3 possible diseases with probabilities

### Profile Management

- Profiles are automatically saved as JSON files in the `profiles/` folder
- Each user can have only one active profile
- Prediction history is automatically tracked and saved
- Load previous profiles from the personal prediction screen

## Sample Dataset Format

```csv
diseases,anxiety,depression,shortness_of_breath,chest_pain,dizziness,insomnia,...
Panic Disorder,1,0,1,1,0,0,...
Anxiety Disorder,1,1,0,0,1,1,...
Heart Disease,0,0,1,1,1,0,...
```

## Code Quality

The project follows best practices:

- **Modular Design**: Separate modules for training, prediction, health profiles, and GUI
- **Class-Based Architecture**: Organized code using Python classes
- **Error Handling**: Comprehensive error handling and user feedback
- **Documentation**: Detailed comments and docstrings throughout
- **Type Hints**: Function parameters and return types documented
- **Configuration Management**: Flexible path management for different environments

## Troubleshooting

### Error: "Models file not found"
- **Solution**: Run `python src/train_model.py` first to train and save models

### Error: "Dataset not found"
- **Solution**: Ensure `res/Disease and symptoms dataset.csv` exists in the correct location

### Error: "ModuleNotFoundError"
- **Solution**: Install dependencies with `pip install -r requirements.txt`

### GUI Not Responsive
- **Solution**: The GUI uses Tkinter which is built-in to Python. Ensure Python is properly installed.

### Low Model Accuracy
- **Solution**: Check dataset quality and ensure it contains enough samples for each disease class

## Algorithm Details

### Decision Tree Classifier
- Simple and interpretable model
- Maximum depth: 15 layers
- Fast prediction time

### Random Forest Classifier
- Ensemble method with 100 trees
- Better accuracy and robustness
- Maximum depth per tree: 15
- Parallel processing enabled

### Support Vector Machine (SVM)
- Non-linear kernel (RBF)
- Good generalization on complex data
- Probability estimates enabled for confidence scores

## Model Performance

The models are trained on an 80-20 train-test split. To check individual model accuracies, run the training script and note the displayed accuracy percentages.

## Personal Health Profile Format

User profiles are stored as JSON files in the `profiles/` folder:

```json
{
  "name": "John Doe",
  "age": 40,
  "previous_diseases": ["diabetes", "hypertension"],
  "created_date": "2024-01-15 10:30:45",
  "predictions_history": [
    {
      "timestamp": "2024-01-15 10:35:20",
      "disease": "Diabetes",
      "confidence": 85.5,
      "risk_level": "HIGH"
    }
  ]
}
```

## Risk Level Calculation

Risk levels are calculated based on:
- **Base Score**: 50%
- **Disease Match**: +30% if predicted disease matches previous disease history
- **Final Categories**:
  - LOW: Score < 40
  - MEDIUM: Score 40-70
  - HIGH: Score >= 70

## System Requirements

- **OS**: Windows, macOS, or Linux
- **Python**: 3.7+
- **RAM**: Minimum 2GB (recommended 4GB)
- **Disk Space**: ~500MB (including dependencies)

## Performance Notes

- Initial model training takes ~1-5 minutes depending on dataset size
- Predictions are made in real-time (usually < 1 second)
- GUI is responsive and handles all operations smoothly
- Models are cached in memory after loading

## Future Enhancements

Possible improvements for future versions:
- Data visualization (charts, graphs)
- Multiple language support
- Advanced filtering of symptoms
- Integration with medical databases
- Mobile app version
- Cloud-based predictions
- User authentication

## License

This project is created for educational purposes.

## Support

For issues or questions:
1. Check the Troubleshooting section
2. Verify all dependencies are installed
3. Ensure dataset is in correct location
4. Review error messages in console output

## Credits

Created as a comprehensive demonstration of Python machine learning with GUI development using Tkinter.

---

**Version**: 1.0  
**Last Updated**: 2024  
**Status**: Ready for Production Use
