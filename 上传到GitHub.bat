@echo off
set "WD=%~dp0"
cd /d "%WD%"

set "REPO=https://github.com/crazy786781/Rolling-Subtitle.git"

echo Step 1 Git config
git config --global user.name "crazy786781"
git config --global user.email "mazhiyuan401@163.com"

if not exist ".git" (
    echo Step 2 Init repo
    git init
)

echo Step 3 Clean repo
git rm --cached build.bat build_debug.bat build_debug_run.bat 2>nul
git rm --cached build_lite.spec build_lite_debug.spec 2>nul
if exist "%WD%cleanup_only.sh" (
    where bash >nul 2>&1
    if not errorlevel 1 bash "%WD%cleanup_only.sh" 2>nul
)

echo Step 4 Add files
git add -A
git status --short
echo.
pause

echo Step 5 Commit
git commit -m "Update core files"
if errorlevel 1 echo No changes to commit.

echo Step 6 Push
git remote get-url origin >nul 2>&1
if errorlevel 1 git remote add origin %REPO%
if not errorlevel 1 git remote set-url origin %REPO%
git branch -M main
git push -u origin main
if errorlevel 1 (
    echo Push failed. Try VPN or run again later.
) else (
    echo Done. https://github.com/crazy786781/Rolling-Subtitle
)
pause
