#!/usr/bin/env python

"""
================================================
AB Electronics UK ADC-DAC Pi 2-Channel ADC, 2-Channel
DAC Speed Demo for MicroMicroPython Library

Run using Thonny Python IDE from https://thonny.org/

Create ADCDACPi.py file and copy contents from  ADCDACPi.py to file and save
onto Raspberry Pi Pico

Create file named demo_dacspeed.py and copy code from this file and save
onto Raspberry Pi Pico

Run with "Run Current Command" or F5 in Thonny

================================================

this demo will output a 3.3V square wave, testing the maximum speed of the DAC
"""

import time

from ADCDACPi import ADCDACPi

def main():
    '''
    Main program function
    '''

    # create an instance of the ADCDAC Pi with a DAC gain set to 2
    adcdac = ADCDACPi(2)

    while True:
        adcdac.set_dac_raw(1, 4095)  # set the voltage on channel 1 to 3.3V
        adcdac.set_dac_raw(1, 0)  # set the voltage on channel 1 to 0V

if __name__ == "__main__":
    main()

