#!/usr/bin/env python

"""
================================================
ABElectronics IO Pi 32-Channel Port Expander - Tutorial 1 for MicroMicroPython Library

Run using Thonny Python IDE from https://thonny.org/

Create IOPI.py file and copy contents from  IOPI.py to file and save
onto Raspberry Pi Pico

Create file named tutorial1.py and copy code from this file and save
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

    bus.set_port_direction(0, 0x00)
    bus.write_port(0, 0x00)

    while True:
        bus.write_pin(1, 1)
        time.sleep(1)
        bus.write_pin(1, 0)
        time.sleep(1)


if __name__ == "__main__":
    main()

