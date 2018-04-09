# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
# Serial write from microbit
from microbit import *

uart.init(115200)

while True:
    leftRight = accelerometer.get_x()
    upDown = accelerometer.get_y()
    if leftRight > 400:
        display.show(Image.ARROW_E)
        uart.write("R")
    elif leftRight < -400:
        display.show(Image.ARROW_W)
        uart.write("L")
    elif upDown > 400:
        display.show(Image.ARROW_N)
        uart.write("U")
    elif upDown < -400:
        display.show(Image.ARROW_S)
        uart.write("D")
    else:
        display.show(Image.NO)
        if button_a.was_pressed():
            uart.write("+")
        if button_b.was_pressed():
            uart.write("-")
    sleep(50)
    