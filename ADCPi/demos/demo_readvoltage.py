#!/usr/bin/env python

"""
================================================
AB Electronics UK ADC Pi 8-Channel ADC demo for MicroPython Library

Run using Thonny Python IDE from https://thonny.org/

Create a file in Thonny called ADCPi.py, copy contents from ADCPi.py 
to the file and save it onto the Raspberry Pi Pico

Create a file named demo_readvoltage.py, copy the code from this file and save
onto the Raspberry Pi Pico

Run with "Run Current Command" or F5 in Thonny

================================================

Initialise the ADC device using the default addresses and sample rate,
change this value if you have changed the address selection jumpers

The sample rate can be 12, 14, 16 or 18

"""
import time
from ADCPi import ADCPi

def main():
    '''
    Main program function
    '''
    # I2C addresses of 0x68 and 0x69, bit rate 12 with SDA on pin 20 and SCL on pin 21
    adc = ADCPi(0x68, 0x69, 12,20,21)

    while True:

        # read from the ADC channels and print to screen
        print("Channel 1: %02f" % adc.read_voltage(1))
        print("Channel 2: %02f" % adc.read_voltage(2))
        print("Channel 3: %02f" % adc.read_voltage(3))
        print("Channel 4: %02f" % adc.read_voltage(4))
        print("Channel 5: %02f" % adc.read_voltage(5))
        print("Channel 6: %02f" % adc.read_voltage(6))
        print("Channel 7: %02f" % adc.read_voltage(7))
        print("Channel 8: %02f" % adc.read_voltage(8))

        # wait 0.2 seconds before reading the pins again
        time.sleep(0.2)

if __name__ == "__main__":
    main()

