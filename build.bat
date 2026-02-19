@echo off
setlocal
echo ========================================
echo Build script - Earthquake Alert Scroller
echo ========================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found. Please install Python and add it to PATH.
    pause
    exit /b 1
)

REM Check PyInstaller
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo [WARN] PyInstaller not found. Installing...
    python -m pip install pyinstaller
    if errorlevel 1 (
        echo [ERROR] Failed to install PyInstaller
        pause
        exit /b 1
    )
)

REM Check dependencies
echo [1/5] Checking dependencies...
if exist requirements.txt (
    echo Installing from requirements.txt...
    python -m pip install -r requirements.txt
    if errorlevel 1 (
        echo [WARN] requirements.txt failed, installing main packages...
        python -c "import PyQt5" 2>nul || python -m pip install PyQt5
        python -c "import websockets" 2>nul || python -m pip install websockets
        python -c "import requests" 2>nul || python -m pip install requests
        python -c "import PIL" 2>nul || python -m pip install Pillow
    )
) else (
    python -c "import PyQt5" 2>nul || python -m pip install PyQt5
    python -c "import websockets" 2>nul || python -m pip install websockets
    python -c "import requests" 2>nul || python -m pip install requests
    python -c "import PIL" 2>nul || python -m pip install Pillow
)

echo.
echo [2/5] Cleaning old build...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist "build.spec" del /q "build.spec"

echo [3/5] Checking resources...
if not exist "fe_fix.txt" echo [WARN] fe_fix.txt not found
if not exist "logo\icon.ico" echo [WARN] logo\icon.ico not found

echo [4/5] Running PyInstaller...
pyinstaller build_lite.spec --clean

if errorlevel 1 (
    echo.
    echo [ERROR] Build failed. Check the output above.
    pause
    exit /b 1
)

echo.
echo [5/5] Done.
echo.
echo ========================================
echo Output: dist\ (see build_lite.spec for exe name)
echo ========================================
echo.
pause
