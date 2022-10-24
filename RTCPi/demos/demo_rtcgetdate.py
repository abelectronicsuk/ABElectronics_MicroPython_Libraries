#!/usr/bin/env python

"""
================================================
ABElectronics RTC Pi | Get Time Demo for MicroMicroPython Library

Run using Thonny Python IDE from https://thonny.org/

Create RTCPi.py file and copy contents from  RTCPi.py to file and save
onto Raspberry Pi Pico

Create file named demo_rtcgetdate.py and copy code from this file and save
onto Raspberry Pi Pico

Run with "Run Current Command" or F5 in Thonny

===============================================

This demo shows how to read the current time on the 
RTC Pi real-time clock at 1 second intervals
"""
import time

from RTCPi import RTC


def main():
    '''
    Main program function
    '''
    # create a new instance of the RTC class with SDA on pin 20 and SCL on pin 21
    rtc = RTC(20,21)  

    while True:
        # read the date from the RTC and print it
        print(rtc.read_date())
        time.sleep(1)  # wait 1 second

if __name__ == "__main__":
    main()

