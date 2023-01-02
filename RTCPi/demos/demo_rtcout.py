#!/usr/bin/env python

"""
================================================
AB Electronics UK RTC Pi | RTC clock output demo for MicroPython Library

Run using Thonny Python IDE from https://thonny.org/

Create a file in Thonny called RTCPi.py, copy contents from RTCPi.py 
to the file and save it onto the Raspberry Pi Pico

Create a file named demo_rtcout.py, copy the code from this file and save
onto the Raspberry Pi Pico

Run with "Run Current Command" or F5 in Thonny

===============================================

This demo shows how to enable the clock square wave output on the
RTC Pi real-time clock and set the frequency


"""
from RTCPi import RTC


def main():
    '''
    Main program function
    '''

    # create a new instance of the RTC class with SDA on pin 20 and SCL on pin 21
    rtc = RTC(20,21)  

    # set the frequency of the output square wave, options are: 
    # 1 = 1Hz, 2 = 4.096KHz, 3 = 8.192KHz, 4 = 32.768KHz
    rtc.set_frequency(3)
    rtc.enable_output()  # enable the square-wave

if __name__ == "__main__":
    main()
