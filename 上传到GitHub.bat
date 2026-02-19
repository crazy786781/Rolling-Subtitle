@echo off
chcp 65001 >nul 2>nul
cd /d "%~dp0"

set REPO=https://github.com/crazy786781/Rolling-Subtitle.git

echo [1] Git config...
git config --global user.name "crazy786781"
git config --global user.email "mazhiyuan401@163.com"

if not exist ".git" (
    echo [2] Init repo...
    git init
)

echo [3] Add files (by .gitignore)...
git add -A
git status --short
echo.
pause

echo [4] Commit...
git commit -m "Update: core files"
if errorlevel 1 (
    echo No changes or already committed.
)

echo [5] Push...
git remote get-url origin >nul 2>&1
if errorlevel 1 git remote add origin %REPO%
if not errorlevel 1 git remote set-url origin %REPO%
git branch -M main
git push -u origin main
if errorlevel 1 (
    echo Push failed. Check GitHub login and repo: %REPO%
) else (
    echo Done: https://github.com/crazy786781/Rolling-Subtitle
)
pause
