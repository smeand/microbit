# Microbit
Microbit i grundskolan, idéer och tips. Microbit in primary and secondary school, ideas and tips.
# På svenska
Microbit och blockprogrammering https://makecode.org 

Microbit, micropython  https://microbit-micropython.readthedocs.io/en/latest/ och editorn MU https://codewith.mu/
MU på github https://github.com/mu-editor/mu

# In english
Microbit and programming with blocks https://makecode.org 

Microbit, micropython  https://microbit-micropython.readthedocs.io/en/latest/ and the editor MU https://codewith.mu/
MU on github https://github.com/mu-editor/mu

# Examples
Micropython and python made in MU-editor (1.01)
https://codewith.mu/
Flash the microbit with uart_send.py (only tested with win 10)
In Python-mode start the readuart_turtle.py (tested with win 10)

Tilt the microbit left-right (x) and up-down (y) to steer the turtle. And button A and button B for change pensize.

# Micro:bit motorshield challenge
Livecode your kitronik motorshield robot. you have to have two micro:bits, one connected to your computer and one to the motorshieldrobot.

Commands (livecoding)
radio.send("fw 3 1000")  commandstring to use with the MU-editor REPL and the sending micro:bit
fw = forward
3 = full speed (you can use 1-3, 1 is lower speed and 3 is highest speed)
1000 = drive 1 sec (use milliseconds)

Other commands
bw = backwards
tr = turn right
tl = turn left
br = back turn right
bl = back turn left

"c 1 0.95"
c= calibrate, 1 = left motor full speed, 0.95 = right motor 95% power
Calibration stores in variables only when the micro:bit is powered on
If your motors don´t drive at the exact same speed (low cost motors are not accurate) you can calibrate a little bit.
"auto"
This execute the auto.txt file with commands. auto.txt must be copied to the motorshield-micro:bit

