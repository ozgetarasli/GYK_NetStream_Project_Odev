@echo off
echo Starting Netflix Recommendation System...

REM Install required packages
pip install fastapi uvicorn numpy scikit-learn requests pydantic

REM Start the backend server
start cmd /k "cd /d %~dp0 && python -m uvicorn api.main:app --reload --host 127.0.0.1 --port 8000"

REM Give the backend some time to start
timeout /t 5

REM Start the frontend server
start cmd /k "cd /d %~dp0\frontend && npm start"

echo Started both servers. Press Ctrl+C in respective windows to stop them.
echo Access the API at http://localhost:8000
echo Access the frontend at http://localhost:3000 