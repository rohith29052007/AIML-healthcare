# Netlify Deployment Guide

## Step 1: Set Up Git Locally

Open PowerShell in your project directory and run:

```powershell
git init
git config user.email "your-email@example.com"
git config user.name "Your Name"
git add .
git commit -m "Initial commit - AI Healthcare Assistant for Netlify"
```

## Step 2: Create GitHub Repository

1. Go to [github.com](https://github.com)
2. Click **+** (top right) → **New repository**
3. Name: `aiml-healthcare` (or any name)
4. Description: `AI Healthcare Assistant - Disease Prediction System`
5. Make it **Public**
6. Click **Create repository**

## Step 3: Push Code to GitHub

Copy the commands from GitHub and run them:

```powershell
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/aiml-healthcare.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

## Step 4: Deploy on Netlify

1. Go to [netlify.com](https://netlify.com)
2. Click **Sign up** → Choose **GitHub**
3. Authorize Netlify to access your GitHub
4. Click **New site from Git**
5. Select your `aiml-healthcare` repository
6. Configure:
   - **Build command**: `pip install -r requirements.txt && python src/train_model.py`
   - **Publish directory**: `.` (leave as is)
7. Click **Deploy site**

## Step 5: Get Your Live URL

Once deployed, Netlify will show your site URL like:
```
https://your-app-name.netlify.app
```

Share this link with others to use your app!

---

## Files Already Created

✅ `netlify.toml` - Netlify configuration
✅ `requirements.txt` - Updated with Flask & gunicorn  
✅ `functions/index.js` - Serverless function wrapper
✅ `.gitignore` - Git ignore rules

You're ready to deploy!
