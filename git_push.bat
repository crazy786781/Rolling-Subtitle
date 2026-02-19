@echo off
cd /d "%~dp0"

git rev-parse HEAD >nul 2>&1
if errorlevel 1 (
    echo No commit yet. Run git_init_and_commit.bat first to init and commit.
    pause
    exit /b 1
)

git remote get-url origin >nul 2>&1
if errorlevel 1 (
    echo Adding remote origin...
    git remote add origin https://github.com/crazy786781/Rolling-Subtitle.git
)

echo Pushing to GitHub...
git branch -M main
git push -u origin main
if errorlevel 1 (
    echo.
    echo Push failed. Check: 1^) GitHub login 2^) Repo exists: https://github.com/crazy786781/Rolling-Subtitle
    pause
    exit /b 1
)
echo.
echo Push done: https://github.com/crazy786781/Rolling-Subtitle
pause
