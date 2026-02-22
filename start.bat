@echo off
echo 🚀 Starting VallamAI Deployment...

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Check if .env file exists
if not exist ".env" (
    echo ⚠️  .env file not found. Please copy .env.example to .env and configure your API key.
    echo    copy .env.example .env
    pause
    exit /b 1
)

REM Start the application
echo 🏁 Starting VallamAI application...
python app.py

pause
