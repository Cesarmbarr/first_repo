# This script sends serial commands from the Pi to the ESP32

import serial
import time

# Change if your port is different
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

time.sleep(2)  # wait for ESP32 reset

while True:

    angle = input("Enter servo angle (0-180): ")

    ser.write((angle + '\n').encode())

    time.sleep(0.1)

    if ser.in_waiting > 0:
        response = ser.readline().decode().strip()
        print("ESP32:", response)