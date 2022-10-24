#!/usr/bin/env python

"""
================================================
AB Electronics UK ADC-DAC Pi 2-Channel ADC, 2-Channel
DAC | ADC Read Demo for MicroMicroPython Library

Run using Thonny Python IDE from https://thonny.org/

Create ADCDACPi.py file and copy contents from  ADCDACPi.py to file and save
onto Raspberry Pi Pico

Create file named demo_adcread.py and copy code from this file and save
onto Raspberry Pi Pico

Run with "Run Current Command" or F5 in Thonny

================================================

this demo reads the voltage from channel 1 on the ADC inputs
"""

import time

from ADCDACPi import ADCDACPi

def main():
    '''
    Main program function
    '''

    # create an instance of the ADCDAC Pi with a DAC gain set to 1
    adcdac = ADCDACPi(1)

    # set the reference voltage.  this should be set to the exact voltage
    # measured on the raspberry pi 3.3V rail.
    adcdac.set_adc_refvoltage(3.3)

    while True:
        # read the voltage from channel 1 in single ended mode
        # and display on the screen

        print(adcdac.read_adc_voltage(1, 0))

        time.sleep(0.1)

if __name__ == "__main__":
    main()

