@echo off
REM Simple installer: uses python from PATH to install packages from file named "req"

echo Installing requirements from "%~dp0req" ...
python -m pip install --upgrade pip
python -m pip install -r "%~dp0req.txt"

if %errorlevel% neq 0 (
    echo.
    echo Installation failed. If you used a "req.txt" file instead of "req", try running install_from_req_txt.bat.
    pause
) else (
    echo.
    echo All done!
    pause
)
