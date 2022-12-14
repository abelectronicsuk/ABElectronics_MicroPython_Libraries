#!/usr/bin/env python
"""
================================================
AB Electronics UK: IO Zero 32 | Tutorial 1 for MicroPython Library

Run using Thonny Python IDE from https://thonny.org/

Create a file in Thonny called IOZero32.py, copy contents from IOZero32.py 
to the file and save it onto the Raspberry Pi Pico

Create a file named tutorial1.py, copy the code from this file and save
onto the Raspberry Pi Pico

Run with "Run Current Command" or F5 in Thonny

================================================

This tutorial flashes an LED connected to bus 1.  For the full tutorial visit
https://www.abelectronics.co.uk/kb/article/1099/io-zero-32-tutorial-1---the-blinking-led

"""

import time
from IOZero32 import IOZero32

# Create iobus1 object on address 0x20 with SDA on pin 20 and SCL on pin 21
bus = IOZero32(0x20, 20, 21)
bus.set_port_direction(0, 0x00)
bus.write_port(0, 0x00)
while True:
    bus.write_pin(1, 1)
    time.sleep(1)
    bus.write_pin(1, 0)
    time.sleep(1)

