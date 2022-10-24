#!/usr/bin/env python

"""
================================================
AB Electronics UK ADC-DAC Pi 2-Channel ADC, 2-Channel DAC 
Write Demo for MicroMicroPython Library

Run using Thonny Python IDE from https://thonny.org/

Create ADCDACPi.py file and copy contents from  ADCDACPi.py to file and save
onto Raspberry Pi Pico

Create file named demo_dacwrite.py and copy code from this file and save
onto Raspberry Pi Pico

Run with "Run Current Command" or F5 in Thonny
================================================

this demo will generate a 1.5V p-p square wave at 1Hz
"""

import time

from ADCDACPi import ADCDACPi


def main():
    '''
    Main program function
    '''

    # create an instance of the ADCDAC Pi with a DAC gain set to 1
    adcdac = ADCDACPi(1)

    while True:
        adcdac.set_dac_voltage(1, 1.5)  # set the voltage on channel 1 to 1.5V
        time.sleep(0.5)  # wait 0.5 seconds
        adcdac.set_dac_voltage(1, 0)  # set the voltage on channel 1 to 0V
        time.sleep(0.5)  # wait 0.5 seconds

if __name__ == "__main__":
    main()

