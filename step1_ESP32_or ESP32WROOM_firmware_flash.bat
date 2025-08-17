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

echo ................
echo erasing nodemcu
echo ................
python.exe esptool.py -p %comPort% -b 115200 erase_flash

echo ...............................
echo uploading micropython firmware
echo ...............................
python esptool.py -p %comPort% -c esp32 --baud 460800 write_flash 0x1000 %batDir%ESP32_firmware\ESP32_GENERIC_20250415_v1.25.0.bin

pause