#!/usr/bin/env python

"""
================================================
ABElectronics ADC Pi ACS712 30 Amp current sensor demo for MicroMicroPython Library

Run using Thonny Python IDE from https://thonny.org/

Create ADCPi.py file and copy contents from  ADCPi.py to file and save
onto Raspberry Pi Pico

Create file named demo_acs712_30.py and copy code from this file and save
onto Raspberry Pi Pico

Run with "Run Current Command" or F5 in Thonny

================================================

Initialise the ADC device using the default addresses and sample rate,
change this value if you have changed the address selection jumpers

Sample rate can be 12,14, 16 or 18

"""
import time
from ADCPi import ADCPi


def calc_current(inval):
    '''
    change the 2.5 value to be half of the supply voltage.
    '''
    return ((inval) - 2.5) / 0.066


def main():
    '''
    Main program function
    '''
    # I2C addresses of 0x68 and 0x69, bit rate 12 with SDA on pin 20 and SCL on pin 21
    adc = ADCPi(0x68, 0x69, 12,20,21)

    while True:
        # read from adc channels and print to screen
        print("Current on channel 1: %02f" % calc_current(adc.read_voltage(1)))

        # wait 0.5 seconds before reading the pins again
        time.sleep(0.5)

if __name__ == "__main__":
    main()

