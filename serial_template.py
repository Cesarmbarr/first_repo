#this is the the first attempt to connect with arduino
#going to connect through serial and send some data to arduino

import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600) # open serial port
print(ser.name)         # check which port was really used

time.sleep(2) # wait for the serial connection to initialize

ser.write(b'Hello Arduino!') # send data to Arduino
ser.close()             # close the serial port

