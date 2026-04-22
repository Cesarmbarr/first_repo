# This script allows you to send commands to an Arduino over serial.
# this is for servo_serial.ino
import serial
import time

# Change this to your Arduino port
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

time.sleep(2)  # wait for Arduino to reset

while True:
    command = input("Enter command (move / other): ")

    ser.write((command + '\n').encode())  # send command

    time.sleep(0.1)

    # read response from Arduino (optional)
    if ser.in_waiting > 0:
        response = ser.readline().decode().strip()
        print("Arduino:", response)