# Quick Start Guide - AI Healthcare Assistant

## Get Started in 3 Steps

### Step 1: Install Dependencies (2 minutes)

Open terminal/command prompt and run:

```bash
pip install -r requirements.txt
```

Or install packages individually:

```bash
pip install pandas numpy scikit-learn joblib
```

### Step 2: Train Models (3-5 minutes)

Run the training script:

```bash
python src/train_model.py
```

You'll see output like:
```
Loading dataset...
Dataset shape: (X, Y)

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
✓ Training pipeline completed successfully!
```

### Step 3: Launch GUI (1 minute)

Run the application:

```bash
python src/main.py
```

A GUI window will open. You're ready to use AI Healthcare Assistant!

---

## Using the Application

### For General Prediction:
1. Click "General Disease Prediction"
2. Check symptoms you're experiencing
3. Click "Predict Disease"
4. View results with top 3 predictions

### For Personal Prediction:
1. Click "Personal Healthcare Prediction"
2. Create a new profile (name, age, previous diseases)
3. Check symptoms
4. Click "Predict Disease"
5. View results with risk level

---

## Folder Structure After Setup

```
AIML healthcare/
├── res/
│   └── Disease and symptoms dataset.csv
├── src/
│   ├── train_model.py
│   ├── predictor.py
│   ├── personal_health.py
│   ├── gui_app.py
│   └── main.py
├── models/
│   └── trained_models.joblib  (created after training)
├── profiles/
│   └── (created after making predictions)
├── requirements.txt
├── README.md
└── QUICKSTART.md
```

---

## Common Issues & Solutions

| Problem | Solution |
|---------|----------|
| "ModuleNotFoundError" | Run `pip install -r requirements.txt` |
| "Models file not found" | Run `python src/train_model.py` |
| "No module named 'tkinter'" | Tkinter comes with Python - may need to update Python |
| GUI window won't open | Try running from command prompt to see error messages |

---

## Next Steps

- Read [README.md](README.md) for detailed documentation
- Explore the code files in `src/` folder
- Check your predictions in the `profiles/` folder (JSON files)

**Enjoy using AI Healthcare Assistant!**
