@echo off
setlocal
cd /d "%~dp0."

echo ========================================
echo Build Debug (with console)
echo ========================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found. Add Python to PATH.
    goto end
)

python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo [WARN] PyInstaller not found. Installing...
    python -m pip install pyinstaller
    if errorlevel 1 (
        echo [ERROR] Failed to install PyInstaller
        goto end
    )
)

echo [1/4] Dependencies...
if exist requirements.txt (
    python -m pip install -r requirements.txt >nul 2>&1
    if errorlevel 1 python -m pip install PyQt5 websockets requests Pillow >nul 2>&1
) else (
    python -m pip install PyQt5 websockets requests Pillow >nul 2>&1
)

echo [2/4] Resources...
if not exist "fe_fix.txt" echo [WARN] fe_fix.txt not found
if not exist "logo\icon.ico" echo [WARN] logo\icon.ico not found

echo [3/4] PyInstaller...
pyinstaller build_lite_debug.spec --clean --distpath debug
if errorlevel 1 (
    echo [ERROR] Build failed. See above.
    goto end
)

echo [4/4] Done.
echo ========================================
echo Output folder: debug\
echo ========================================

:end
echo.
pause
