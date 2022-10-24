#!/usr/bin/env python

"""
================================================
AABElectronics ADC Differential Pi 8-Channel ADC Read Raw demo for MicroMicroPython Library

Run using Thonny Python IDE from https://thonny.org/

Create ADCPi.py file and copy contents from  ADCPi.py to file and save
onto Raspberry Pi Pico

Create file named demo_readraw.py and copy code from this file and save
onto Raspberry Pi Pico

Run with "Run Current Command" or F5 in Thonny

================================================

Initialise the ADC device using the default addresses and sample rate,
change this value if you have changed the address selection jumpers
Sample rate can be 12,14, 16 or 18

"""
import time
from ADCDifferentialPi import ADCDifferentialPi

def main():
    '''
    Main program function
    '''
    # I2C addresses of 0x68 and 0x69, bit rate 12 with SDA on pin 20 and SCL on pin 21
    adc = ADCDifferentialPi(0x68, 0x69, 18,20,21)

    while True:

        # read the raw value from adc channels and print to screen
        print("Channel 1: %d" % adc.read_raw(1))
        print("Channel 2: %d" % adc.read_raw(2))
        print("Channel 3: %d" % adc.read_raw(3))
        print("Channel 4: %d" % adc.read_raw(4))
        print("Channel 5: %d" % adc.read_raw(5))
        print("Channel 6: %d" % adc.read_raw(6))
        print("Channel 7: %d" % adc.read_raw(7))
        print("Channel 8: %d" % adc.read_raw(8))

        # wait 0.5 seconds before reading the pins again
        time.sleep(0.5)

if __name__ == "__main__":
    main()

