#!/usr/bin/env pwsh

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Deploying to Netlify - Complete Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Step 1: Initialize Git
Write-Host "Step 1: Initializing Git repository..." -ForegroundColor Green
git init
sleep 1

# Step 2: Configure Git user
Write-Host "Step 2: Configuring Git user..." -ForegroundColor Green
git config user.email "rohith@example.com"
git config user.name "Rohith"
sleep 1

# Step 3: Add all files
Write-Host "Step 3: Adding files to Git..." -ForegroundColor Green
git add .
sleep 1

# Step 4: Commit
Write-Host "Step 4: Creating initial commit..." -ForegroundColor Green
git commit -m "AI Healthcare Assistant - Ready for Netlify deployment"
sleep 1

# Step 5: Branch rename
Write-Host "Step 5: Setting up main branch..." -ForegroundColor Green
git branch -M main
sleep 1

# Status
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "✓ Local Git setup complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "NEXT STEPS:" -ForegroundColor Yellow
Write-Host ""
Write-Host "1. Create GitHub Repository:" -ForegroundColor Cyan
Write-Host "   - Go to https://github.com/new" -ForegroundColor White
Write-Host "   - Repository name: aiml-healthcare" -ForegroundColor White
Write-Host "   - Make it PUBLIC" -ForegroundColor White
Write-Host "   - Click 'Create repository'" -ForegroundColor White
Write-Host ""

Write-Host "2. Connect to GitHub (copy these commands after creating repo):" -ForegroundColor Cyan
Write-Host "   git remote add origin https://github.com/YOUR_USERNAME/aiml-healthcare.git" -ForegroundColor White
Write-Host "   git push -u origin main" -ForegroundColor White
Write-Host ""

Write-Host "3. Deploy on Netlify:" -ForegroundColor Cyan
Write-Host "   - Go to https://netlify.com" -ForegroundColor White
Write-Host "   - Click 'Sign up with GitHub'" -ForegroundColor White
Write-Host "   - Click 'New site from Git'" -ForegroundColor White
Write-Host "   - Select your aiml-healthcare repository" -ForegroundColor White
Write-Host "   - Click 'Deploy site'" -ForegroundColor White
Write-Host ""

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Your app will be live with a shareable URL!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
