#!/usr/bin/env python

"""
================================================
ABElectronics IO Pi | Digital I/O Write Demo for MicroMicroPython Library

Run using Thonny Python IDE from https://thonny.org/

Create IOPI.py file and copy contents from  IOPI.py to file and save
onto Raspberry Pi Pico

Create file named demo_iowrite.py and copy code from this file and save
onto Raspberry Pi Pico

Run with "Run Current Command" or F5 in Thonny

================================================

This example uses the write_pin and write_port methods to switch the pins
on and off on the I/O bus.

"""
import time
from IOPi import IOPi

def main():
    '''
    Main program function
    '''

    # Create an instance of the IOPi class with an I2C address of 0x20 with SDA on pin 20 and SCL on pin 21
    iobus = IOPi(0x20,20,21)

    # We will write to the pins 9 to 16 so set port 1 to be outputs turn off
    # the pins
    iobus.set_port_direction(1, 0x00)
    iobus.write_port(1, 0x00)

    while True:

        # count to 255 and display the value on pins 9 to 16 in binary format
        for val in range(0, 255):
            time.sleep(0.05)
            iobus.write_port(1, val)

        # turn off all of the pins on bank 1
        iobus.write_port(1, 0x00)

        # now turn on all of the leds in turn by writing to one pin at a time
        iobus.write_pin(9, 1)
        time.sleep(0.1)
        iobus.write_pin(10, 1)
        time.sleep(0.1)
        iobus.write_pin(11, 1)
        time.sleep(0.1)
        iobus.write_pin(12, 1)
        time.sleep(0.1)
        iobus.write_pin(13, 1)
        time.sleep(0.1)
        iobus.write_pin(14, 1)
        time.sleep(0.1)
        iobus.write_pin(15, 1)
        time.sleep(0.1)
        iobus.write_pin(16, 1)

        # and turn off all of the leds in turn by writing to one pin at a time
        iobus.write_pin(9, 0)
        time.sleep(0.1)
        iobus.write_pin(10, 0)
        time.sleep(0.1)
        iobus.write_pin(11, 0)
        time.sleep(0.1)
        iobus.write_pin(12, 0)
        time.sleep(0.1)
        iobus.write_pin(13, 0)
        time.sleep(0.1)
        iobus.write_pin(14, 0)
        time.sleep(0.1)
        iobus.write_pin(15, 0)
        time.sleep(0.1)
        iobus.write_pin(16, 0)

        # repeat until the program ends

if __name__ == "__main__":
    main()

