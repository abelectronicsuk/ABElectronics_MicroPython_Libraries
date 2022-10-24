#!/usr/bin/env python

"""
================================================
ABElectronics IO Pi 32-Channel Port Expander - Tutorial 2 for MicroMicroPython Library

Run using Thonny Python IDE from https://thonny.org/

Create IOPI.py file and copy contents from  IOPI.py to file and save
onto Raspberry Pi Pico

Create file named tutorial2.py and copy code from this file and save
onto Raspberry Pi Pico

Run with "Run Current Command" or F5 in Thonny

================================================

This example uses the write_pin and write_port methods to switch pin 1 on
and off on the IO Pi.

"""
import time
from IOPi import IOPi


def main():
    '''
    Main program function
    '''

    # Create an instance of the IOPi class with an I2C address of 0x20 with SDA on pin 20 and SCL on pin 21
    bus = IOPi(0x20,20,21)

    bus.set_pin_direction(1, 1)  # set pin 1 as an input

    bus.set_pin_direction(8, 0)  # set pin 8 as an output

    bus.write_pin(8, 0)  # turn off pin 8

    bus.set_pin_pullup(1, 1)  # enable the internal pull-up resistor on pin 1

    bus.invert_pin(1, 1)  # invert pin 1 so a button press will register as 1

    while True:

        if bus.read_pin(1) == 1:  # check to see if the button is pressed
            print('button pressed')  # print a message to the screen
            bus.write_pin(8, 1)  # turn on the led on pin 8
            time.sleep(2)  # wait 2 seconds
        else:
            bus.write_pin(8, 0)  # turn off the led on pin 8

if __name__ == "__main__":
    main()

