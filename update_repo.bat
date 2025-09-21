@echo off
echo ============================
echo   Updating Git Repository
echo ============================

REM Navigate to repo folder
cd /d "C:\Users\Ani\Desktop\Ajay Bharatiya\Counter-Drone-IQ-Data-Detection"

git status

echo.
echo Staging all changes...
git add .

echo.
set /p msg="Enter commit message: "
git commit -m "%msg%"

echo.
echo Pushing to GitHub...
git push

echo.
echo Done!
pause
