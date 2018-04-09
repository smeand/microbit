# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
#Turtle moves serial communication microbit
import serial
import turtle
from serial.tools import list_ports
psize = 1

#This works on a win 10 and no other devices connected
port = [port.device for port in serial.tools.list_ports.comports()]
if port:
    print("Microbit connected " + str(port))
    s = serial.Serial(port[0], 115200, timeout=0.5)
    t = turtle.Turtle()
else:
    print("No microbit connected")

while port:    
    r = s.read()            # Read the serial communication
    r = r.decode('utf-8')   # Decode the received byte
    if r == "L":            # Do something depending on received char
        t.left(10)
    elif r == "R":
        t.right(10)
    elif r == "U":
        t.forward(10)
    elif r == "D":
        t.backward(10)
    elif r == "+":
        psize += 1
    elif r == "-":
        if psize > 1:
            psize -= 1
    t.pensize(psize)