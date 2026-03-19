@echo off
REM Setup script for Netlify deployment

echo ============================================
echo Setting up Git for Netlify Deployment
echo ============================================

REM Initialize git if not already done
if not exist .git (
    echo Initializing Git repository...
    git init
    echo Configuring Git user...
    git config user.email "developer@example.com"
    git config user.name "Developer"
) else (
    echo Git repository already initialized
)

echo.
echo Adding files...
git add .

echo.
echo Creating initial commit...
git commit -m "AI Healthcare Assistant - Ready for Netlify deployment"

echo.
echo ============================================
echo Git setup complete!
echo ============================================
echo.
echo Next steps:
echo 1. Go to https://github.com/new
echo 2. Create a new repository named 'aiml-healthcare'
echo 3. Copy the SSH commands and run them here
echo 4. Then deploy on Netlify
echo.
pause
