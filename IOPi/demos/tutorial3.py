#!/usr/bin/env python

"""
================================================
AB Electronics UK IO Pi 32-Channel Port Expander - Tutorial 3 for MicroPython Library

Run using Thonny Python IDE from https://thonny.org/

Create a file in Thonny called IOPI.py, copy contents from IOPI.py 
to the file and save it onto the Raspberry Pi Pico

Create a file named tutorial3.py, copy the code from this file and save
onto the Raspberry Pi Pico

Run with "Run Current Command" or F5 in Thonny

================================================

This tutorial shows how to use interrupts on the IO Pi Plus.
Port 0 on Bus 1 is set as inputs with pull-ups enabled and the pins inverted.
Port 0 on Bus 2 is set as outputs.
When a button is pressed on port 0 on bus 1 an interrupt is triggered.
The interrupt value is read and the value is used to set the output bus 2.

"""
import time
from IOPi import IOPi


def main():
    '''
    Main program function
    '''
    # Create two instances of the IOPi class with
    # I2C addresses of 0x20 and 0x21 with SDA on pin 20 and SCL on pin 21
    busin = IOPi(0x20,20,21)
    busout = IOPi(0x21,20,21)

    # Set port 0 on the busin bus as inputs with internal pull-ups enabled.

    busin.set_port_pullups(0, 0xFF)
    busin.set_port_direction(0, 0xFF)

    # Invert the port so pins will show 1 when grounded
    busin.invert_port(0, 0xFF)

    # Set port 0 on busout as outputs and set the port to be off
    busout.set_port_direction(0, 0x00)
    busout.write_port(0, 0x00)

    # Set the interrupts default value for port 0 to 0x00 so the interrupt
    # will trigger when any pin registers as true
    busin.set_interrupt_defaults(0, 0x00)

    # Set the interrupt type to be 1 on each pin for port 0 so an interrupt is
    # fired when the pin matches the default value
    busin.set_interrupt_type(0, 0xFF)

    # Enable interrupts for all pins on port 0
    busin.set_interrupt_on_port(0, 0xFF)

    # Reset the interrupts
    busin.reset_interrupts()

    while True:

        # read the interrupt status for each port.

        if (busin.read_interrupt_status(0) != 0):
            # If the status is not 0 then an interrupt has occurred
            # on one of the pins so read the value from the interrupt capture
            value = busin.read_interrupt_capture(0)

            # write the value to port 0 on the busout bus
            busout.write_port(0, value)

        # sleep 200ms before checking the pin again
        time.sleep(0.2)

if __name__ == "__main__":
    main()

