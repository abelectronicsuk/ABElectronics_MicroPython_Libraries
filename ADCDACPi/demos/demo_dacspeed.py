#!/usr/bin/env python

"""
================================================
AB Electronics UK ADC-DAC Pi 2-Channel ADC, 2-Channel
DAC Speed Demo for the MicroPython Library

Run using Thonny Python IDE from https://thonny.org/

Create a file in Thonny called ADCDACPi.py, copy contents from ADCDACPi.py 
to the file and save it onto the Raspberry Pi Pico

Create a file named demo_dacspeed.py, copy the code from this file and save
onto the Raspberry Pi Pico

Run with "Run Current Command" or F5 in Thonny

================================================

This demo will output a 3.3V square wave, testing the maximum speed of the DAC

"""

import time

from ADCDACPi import ADCDACPi

def main():
    '''
    Main program function
    '''

    # create an instance of the ADCDACPi class with a DAC gain set to 2
    adcdac = ADCDACPi(2)

    while True:
        adcdac.set_dac_raw(1, 4095)  # set the voltage on channel 1 to 3.3V
        adcdac.set_dac_raw(1, 0)  # set the voltage on channel 1 to 0V

if __name__ == "__main__":
    main()

