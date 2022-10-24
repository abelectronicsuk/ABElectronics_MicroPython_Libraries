#!/usr/bin/env python
"""
================================================
AB Electronics UK: IO Zero 32 | Tutorial 2 for MicroMicroPython Library

Run using Thonny Python IDE from https://thonny.org/

Create IOZero32.py file and copy contents from  IOZero32.py to file and save
onto Raspberry Pi Pico

Create file named tutorial-1.py and copy code from this file and save
onto Raspberry Pi Pico

Run with "Run Current Command" or F5 in Thonny

================================================

This tutorial uses a button to control an LED.  For the full tutorial visit
https://www.abelectronics.co.uk/kb/article/1100/io-zero-32-tutorial-2---push-the-button

"""

import time
from IOZero32 import IOZero32

# Create iobus1 object on address 0x20 with SDA on pin 20 and SCL on pin 21
bus = IOZero32(0x20, 20, 21)
bus.set_pin_direction(1, 1) # set pin 1 as an input
bus.set_pin_direction(8, 0) # set pin 8 as an output
bus.write_pin(8, 0) # turn off pin 8

while True:
    if bus.read_pin(1) == 1: # check to see if the button is pressed
        print("button pressed") # print a message to the screen
        bus.write_pin(8, 1) # turn on the led on pin 8
        time.sleep(2) # wait 2 seconds
    else:
        bus.write_pin(8, 0) # turn off the led on pin 8
