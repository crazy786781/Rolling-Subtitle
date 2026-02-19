@echo off
cd /d "%~dp0"

echo [1/4] Init Git repo...
git init
if errorlevel 1 (
    echo.
    echo Git not found. Please install Git for Windows:
    echo   https://git-scm.com/download/win
    echo Install then restart cmd and run this script again.
    echo.
    pause
    exit /b 1
)

echo.
echo [2/4] Add files...
git add .
if errorlevel 1 ( echo Add failed. & pause & exit /b 1 )

echo.
echo [3/4] Files to commit:
git status --short

echo.
echo [4/4] First commit...
git commit -m "Initial commit: earthquake alert subtitle app"
if errorlevel 1 (
    echo.
    echo If Git asks for user.name / user.email, run:
    echo   git config --global user.name "YourName"
    echo   git config --global user.email "your@email.com"
    echo Then run this script again.
    pause
    exit /b 1
)

echo.
echo Done. Next: push to GitHub (run git_push.bat or run below in this folder):
echo   git remote add origin https://github.com/crazy786781/Rolling-Subtitle.git
echo   git branch -M main
echo   git push -u origin main
echo.
pause
