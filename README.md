# Simple steps to flash micropython and deploy WebREPL 🚀

This project simplifies the process for new developers to get started with micropython on **ESP32**, **ESP32-WROOM-32** or **ESP8266** device.

## 🎯 It helps users to:
- Flashing micropython firmware onto the supported device
- Upload custom Python scripts to the device
- Interact with the device using WebREPL for running Python commands remotely

---

## 🧩 Supported Devices
- ESP32  
- ESP32-WROOM-32  
- ESP8266  

---

## 📡 ESP Access Point
- **SSID**: `ESP328266`  
- **Password**: `12345678`  

## 🔐 WebREPL
- **Password**: `1234`  

---

## 🛠️ Installation Steps

### Step 1: Connect Device
Connect your ESP device to your PC via USB.

---

### Step 2: Flash Firmware
#### For ESP32 / ESP32-WROOM-32:

Double Click:  
```step1_ESP32_or ESP32WROOM_firmware_flash.bat```

#### For ESP8266:

Double Click:  
```step1_ESP8266_firmware_flash.bat```

> **💡 Remark:** Please wait until you see 'Press any key to continue', then press any key to close the command prompt.<br>
> **💡 Remark:** Please ignore this if the flashing is functioning correctly. If flashing fails, you may click 'boot' button on ESP device when it shows 'connecting......'.

### Step 3: Upload Python Scripts
Double Click:  
```step2_upload_files.bat```
> **💡 Remark:** You may put your own scripts in 'python_code' folder before clicking 'step2_upload_files.bat'.<br>
> **💡 Remark:** You may also customize ESP Access Point settings in /python_code/boot.py, as well as WebREPL password in /python_code/webrepl_cfg.py, before clicking 'step2_upload_files.bat'.<br>
> **💡 Remark:** Please wait until you see 'Press any key to continue', then press any key to close the command prompt.

### Step 4: Launch WebREPL in Microsoft Edge
Double Click:  
```step3_open_webrepl_Please_connect_WiFi.bat```
> WebREPL will be launched in Microsoft Edge.

### Step 5: Connect your PC's WiFi to ESP access point
> **💡 Remark:** If ESP access point SSID does not appear, please press 'EN' or 'RST' button on ESP device or reconnect ESP device USB cable.

### Step 6: Access to WebREPL
Click 'Connect' on WebREPL in Edge browser. Key in the WebREPL password and press Enter key.
> **💡 Remark:** The password cannot be seen on WebREPL.

### Done
