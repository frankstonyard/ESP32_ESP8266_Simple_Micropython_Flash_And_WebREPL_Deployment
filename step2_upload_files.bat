@echo off
setlocal enabledelayedexpansion

set "batDir=%~dp0"
set "currentDir=%batDir%software
cd /d "%currentDir%"
echo Now in: %cd%

set "comPort="
for /f "tokens=4 delims= " %%A in ('mode ^| findstr "COM"') do (
    set "comPort=%%~nA"
    set "comPort=!comPort::=!"
)
echo COM Port: %comPort%

echo ..........................
echo uploading user code files
echo ..........................

for /r "%batDir%python_code\" %%f in (*) do (
    echo %%f
    python.exe micropython_send.py --baud 115200 --port %comPort% --file %%f
)

pause