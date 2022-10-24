#!/usr/bin/env python

"""
================================================
ABElectronics IO Pi Zero | Digital I/O Read Demo for MicroMicroPython Library

Run using Thonny Python IDE from https://thonny.org/

Create IOPI.py file and copy contents from  IOPI.py to file and save
onto Raspberry Pi Pico

Create file named demo_ioreadzero.py and copy code from this file and save
onto Raspberry Pi Pico

Run with "Run Current Command" or F5 in Thonny

================================================

This example reads from all 16 pins on the IO Pi Zero.
The internal pull-up resistors are enabled so each pin will read
as 1 unless the pin is connected to ground.

"""
import time
from IOPi import IOPi

def main():
    """
    # Create an instance of the IOPi class with an I2C address of 0x20 with SDA on pin 20 and SCL on pin 21
    """
    iobus1 = IOPi(0x20,20,21)

    # We will read the inputs 1 to 16 from the I/O bus so set port 0 and
    # port 1 to be inputs and enable the internal pull-up resistors
    iobus1.set_port_direction(0, 0xFF)
    iobus1.set_port_pullups(0, 0xFF)

    iobus1.set_port_direction(1, 0xFF)
    iobus1.set_port_pullups(1, 0xFF)

    while True:
        # read the pins 1 to 16 and print the results
        print("Pin 1:  " + str(iobus1.read_pin(1)))
        print("Pin 2:  " + str(iobus1.read_pin(2)))
        print("Pin 3:  " + str(iobus1.read_pin(3)))
        print("Pin 4:  " + str(iobus1.read_pin(4)))
        print("Pin 5:  " + str(iobus1.read_pin(5)))
        print("Pin 6:  " + str(iobus1.read_pin(6)))
        print("Pin 7:  " + str(iobus1.read_pin(7)))
        print("Pin 8:  " + str(iobus1.read_pin(8)))
        print("Pin 9:  " + str(iobus1.read_pin(9)))
        print("Pin 10: " + str(iobus1.read_pin(10)))
        print("Pin 11: " + str(iobus1.read_pin(11)))
        print("Pin 12: " + str(iobus1.read_pin(12)))
        print("Pin 13: " + str(iobus1.read_pin(13)))
        print("Pin 14: " + str(iobus1.read_pin(14)))
        print("Pin 15: " + str(iobus1.read_pin(15)))
        print("Pin 16: " + str(iobus1.read_pin(16)))

        # wait 0.5 seconds before reading the pins again
        time.sleep(0.1)


if __name__ == "__main__":
    main()

    

