# Installation & Setup Guide

## System Requirements

- **Python**: 3.7 or higher
- **Operating System**: Windows, macOS, or Linux
- **RAM**: Minimum 2GB (4GB recommended)
- **Disk Space**: ~500MB for dependencies + dataset

## Detailed Installation Steps

### 1. Verify Python Installation

**Windows (Command Prompt)**:
```bash
python --version
```

**macOS/Linux (Terminal)**:
```bash
python3 --version
```

Should show Python 3.7 or higher. If not, download from [python.org](https://www.python.org/downloads/)

---

### 2. Navigate to Project Directory

**Windows**:
```bash
cd C:\Users\Rohith\Desktop\AIML healthcare
```

**macOS/Linux**:
```bash
cd ~/Desktop/AIML\ healthcare
```

---

### 3. Create Virtual Environment (Optional but Recommended)

Virtual environments keep your project dependencies isolated.

**Windows**:
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**:
```bash
python3 -m venv venv
source venv/bin/activate
```

You'll see `(venv)` at the start of your terminal line when activated.

---

### 4. Install Dependencies

**Using requirements.txt** (Recommended):
```bash
pip install -r requirements.txt
```

**Or install individually**:
```bash
pip install pandas numpy scikit-learn joblib
```

**Verify installation**:
```bash
pip list
```

Should show:
- pandas
- numpy
- scikit-learn
- joblib

---

### 5. Verify Dataset Location

Check that this file exists:
```
C:\Users\Rohith\Desktop\AIML healthcare\res\Disease and symptoms dataset.csv
```

If not, place your CSV file in the `res/` folder.

---

## Training the Models

### Run Training Script

**Windows**:
```bash
python src/train_model.py
```

**macOS/Linux**:
```bash
python3 src/train_model.py
```

### Expected Output:
```
Loading dataset...
Dataset shape: (1500, 44)
Columns: ['diseases', 'anxiety', 'depression', ...]
Features: 43
Diseases: 20
Disease classes: ['anxiety_disorder', 'arthritis', ...]

==================================================
TRAINING MODELS
==================================================

1. Training Decision Tree Classifier...
   Accuracy: 0.9250 (92.50%)

2. Training Random Forest Classifier...
   Accuracy: 0.9450 (94.50%)

3. Training Support Vector Machine (SVM)...
   Accuracy: 0.9200 (92.00%)

==================================================
MODEL TRAINING COMPLETED
==================================================

Saving models...
Models saved to: [path]/models/trained_models.joblib

✓ Training pipeline completed successfully!
```

**Training typically takes 1-5 minutes** depending on your system and dataset size.

---

## Launching the GUI Application

### Run Main Application

**Windows**:
```bash
python src/main.py
```

**macOS/Linux**:
```bash
python3 src/main.py
```

A GUI window titled "AI Healthcare Assistant" will open.

---

## Troubleshooting Installation Issues

### Issue 1: "python: command not found"
**Solution**: 
- Add Python to PATH environment variable
- Use `python3` instead of `python` (especially on macOS/Linux)
- Reinstall Python and check "Add Python to PATH" during installation

### Issue 2: "ModuleNotFoundError: No module named 'pandas'"
**Solution**:
```bash
pip install pandas numpy scikit-learn joblib
```
Or ensure you're using the correct Python interpreter.

### Issue 3: Virtual environment won't activate
**Windows**:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\activate
```

**macOS/Linux**:
```bash
source venv/bin/activate
```

### Issue 4: "Permission denied" error
**Windows**: Run Command Prompt as Administrator

**macOS/Linux**:
```bash
sudo pip install -r requirements.txt
```

### Issue 5: Dataset file not found
**Check**:
1. File path is: `res/Disease and symptoms dataset.csv`
2. Not in a subdirectory like `res/legacy/`
3. File name matches exactly (case-sensitive on Linux)
4. File is readable: `python src/train_model.py`

### Issue 6: Models file not found when running GUI
**Solution**: Train models first
```bash
python src/train_model.py
```

---

## Verify Installation Success

### Step 1: Check Python Packages
```bash
pip list | findstr "pandas numpy scikit sklearn joblib"  # Windows
pip list | grep -E "pandas|numpy|scikit|joblib"  # macOS/Linux
```

### Step 2: Test Dataset Loading
```bash
python -c "import pandas as pd; df = pd.read_csv('res/Disease and symptoms dataset.csv'); print(f'Dataset loaded: {df.shape}')"
```

### Step 3: Run Training
```bash
python src/train_model.py
```

### Step 4: Launch GUI
```bash
python src/main.py
```

If all steps succeed without errors, installation is complete!

---

## Uninstalling / Cleanup

### Remove Virtual Environment
**Windows**:
```bash
rmdir /s venv
```

**macOS/Linux**:
```bash
rm -rf venv
```

### Remove Installed Packages
```bash
pip uninstall -y pandas numpy scikit-learn joblib
```

---

## Advanced Setup

### Using Conda (Alternative to pip)

If you have Anaconda installed:

**Create conda environment**:
```bash
conda create -n healthcare python=3.9
conda activate healthcare
conda install pandas numpy scikit-learn joblib
```

**Then run**:
```bash
python src/train_model.py
python src/main.py
```

### Using Poetry (Alternative to pip)

If you have Poetry installed:

```bash
poetry install
poetry run python src/train_model.py
poetry run python src/main.py
```

---

## Environment Variables (Optional)

For system-wide setup, you can set environment variables:

**Windows (Command Prompt)**:
```bash
setx PYTHONPATH=%PYTHONPATH%;C:\Users\Rohith\Desktop\AIML healthcare
```

**macOS/Linux (Terminal)**:
```bash
export PYTHONPATH="${PYTHONPATH}:~/Desktop/AIML\ healthcare"
```

---

## Quick Reference Commands

| Task | Command |
|------|---------|
| Check Python version | `python --version` |
| Create venv | `python -m venv venv` |
| Activate venv | `venv\Scripts\activate` (Windows) or `source venv/bin/activate` |
| Install dependencies | `pip install -r requirements.txt` |
| Train models | `python src/train_model.py` |
| Run GUI | `python src/main.py` |
| Check packages | `pip list` |
| List installed versions | `pip show pandas numpy scikit-learn joblib` |

---

## Getting Help

If you encounter issues:

1. **Check console output** for specific error messages
2. **Read README.md** for detailed documentation
3. **Review QUICKSTART.md** for common solutions
4. **Check file permissions** (files must be readable)
5. **Verify dataset exists** and is in correct location
6. **Try reinstalling** packages: `pip install -r requirements.txt --upgrade`

---

## Success Indicators

✅ Python installed (version 3.7+)  
✅ Virtual environment created (optional)  
✅ All dependencies installed  
✅ Dataset file exists in `res/` folder  
✅ Model training completes successfully  
✅ GUI application launches without errors  
✅ Can make predictions and create profiles  

---

**Installation Complete!** You're ready to use AI Healthcare Assistant.

Start with: `python src/train_model.py`
