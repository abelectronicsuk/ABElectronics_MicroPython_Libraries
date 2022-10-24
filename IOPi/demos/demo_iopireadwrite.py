#!/usr/bin/env python

"""
================================================
ABElectronics IO Pi | Digital I/O Read and Write Demo for MicroMicroPython Library

Run using Thonny Python IDE from https://thonny.org/

Create IOPI.py file and copy contents from  IOPI.py to file and save
onto Raspberry Pi Pico

Create file named demo_iopireadwrite.py and copy code from this file and save
onto Raspberry Pi Pico

Run with "Run Current Command" or F5 in Thonny

================================================

This example reads pin 1 of bus 1 on the IO Pi board and sets
pin 1 of bus 2 to match.
The internal pull-up resistors are enabled so the input pin
will read as 1 unless the pin is connected to ground.

Initialise the IOPi device using the default addresses, you will need to
change the addresses if you have changed the jumpers on the IO Pi

"""
import time
from IOPi import IOPi

def main():
    """
    Main program function
    """

    # create two instances of the IoPi class called iobus1 and iobus2 and set
    # the default i2c addresses
    
    # Create an instance of the IOPi class with an I2C address of 0x20 with SDA on pin 20 and SCL on pin 21
    # bus 1 will be inputs
    iobus1 = IOPi(0x20,20,21)
    # Create an instance of the IOPi class with an I2C address of 0x21 with SDA on pin 20 and SCL on pin 21
    # bus 2 will be outputs
    iobus2 = IOPi(0x21,20,21)
    
    # Each bus is divided up two 8 bit ports.  Port 0 controls pins 1 to 8,
    # Port 1 controls pins 9 to 16.
    # We will read the inputs on pin 1 of bus 1 so set port 0 to be inputs and
    # enable the internal pull-up resistors
    iobus1.set_port_direction(0, 0xFF)
    iobus1.set_port_pullups(0, 0xFF)

    # We will write to the output pin 1 on bus 2 so set port 0 to be outputs
    # and turn off the pins on port 0
    iobus2.set_port_direction(0, 0x00)
    iobus2.write_port(0, 0x00)

    while True:

        # read pin 1 on bus 1.  If pin 1 is high set the output on
        # bus 2 pin 1 to high, otherwise set it to low.
        # connect pin 1 on bus 1 to ground to see the output on
        # bus 2 pin 1 change state.
        if iobus1.read_pin(1) == 1:

            iobus2.write_pin(1, 1)
        else:
            iobus2.write_pin(1, 0)

        # wait 0.1 seconds before reading the pins again
        time.sleep(0.1)

if __name__ == "__main__":
    main()


    

