import time
import serial
from serial.tools import list_ports
from serial import tools
import io

#help(serial)

print(serial.tools.list_ports)

ser = serial.Serial()  # open serial port>>> ser = serial.Serial()
#sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
ser.baudrate = 9600
ser.port = 'COM7'
ser.open()
print(ser)

while True:
    if ser.is_open:
        # check which port was really used
        #ser.write(b'b\n')     # write a string
        #time.sleep(1)
        a = ser.read()
        print(a)
        #hello = sio.readline()
        #print(hello)
        #print(s)

