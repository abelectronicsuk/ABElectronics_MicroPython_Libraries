#!/usr/bin/env python
"""
================================================
AB Electronics UK: RTC Pi Real-time clock

Raspberry Pi Pico MicroPython Library
================================================
"""
import machine
import re


class RTC:
    """
    Based on the Maxim DS1307
    """

    # define registers from the datasheet
    SECONDS = 0x00
    MINUTES = 0x01
    HOURS = 0x02
    DAYOFWEEK = 0x03
    DAY = 0x04
    MONTH = 0x05
    YEAR = 0x06
    CONTROL = 0x07

    # variables
    __rtcaddress = 0x68  # I2C address
    # initial configuration - square wave and output disabled, frequency set
    # to 32.768KHz.
    __rtcconfig = 0x03
    # the DS1307 does not store the current century so that has to be added on
    # manually.
    __century = 2000

    __weekday_start = 1
    
    __bus = None

    # local methods

    @staticmethod
    def __updatebyte(byte, bit, value):
        """
        Internal method for setting the value of a single bit within a byte

        :param byte: input value
        :type byte: int
        :param bit: location to update
        :type bit: int
        :param value: new bit, 0 or 1
        :type value: int
        :return: updated value
        :rtype: int
        """

        if value == 0:
            return byte & ~(1 << bit)
        elif value == 1:
            return byte | (1 << bit)

    @staticmethod
    def __bcd_dec(bcd):
        """
        Internal method for converting BCD format number to decimal

        :param bcd: BCD formatted number
        :type bcd: int
        :return: decimal number
        :rtype: int
        """
        return bcd - 6 * (bcd >> 4)

    @staticmethod
    def __dec_bcd(dec):
        """
        Internal method for converting a decimal formatted number to BCD

        :param dec: decimal number
        :type dec: int
        :return: BCD formatted number
        :rtype: int
        """
        bcd = 0
        for vala in (dec // 10, dec % 10):
            for valb in (8, 4, 2, 1):
                if vala >= valb:
                    bcd += 1
                    vala -= valb
                bcd <<= 1
        return bcd >> 1

    
    # public methods

    def __init__(self, sda=None, scl=None):
        """
        Initialise the RTC module
        :param address: sda pin
        :type address: int
        :param address: scl pin
        :type address: int
        """
        if sda == None or sda < 0 or sda > 40:           
            sdaPIN=machine.Pin(20)
        else:
            sdaPIN=machine.Pin(sda)
            
        if scl == None or scl < 0 or scl > 40:           
            sclPIN=machine.Pin(21)
        else:
            sclPIN=machine.Pin(scl)

        self.__bus = machine.I2C(0,sda=sdaPIN, scl=sclPIN, freq=100000)
        self.__bus.writeto_mem(self.__rtcaddress, self.CONTROL,bytearray(self.__rtcconfig))
        
        return

    def set_date(self, date):
        """
        Set the date and time on the RTC

        :param date:  Year, Month, Day, dayofweek, Hour, Minute, Seconds, 0
        :type date: array
        """
        writeval = [self.__dec_bcd(date[6]),
                    self.__dec_bcd(date[5]),
                    self.__dec_bcd(date[4]),
                    self.__dec_bcd(date[3] + self.__weekday_start),
                    self.__dec_bcd(date[2]),
                    self.__dec_bcd(date[1]),
                    self.__dec_bcd(date[0]) - self.__century]

        self.__bus.writeto_mem(self.__rtcaddress, 0x00,bytearray(writeval))
       
        return

    def read_date(self):
        """
        Read the date and time from the RTC

        :return: array
        :rtype: array
        """
        readval = self.__bus.readfrom_mem(self.__rtcaddress, 0, 7)
        
        date = ((self.__bcd_dec(readval[6]) + self.__century,
                                                   self.__bcd_dec(readval[5]),
                                                   self.__bcd_dec(readval[4]),
                                                   self.__bcd_dec(readval[2]),
                                                   self.__bcd_dec(readval[1]),
                                                   self.__bcd_dec(readval[0])))
       
        return date

    def enable_output(self):
        """
        Enable the output pin
        """

        self.__rtcconfig = self.__updatebyte(self.__rtcconfig, 7, 1)
        self.__rtcconfig = self.__updatebyte(self.__rtcconfig, 4, 1)
        self.__bus.writeto_mem(self.__rtcaddress, self.CONTROL, bytearray(self.__rtcconfig))
        return

    def disable_output(self):
        """
        Disable the output pin
        """

        self.__rtcconfig = self.__updatebyte(self.__rtcconfig, 7, 0)
        self.__rtcconfig = self.__updatebyte(self.__rtcconfig, 4, 0)
        self.__bus.writeto_mem(self.__rtcaddress, self.CONTROL, bytearray(self.__rtcconfig))
        return

    def set_frequency(self, frequency):
        """
        Set the frequency of the output pin square-wave

        :param frequency: 1 = 1Hz, 2 = 4.096KHz, 3 = 8.192KHz, 4 = 32.768KHz
        :type frequency: int
        """

        if frequency == 1:
            self.__rtcconfig = self.__updatebyte(self.__rtcconfig, 0, 0)
            self.__rtcconfig = self.__updatebyte(self.__rtcconfig, 1, 0)
        if frequency == 2:
            self.__rtcconfig = self.__updatebyte(self.__rtcconfig, 0, 1)
            self.__rtcconfig = self.__updatebyte(self.__rtcconfig, 1, 0)
        if frequency == 3:
            self.__rtcconfig = self.__updatebyte(self.__rtcconfig, 0, 0)
            self.__rtcconfig = self.__updatebyte(self.__rtcconfig, 1, 1)
        if frequency == 4:
            self.__rtcconfig = self.__updatebyte(self.__rtcconfig, 0, 1)
            self.__rtcconfig = self.__updatebyte(self.__rtcconfig, 1, 1)        
        self.__bus.writeto_mem(self.__rtcaddress, self.CONTROL, bytearray(self.__rtcconfig))
        return

    def write_memory(self, address, valuearray):
        """
        Write to the memory on the DS1307
        The DS1307 contains 56-Byte, battery-backed RAM with Unlimited Writes

        :param address: 0x08 to 0x3F
        :type address: int
        :param valuearray: byte array containing data to be written to memory
        :type valuearray: int array
        :raises ValueError: write_memory: memory overflow error,
                            address length exceeds 0x3F
        :raises ValueError: write_memory: address out of range
        """

        if address >= 0x08 and address <= 0x3F:
            if address + len(valuearray) <= 0x3F:
                self.__bus.writeto_mem(self.__rtcaddress, address,bytearray(valuearray))
            else:
                raise ValueError('write_memory: memory overflow error: address + \
                                length exceeds 0x3F')
        else:
            raise ValueError('write_memory: address out of range')

    def read_memory(self, address, length):
        """
        Read from the memory on the DS1307
        The DS1307 contains 56-Byte, battery-backed RAM with Unlimited Writes

        :param address: 0x08 to 0x3F
        :type address: int
        :param length: number of bytes to read, up to 32 bytes.
                       length can not exceed the address space.
        :type length: int
        :raises ValueError: read_memory: memory overflow error,
                            address length exceeds 0x3F
        :raises ValueError: read_memory: address out of range
        :return: array of bytes from RAM
        :rtype: int array
        """

        if address >= 0x08 and address <= 0x3F:
            if address <= (0x3F - length):
                return self.__bus.readfrom_mem(self.__rtcaddress,address,length)

            else:
                raise ValueError('read_memory: memory overflow error: address + \
                                length exceeds 0x3F')
        else:
            raise ValueError('read_memory: address out of range')

