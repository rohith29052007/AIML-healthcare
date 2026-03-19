"""
Quick Training Script - Simplified and Fast
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

# Get paths
project_root = Path(__file__).parent.parent
data_path = os.path.join(project_root, "res", "Disease and symptoms dataset.csv")
models_dir = os.path.join(project_root, "models")

# Create models directory
os.makedirs(models_dir, exist_ok=True)

print("="*60)
print("QUICK TRAINING - AI Healthcare Assistant")
print("="*60)

# 1. LOAD DATA
print("\n[1/4] Loading dataset (FULL DATA)...")
df = pd.read_csv(data_path)
print(f"✓ Dataset loaded: {df.shape}")

# Get features and target
feature_names = [col for col in df.columns if col.lower() != 'diseases']
X = df[feature_names].copy()

# Clean feature names for LightGBM (remove special characters)
X.columns = [f"feature_{i}" for i in range(len(X.columns))]

y = df['diseases'] if 'diseases' in df.columns else df.iloc[:, 0]

# Remove diseases with only 1 sample (helps with training)
disease_counts = y.value_counts()
diseases_to_keep = disease_counts[disease_counts >= 2].index
mask = y.isin(diseases_to_keep)
X = X[mask].reset_index(drop=True)
y = y[mask].reset_index(drop=True)
print(f"✓ Removed rare diseases. New dataset: {X.shape}")

print(f"✓ Features: {len(feature_names)}")
print(f"✓ Dataset size: {len(X)} samples, {len(feature_names)} symptoms")

# Encode diseases
disease_encoder = LabelEncoder()
y_encoded = disease_encoder.fit_transform(y)
print(f"✓ Diseases: {len(disease_encoder.classes_)}")

# 2. SPLIT DATA
print("\n[2/4] Splitting data (80-20 stratified)...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
)
print(f"✓ Train: {len(X_train)}, Test: {len(X_test)}")

# 3. TRAIN MODELS
print("\n[3/4] Training models...")

models = {}

# Decision Tree with better hyperparameters AND balanced class weights
print("  • Decision Tree...", end=" ", flush=True)
dt = DecisionTreeClassifier(max_depth=25, min_samples_split=5, min_samples_leaf=2, 
                             random_state=42, class_weight='balanced')  # Handles imbalanced data
dt.fit(X_train, y_train)
dt_acc = dt.score(X_test, y_test)
models['decision_tree'] = dt
print(f"✓ {dt_acc*100:.2f}%")

# Random Forest with better hyperparameters AND balanced class weights
print("  • Random Forest...", end=" ", flush=True)
rf = RandomForestClassifier(n_estimators=150, max_depth=20, min_samples_split=5, 
                            min_samples_leaf=2, random_state=42, n_jobs=-1,
                            class_weight='balanced')  # Handles imbalanced data
rf.fit(X_train, y_train)
rf_acc = rf.score(X_test, y_test)
models['random_forest'] = rf
print(f"✓ {rf_acc*100:.2f}%")

# 4. SAVE MODELS
print("\n[4/4] Saving models...")
save_data = {
    'models': models,
    'feature_names': feature_names,
    'disease_encoder': disease_encoder
}
models_file = os.path.join(models_dir, 'trained_models.joblib')
joblib.dump(save_data, models_file)
print(f"✓ Models saved: {models_file}")

print("\n" + "="*60)
print("✅ TRAINING COMPLETE!")
print("="*60)
print("\nAccuracies:")
print(f"  Decision Tree:     {dt_acc*100:.2f}%")
print(f"  Random Forest:     {rf_acc*100:.2f}% ⭐ (Recommended)")

print("\nNext step: Run 'python src/main.py' to launch the GUI!")
print("="*60)
