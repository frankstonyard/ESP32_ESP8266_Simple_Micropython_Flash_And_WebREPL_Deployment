import serial
import os
import sys

com_port = sys.argv[1]
webrepl_path = sys.argv[2]  

# Replace 'COM8' with your serial port
ser = serial.Serial(com_port, 115200, timeout=1)

try:
    while True:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if "192.168." in line:
            print(line.partition("192.168.")[1]+line.partition("192.168.")[2])
            os.system("start msedge " + "file:///"+webrepl_path+"#192.168.4.1:8266")
            break
        else:
            print("please press reset button on ESP board")
finally:
    ser.close()