# AI Healthcare Assistant

A comprehensive Python machine learning project with a Graphical User Interface (GUI) for predicting diseases based on symptoms.

## Project Overview

The **AI Healthcare Assistant** is an intelligent system that uses machine learning algorithms to predict diseases based on symptoms selected by users. It provides both a general disease prediction mode and a personal healthcare prediction mode with health profile management.

### Features

- **Machine Learning Models**: 
  - Decision Tree Classifier
  - Random Forest Classifier
  - Support Vector Machine (SVM)

- **GUI Application**:
  - User-friendly Tkinter interface
  - Home screen with multiple options
  - General disease prediction
  - Personal healthcare prediction with profile management
  - Disease probability display (Top 3 predictions)
  - Risk level assessment (LOW/MEDIUM/HIGH)

- **Personal Health Profiles**:
  - Create and manage user profiles
  - Store personal health information
  - Track prediction history
  - Risk score calculation based on disease history

## Project Structure

```
AI_Healthcare_Assistant/
│
├── res/
│   └── Disease and symptoms dataset.csv
│
├── models/
│   └── trained_models.joblib (generated after training)
│
├── profiles/
│   └── (user profiles stored as JSON files)
│
├── src/
│   ├── train_model.py        # Model training script
│   ├── predictor.py          # Disease prediction module
│   ├── personal_health.py    # Health profile management
│   ├── gui_app.py            # Tkinter GUI application
│   └── main.py               # Application entry point
│
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

**Required packages:**
- pandas: Data processing and analysis
- numpy: Numerical computing
- scikit-learn: Machine learning algorithms
- joblib: Model serialization

### Step 2: Verify Dataset

Ensure the dataset file exists at: `res/Disease and symptoms dataset.csv`

The dataset should contain:
- Column "diseases": Target label (disease names)
- Remaining columns: Symptoms (binary values 0 or 1)

## Usage

### Step 1: Train the Models

Before running the GUI application, you must train the machine learning models:

```bash
python src/train_model.py
```

**Expected Output:**
```
Loading dataset...
Dataset shape: (X, Y)
Columns: [list of columns]
Features: [number]
Diseases: [number]
Disease classes: [list of diseases]

==================================================
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
