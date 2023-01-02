#!/usr/bin/env python
"""
================================================
AB Electronics UK: IO Zero 32 | Digital I/O Read Demo for MicroPython Library

Run using Thonny Python IDE from https://thonny.org/

Create a file in Thonny called IOZero32.py, copy contents from IOZero32.py 
to the file and save it onto the Raspberry Pi Pico

Create a file named demo_ioread.py, copy the code from this file and save
onto the Raspberry Pi Pico

Run with "Run Current Command" or F5 in Thonny

================================================

This example reads from all 32 pins across both buses on the IO Zero 32.
The pull-up or pull-down resistors may be needed on the inputs to stop them
from floating in an indeterminate state.

"""

import time
from IOZero32 import IOZero32


def main():
    """
    Main program function
    """
    # Create iobus1 object on address 0x20 with SDA on pin 20 and SCL on pin 21
    iobus1 = IOZero32(0x20, 20, 21)
    # Create iobus2 object on address 0x21 with SDA on pin 20 and SCL on pin 21
    iobus2 = IOZero32(0x21, 20, 21)

    # We will read all inputs 1 to 16 from the I/O bus so 
    # set the inputs using the set_bus_direction method.
    iobus1.set_bus_direction(0xFFFF)

    # Repeat the steps above for the second bus
    iobus2.set_bus_direction(0xFFFF)

    while True:
        # read the pins 1 to 16 on both buses and print the results
        print("Bus 1                   Bus 2")
        print("Pin 1:  " + str(iobus1.read_pin(1)) +
              "               Pin 1:  " + str(iobus2.read_pin(1)))
        print("Pin 2:  " + str(iobus1.read_pin(2)) +
              "               Pin 2:  " + str(iobus2.read_pin(2)))
        print("Pin 3:  " + str(iobus1.read_pin(3)) +
              "               Pin 3:  " + str(iobus2.read_pin(3)))
        print("Pin 4:  " + str(iobus1.read_pin(4)) +
              "               Pin 4:  " + str(iobus2.read_pin(4)))
        print("Pin 5:  " + str(iobus1.read_pin(5)) +
              "               Pin 5:  " + str(iobus2.read_pin(5)))
        print("Pin 6:  " + str(iobus1.read_pin(6)) +
              "               Pin 6:  " + str(iobus2.read_pin(6)))
        print("Pin 7:  " + str(iobus1.read_pin(7)) +
              "               Pin 7:  " + str(iobus2.read_pin(7)))
        print("Pin 8:  " + str(iobus1.read_pin(8)) +
              "               Pin 8:  " + str(iobus2.read_pin(8)))
        print("Pin 9:  " + str(iobus1.read_pin(9)) +
              "               Pin 9:  " + str(iobus2.read_pin(9)))
        print("Pin 10: " + str(iobus1.read_pin(10)) +
              "               Pin 10: " + str(iobus2.read_pin(10)))
        print("Pin 11: " + str(iobus1.read_pin(11)) +
              "               Pin 11: " + str(iobus2.read_pin(11)))
        print("Pin 12: " + str(iobus1.read_pin(12)) +
              "               Pin 12: " + str(iobus2.read_pin(12)))
        print("Pin 13: " + str(iobus1.read_pin(13)) +
              "               Pin 13: " + str(iobus2.read_pin(13)))
        print("Pin 14: " + str(iobus1.read_pin(14)) +
              "               Pin 14: " + str(iobus2.read_pin(14)))
        print("Pin 15: " + str(iobus1.read_pin(15)) +
              "               Pin 15: " + str(iobus2.read_pin(15)))
        print("Pin 16: " + str(iobus1.read_pin(16)) +
              "               Pin 16: " + str(iobus2.read_pin(16)))

        # wait 0.5 seconds before reading the pins again
        time.sleep(0.5)


if __name__ == "__main__":
    main()

