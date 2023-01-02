#!/usr/bin/env python

"""
================================================
ABElectronics ADC Pi TMP36 temperature sensor demo for MicroPython Library

Run using Thonny Python IDE from https://thonny.org/

Create a file in Thonny called ADCPi.py, copy contents from ADCPi.py 
to the file and save it onto the Raspberry Pi Pico

Create a file named demo_tmp36.py, copy the code from this file and save
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

        # Calculate the temperature
        # TMP36 returns 0.01 volts per C - -40C to +125C
        # 750mV = 25C and 500mV = 0C.  The temperature is (voltage / 0.01) - 50

        temperature = (adc.read_voltage(1)/0.01)-50

        # read from the ADC channels and print to screen
        print("Temperature on channel 1: %0.02f°C" % temperature)

        # wait 0.5 seconds before reading the pins again
        time.sleep(0.5)

if __name__ == "__main__":
    main()

