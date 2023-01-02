#!/usr/bin/env python

"""
================================================
AB Electronics UK RTC Pi | RTC memory double demo for MicroPython Library

Run using Thonny Python IDE from https://thonny.org/

Create a file in Thonny called RTCPi.py, copy contents from RTCPi.py 
to the file and save it onto the Raspberry Pi Pico

Create a file named demo_rtcmemory_int.py, copy the code from this file and save
onto the Raspberry Pi Pico

Run with "Run Current Command" or F5 in Thonny

===============================================

This demo shows how to write to and read from the internal battery
backed memory on the DS1307 RTC chip


"""
from RTCPi import RTC
import struct
def int_to_array(val):
    '''
    convert an integer into a four-byte array
    '''
    arraybytes = [0, 0, 0, 0]
    arraybytes[3] = val & 0xFF
    val >>= 8
    arraybytes[2] = val & 0xFF
    val >>= 8
    arraybytes[1] = val & 0xFF
    val >>= 8
    arraybytes[0] = val & 0xFF
    return arraybytes


def array_to_int(arraybytes):
    '''
    convert a four-byte array into an integer
    '''
    val = (arraybytes[0] << 24) + (arraybytes[1] << 16) + \
          (arraybytes[2] << 8) + arraybytes[3]
    return val


def main():
    '''
    Main program function
    '''

    # create a new instance of the RTC class with SDA on pin 20 and SCL on pin 21
    rtc = RTC(20,21)  

    # integer to be written to the RTC memory
    writeval = 176247
    print("Writing to memory: ", writeval)

    # convert the integer into an array of bytes
    writearray = int_to_array(writeval)

    # write the array to the RTC memory
    rtc.write_memory(0x08, writearray)

    # read four bytes from the RTC memory into an array
    readarray = rtc.read_memory(0x08, 4)

    # combine the array values into an integer and print it
    print("Reading from memory: ", array_to_int(readarray))

if __name__ == "__main__":
    main()

