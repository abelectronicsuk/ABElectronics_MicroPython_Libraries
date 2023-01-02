#!/usr/bin/env python
"""
================================================
AB Electronics UK: I2CSwitch - 4 Channel I2C Switch

Raspberry Pi Pico MicroPython Library
================================================
"""

import machine
import re
import time

class I2CSwitch(object):
    """
    I2CSwitch class for controlling the PCA9546A I2C Switch
    """

    # define GPIO Reset Pin
    __RESETPIN = 12

    # 11

    # local variables
    __ctl = 0x00
    __address = 0x70
    __bus = None
    
    
    __reset = None;
    
    # local methods
    @staticmethod
    def __checkbit(byte, bit):
        """
        Internal method for reading the value of a single bit within a byte

        :param byte: input value
        :type byte: int
        :param bit: location within value to check
        :type bit: int
        :return: value of the selected bit, 0 or 1
        :rtype: int
        """
        value = 0
        if byte & (1 << bit):
            value = 1
        return value

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

    def __write(self, value):
        """
        Internal method for writing data to the I2C bus

        :param value: value to write
        :type value: int
        :return: IOError
        :rtype: IOError
        """
        self.__bus.writeto(self.__address, bytearray([value]))
        

    def __read(self):
        """
        Internal method for reading data from the I2C bus

        :return: IOError
        :rtype: IOError
        """
        try:
            #result = self.__bus.readfrom(self.__address,8)
            result = self.__bus.readfrom_mem(self.__address, 0x00, 1)
            return result
        except  Exception as err:
            return err

    # public methods

    def __init__(self, address=0x70,  sda=None, scl=None):
        """
        Initialise object with the I2C address for the I2C Switch board

        :param address: device I2C address, defaults to 0x70
        :type address: int, optional
        :type bus: int, optional
        :param sda: SDA pin
        :type sda: int
        :param scl: SCL pin
        :type scl: int
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
        
        self.__address = address
        self.__write(self.__ctl)
        
        self.__reset = machine.Pin(self.__RESETPIN, machine.Pin.OUT)
        self.__reset.on()


    def switch_channel(self, channel):
        """
        Enable the specified I2C channel and disable other channels

        :param channel: 1 to 4
        :type channel: int
        :raises ValueError: set_channel: channel out of range (1 to 4)
        """
        if channel < 1 or channel > 4:
            raise ValueError('set_channel: channel out of range (1 to 4)')
        else:
            self.__ctl = 0
            self.__ctl = self.__updatebyte(self.__ctl, channel - 1, 1)
            
            self.__write(self.__ctl)

    def set_channel_state(self, channel, state):
        """
        Set the state of an individual I2C channel

        :param channel: 1 to 4
        :type channel: int
        :param state: True or False
        :type state: bool
        :raises ValueError: set_channel: channel out of range (1 to 4)
        :raises ValueError: set_channel: state out of range (True or False)
        """
        if channel < 1 or channel > 4:
            raise ValueError('set_channel: channel out of range (1 to 4)')
        if type(state) != bool:
            raise ValueError('set_channel: state out of range (True or False)')
        else:
            if state is True:
                self.__ctl = self.__updatebyte(self.__ctl, channel - 1, 1)
            else:
                self.__ctl = self.__updatebyte(self.__ctl, channel - 1, 0)
            self.__write(self.__ctl)

    def get_channel_state(self, channel):
        """
        Get the state of an individual I2C channel

        :param channel: 1 to 4
        :type channel: int
        :raises ValueError: set_channel: channel out of range (1 to 4)
        :return: True = channel enabled, False = channel disabled
        :rtype: bool
        """
        if channel < 1 or channel > 4:
            raise ValueError('set_channel: channel out of range (1 to 4)')
        else:
            ctrreg = self.__read()
            curval = int.from_bytes(ctrreg, 'big', False)
            if (self.__checkbit(curval, channel - 1) == 1):
                return True
            else:
                return False

    def reset(self):
        """
        Reset the PCA9546A I2C switch.
        Resetting allows the PCA9546A to recover from a situation in which one
        of the downstream I2C buses is stuck in a low state.
        All channels will be set to an off-state.

        :raises ValueError: Failed to write to GPIO pin
        """
        try:
            self.__reset.off()
            # wait 1 millisecond before setting the pin high again
            time.sleep(0.001)
            self.__reset.on()
            # wait another 1 millisecond for the device to reset
            time.sleep(0.001)
        except:
            print("Failed to write to GPIO pin")

