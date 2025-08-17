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
python esptool.py -p %comPort% -c esp8266 -b 115200 write_flash --flash_size=detect 0 %batDir%ESP32_firmware\ESP8266_GENERIC-20250809-v1.26.0.bin

pause