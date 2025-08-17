#Python version 3.6.2
import serial
import time
import argparse

parser = argparse.ArgumentParser(description="Run serial connection")
parser.add_argument('--baud', type=int, help="Set the baud rate")
parser.add_argument('--port', type=str, help="Set the COM port")
parser.add_argument('--file', type=str, help="Set the filename")
args = parser.parse_args()
path = args.file
ser = serial.Serial(args.port, args.baud)
ser.timeout = 1
t0 = time.time()

while True:
    data = ser.readline()
    if '>>>' in str(data):
        break
    elif time.time() - t0 > 2:
        ser.write(chr(3).encode())
        break
    else:
        datastr = data.decode().strip()
        #print(datastr)

print("start sending file data.....")

if ':\\' in path:
    head, sep, tail = path.rpartition('\\')
    filename = tail 
else:
    filename = path
print('filename :'+filename)

ser.write(b"fw = open('"+filename.encode("utf-8")+b"', 'w')\r\n")
with open(path, 'r') as f:
    total_lines = sum(1 for line in f)
    
    # Rewind the file pointer to the beginning
    f.seek(0)
    
    for line_number, line in enumerate(f, start=1):
        line = line.rstrip('\r\n')
        line = line.replace('\\r', '\\\\r').replace('\\n', '\\\\n')
        line = line.replace('\"', '\\\"')
        ser.write(b"fw.write(\""+line.encode('utf-8')+b"\\r\\n\")\r\n")
        print("sending.....     ")
        print("sending.....     "+str(line_number)+"/"+str(total_lines))
        time.sleep(0.001)
ser.write(b"fw.close()\r\n")
ser.write(b"print('all data sent')\r\n")

while True:
    data = ser.readline()
    if 'all data sent' in str(data):
        print("all file data is sent.")
        break
    else:
        datastr = data.decode().strip()