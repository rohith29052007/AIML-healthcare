# How to Deploy Models on Render

## Problem
The trained ML models file (`trained_models.joblib`) is too large (~3.9 GB) to push to GitHub.

## Solution: Upload Models via Render

### Step 1: Prepare the Models Locally
The models are already trained:
```
C:\Users\Rohith\Desktop\AIML healthcare\models\trained_models.joblib
```

### Step 2: Deploy on Render (Without Models First)
1. Go to https://render.com
2. Connect your GitHub repo
3. Click "New +" → "Web Service"
4. Select your AIML-healthcare repository
5. Set Start Command: `gunicorn web_app:app`
6. Click "Deploy"

### Step 3: Upload Models to Render
Once deployed, use Render's file upload feature or Rclone:

**Option A: Using Render Dashboard (Easiest)**
1. Go to your Render service dashboard
2. Look for "Files" or "Storage" section
3. Upload the `trained_models.joblib` file to the `models/` directory

**Option B: Using SFTP (Advanced)**
1. Get Render service details from dashboard
2. Use WinSCP or FileZilla to connect via SFTP
3. Upload file to `models/` directory

### Step 4: Restart the Service
- Click "Restart service" in Render dashboard
- App will now load the models automatically!

---

## Production Alternative
For permanent solution, consider:
- **AWS S3**: Store models in S3, download during app startup
- **Google Cloud Storage**: Similar to S3
- **Model Compression**: Use techniques to reduce model size (<100MB)

---

**Your deployed app will work without models (shows error message), but will fully function once models are uploaded!**
