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
echo start web terminal
echo ..........................

python.exe CheckSerial.py %comPort% %batDir%WebREPL\WebREPL.html
