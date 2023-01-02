#!/usr/bin/env python

"""
================================================
AB Electronics UK ADC Pi HIH4000 humidity sensor demo for MicroPython Library

Run using Thonny Python IDE from https://thonny.org/

Create a file in Thonny called ADCPi.py, copy contents from ADCPi.py 
to the file and save it onto the Raspberry Pi Pico

Create a file named demo_hih4000.py, copy the code from this file and save
onto the Raspberry Pi Pico

Run with "Run Current Command" or F5 in Thonny

================================================

The HIH4000 humidity sensor needs a load of at least 80K between the output
and ground pin so add a 100K resistor between the sensor output and the
ADC Pi input pin to make the sensor work correctly

Initialise the ADC device using the default addresses and sample rate,
change this value if you have changed the address selection jumpers

The sample rate can be 12, 14, 16 or 18

"""
import time
from ADCPi import ADCPi

RESISTOR_MULTIPLIER = 6.95225  # use 100K resistor in series with the input
ZERO_OFFSET = 0.826  # zero offset value from calibration data printout
SLOPE = 0.031483  # slope value from calibration data printout


def calc_humidity(inval):
    '''
    Calculate the humidity
    '''
    voltage = inval * RESISTOR_MULTIPLIER
    humidity = (voltage - ZERO_OFFSET) / SLOPE
    return humidity



def main():
    '''
    Main program function
    '''
    # I2C addresses of 0x68 and 0x69, bit rate 12 with SDA on pin 20 and SCL on pin 21
    adc = ADCPi(0x68, 0x69, 12,20,21)

    while True:

        # read from the ADC channels and print to screen
        print("Humidity on channel 1: %0.1f%%" %
              calc_humidity(adc.read_voltage(1)))

        # wait 0.5 seconds before reading the pins again
        time.sleep(0.5)

if __name__ == "__main__":
    main()

