#!/usr/bin/env python

"""
================================================
ABElectronics RTC Pi | Set Time Demo for MicroMicroPython Library

Run using Thonny Python IDE from https://thonny.org/

Create RTCPi.py file and copy contents from  RTCPi.py to file and save
onto Raspberry Pi Pico

Create file named demo_rtcsetdate.py and copy code from this file and save
onto Raspberry Pi Pico

Run with "Run Current Command" or F5 in Thonny

===============================================

This demo shows how to set the time on the RTC Pi real-time clock
and then read the current time at 1 second intervals


"""
from RTCPi import RTC
import time

def main():
    '''
    Main program function
    '''
    # create a new instance of the RTC class with SDA on pin 20 and SCL on pin 21
    rtc = RTC(20,21)  

    # set the datetime 10th April 2022 at 15:22:00 PM
    # Year, Month, Day, dayofweek, Hour, Minute, Seconds, 0
    now = (2022, 4, 10, 6, 15, 22, 00, 0)


    rtc.set_date(now)

    while True:
        # read the date from the RTC in and print it
        print(rtc.read_date())
        time.sleep(1)  # wait 1 second

if __name__ == "__main__":
    main()
