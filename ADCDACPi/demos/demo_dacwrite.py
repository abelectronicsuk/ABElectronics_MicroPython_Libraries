#!/usr/bin/env python

"""
================================================
AB Electronics UK ADC-DAC Pi 2-Channel ADC, 2-Channel DAC 
Write Demo for the MicroPython Library

Run using Thonny Python IDE from https://thonny.org/

Create a file in Thonny called ADCDACPi.py, copy contents from ADCDACPi.py 
to the file and save it onto the Raspberry Pi Pico

Create a file named demo_dacwrite.py, copy the code from this file and save
onto the Raspberry Pi Pico

Run with "Run Current Command" or F5 in Thonny
================================================

This demo will generate a 1.5V p-p square wave at 1Hz
"""

import time

from ADCDACPi import ADCDACPi


def main():
    '''
    Main program function
    '''

    # create an instance of the ADCDACPi class with a DAC gain set to 1
    adcdac = ADCDACPi(1)

    while True:
        adcdac.set_dac_voltage(1, 1.5)  # set the voltage on channel 1 to 1.5V
        time.sleep(0.5)  # wait 0.5 seconds
        adcdac.set_dac_voltage(1, 0)  # set the voltage on channel 1 to 0V
        time.sleep(0.5)  # wait 0.5 seconds

if __name__ == "__main__":
    main()

