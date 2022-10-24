#!/usr/bin/env python

"""
================================================
ABElectronics RTC Pi | RTC memory double demo for MicroMicroPython Library

Run using Thonny Python IDE from https://thonny.org/

Create RTCPi.py file and copy contents from  RTCPi.py to file and save
onto Raspberry Pi Pico

Create file named demo_rtcmemory_double.py and copy code from this file and save
onto Raspberry Pi Pico

Run with "Run Current Command" or F5 in Thonny

===============================================

This demo shows how to write to and read from the internal battery
backed memory on the DS1307 RTC chip


"""
import struct
from RTCPi import RTC


def double_to_array(val):
    '''
    convert a double into an eight byte array
    '''
    buf = bytearray(struct.pack('d', val))
    arraybytes = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 8):
        arraybytes[i] = buf[i]
    return arraybytes


def array_to_double(val):
    '''
    convert an eight byte array into a double
    '''
    dval, = struct.unpack('d', bytearray(val))
    return dval


def main():
    '''
    Main program function
    '''

    # create a new instance of the RTC class with SDA on pin 20 and SCL on pin 21
    rtc = RTC(20,21)  

    # number to be written to the RTC memory
    value = 0.0005
    print("Writing to memory: ", value)

    # convert the number into an array of bytes
    writearray = double_to_array(value)

    # write the array to the RTC memory
    rtc.write_memory(0x08, writearray)

    # read eight bytes from the RTC memory into an array
    read_array = rtc.read_memory(0x08, 8)

    # combine the array values into an number and print it
    print("Reading from memory: ", array_to_double(read_array))

if __name__ == "__main__":
    main()

