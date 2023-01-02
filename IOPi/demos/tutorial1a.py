#!/usr/bin/env python

"""
================================================
AB Electronics UK IO Pi 32-Channel Port Expander - Tutorial 1a for MicroPython Library

Run using Thonny Python IDE from https://thonny.org/

Create a file in Thonny called IOPI.py, copy contents from IOPI.py 
to the file and save it onto the Raspberry Pi Pico

Create a file named tutorial1a.py, copy the code from this file and save
onto the Raspberry Pi Pico

Run with "Run Current Command" or F5 in Thonny

================================================

This example uses the write_port method to count in binary using 8 LEDs

"""
import time
from IOPi import IOPi


def main():
    '''
    Main program function
    '''

    # Create an instance of the IOPi class with an I2C address of 0x20 with SDA on pin 20 and SCL on pin 21
    bus = IOPi(0x20,20,21)

    bus.set_port_direction(0, 0x00)
    bus.write_port(0, 0x00)

    while True:
        for count in range(0, 255):
            bus.write_port(0, count)
            time.sleep(0.5)

        bus.write_port(0, 0x00)


if __name__ == "__main__":
    main()

