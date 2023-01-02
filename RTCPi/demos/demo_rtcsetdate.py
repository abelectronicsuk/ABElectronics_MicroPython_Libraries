#!/usr/bin/env python

"""
================================================
AB Electronics UK RTC Pi | Set Time Demo for MicroPython Library

Run using Thonny Python IDE from https://thonny.org/

Create a file in Thonny called RTCPi.py, copy contents from RTCPi.py 
to the file and save it onto the Raspberry Pi Pico

Create a file named demo_rtcsetdate.py, copy the code from this file and save
onto the Raspberry Pi Pico

Run with "Run Current Command" or F5 in Thonny

===============================================

This demo shows how to set the time on the RTC Pi real-time clock
and then read the current time at 1-second intervals


"""
from RTCPi import RTC
import time

def main():
    '''
    Main program function
    '''
    # create a new instance of the RTC class with SDA on pin 20 and SCL on pin 21
    rtc = RTC(20,21)  

    # set the date and time to 10th April 2022 at 15:22:00 PM
    # Year, Month, Day, dayofweek, Hour, Minute, Seconds, 0
    now = (2022, 4, 10, 6, 15, 22, 00, 0)


    rtc.set_date(now)

    while True:
        # read the date from the RTC and print it
        print(rtc.read_date())
        time.sleep(1)  # wait 1 second

if __name__ == "__main__":
    main()
