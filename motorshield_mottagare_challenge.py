from microbit import *
import radio

radio.on()
radio.config(group=1) 	# samma grupp som sändaren
calL = 1		# 2 st globala variabler för kalibrering av motorerna
calR = 1

def wait():		# skapa en funktion som visar att mottagaren väntar på kommando
    display.clear()
    for x in range(1, 4):
        display.set_pixel(x, 2, 9)
        sleep(100)
        display.set_pixel(x, 2, 0)
    
def calibr(MotorL, MotorR):
        p0, p8, p12, p16 = 0, 0, 1023, 1023
        pin0.write_digital(p0)
        pin8.write_digital(p8)
        pin12.write_analog(p12*MotorL)
        pin16.write_analog(p16*MotorR)
        display.show(Image.DIAMOND)
        sleep(4000)
        pin12.write_digital(0)
        pin16.write_digital(0)

def drive(cmd, speed, duration):
    if speed.lower() == "3":
        power = 1023
    elif speed.lower() == "2":
        power = 800
    elif speed.lower() == "1":
        power = 700
    else:
        display.show(Image.NO)
        power = 1023
    if cmd.lower() == "fw":
        p0, p8, p12, p16 = 0, 0, power*calL, power*calR
        display.show(Image.ARROW_N)
    elif cmd.lower() == "bw":
        p0, p8, p12, p16 = power*calL, power*calR,  0, 0
        display.show(Image.ARROW_S)
    elif cmd.lower() == "tl":
        p0, p8, p12, p16 = 0, 0, power*calL, 0
        display.show(Image.ARROW_W)
    elif cmd.lower() == "tr":
        p0, p8, p12, p16 = 0, 0, 0, power*calR
        display.show(Image.ARROW_E)
    elif cmd.lower() == "bl":
        p0, p8, p12, p16 = 0, power*calL, 0, 0
        display.show(Image.ARROW_SW)
    elif cmd.lower() == "br":
        p0, p8, p12, p16 = power*calR, 0, 0, 0
        display.show(Image.ARROW_SE)
    else:
        p0, p8, p12, p16 = 0, 0, 0, 0
        duration = "0"
        display.show(Image.NO)
    pin0.write_analog(p0)
    pin8.write_analog(p8)
    pin12.write_analog(p12)
    pin16.write_analog(p16)
    sleep(int(duration))
    pin0.write_digital(0)
    pin8.write_digital(0)
    pin12.write_digital(0)
    pin16.write_digital(0)

def read_file():
    with open("auto.txt", "r") as start:
        readfile = start.read()
        readfile = readfile.split(";")
        start.close()
    for i in range(0, len(readfile)-1):
        cmd = readfile[i]   
        cmd = cmd.split(" ")
        drive(cmd[0], cmd[1], cmd[2])

while True:
    command = radio.receive()
    if command is None:
        wait()
    else:
        command = command.strip()
        command = command.split(" ")
        if command[0].lower() == "c": 
            calL = float(command[1])
            calR = float(command[2])
            calibr(calL, calR)
        elif command[0].lower() == "auto":
            read_file()
        else:
            drive(command[0], command[1], command[2])