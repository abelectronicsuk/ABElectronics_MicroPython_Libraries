#!/usr/bin/env python
"""
================================================
ABElectronics ADCDAC Pi Analogue to Digital / Digital to Analogue Converter
================================================

Based on the Microchip MCP3202 and MCP4822
"""

import machine
import utime
import ustruct
import sys

class ADCDACPi(object):
    """
    Based on the Microchip MCP3202 and MCP4822
    """

    # variables
    __adcrefvoltage = 3.3  # reference voltage for the ADC chip.
    
    # Define Cable Select Pins
    adccs = machine.Pin(5, machine.Pin.OUT)
    daccs = machine.Pin(19, machine.Pin.OUT)

    # Define SPI bus and init
    spiDevice = machine.SPI(0,
                  baudrate=1000000,
                  polarity=1,
                  phase=1,
                  bits=8,
                  firstbit=machine.SPI.MSB,
                  sck=machine.Pin(2),
                  mosi=machine.Pin(3),
                  miso=machine.Pin(4))
    dactx = bytearray([0, 0])

    # Max DAC output voltage. Depends on gain factor
    # The following table is in the form <gain factor>:<max voltage>

    __dacMaxOutput__ = {
        1: 2.048,  # This is Vref
        2: 3.3  # This is the voltage of the 3.3V rail
    }

    # public methods
    def __init__(self, gain_factor=1):
        """
        Class Constructor - Initialise the DAC

        :param gain_factor: Set the DAC's gain factor. The value should
           be 1 or 2.  Gain factor is used to determine output voltage
           from the formula: Vout = G * Vref * D/4096
           Where G is gain factor, Vref (for this chip) is 2.048 and
           D is the 12-bit digital value, defaults to 1
        :type gain_factor: int, optional
        :raises ValueError: DAC __init__: Invalid gain factor. Must be 1 or 2
        """
        
        self._out_buf = bytearray(3)
        self._out_buf[0] = 0x01
        self._in_buf = bytearray(3)
        
        
        if (gain_factor != 1) and (gain_factor != 2):
            raise ValueError('DAC __init__: Invalid gain factor. \
                            Must be 1 or 2')
        else:
            self.gain = gain_factor
            self.maxdacvoltage = self.__dacMaxOutput__[self.gain]

    def read_adc_voltage(self, channel, mode):
        """
        [summary]

        :param channel: 1 or 2
        :type channel: int
        :param mode: 0 = single ended, 1 = differential
        :type mode: int
        :raises ValueError: read_adc_voltage: channel out of range
        :raises ValueError: read_adc_voltage: mode out of range
        :return: voltage
        :rtype: float
        """
        if (channel > 2) or (channel < 1):
            raise ValueError('read_adc_voltage: channel out of range')
        if (mode > 1) or (mode < 0):
            raise ValueError('read_adc_voltage: mode out of range')
        raw = self.read_adc_raw(channel, mode)
        voltage = float((self.__adcrefvoltage / 4096) * raw)
        return voltage

    def read_adc_raw(self, channel, mode):
        """
        Read the raw value from the selected channel on the ADC

        :param channel: 1 or 2
        :type channel: int
        :param mode: 0 = single ended, 1 = differential
        :type mode: int
        :raises ValueError: read_adc_voltage: channel out of range
        :raises ValueError: read_adc_voltage: mode out of range
        :return: raw value from ADC, 0 to 4095
        :rtype: int
        """
        """
        self.cs.value(0) # select
        self._out_buf[1] = ((not mode) << 7) | (channel << 4)
        self.spiDevice.write_readinto(self._out_buf, self._in_buf)
        self.cs.value(1) # turn off
        return ((self._in_buf[1] & 0x03) << 8) | self._in_buf[2]
        """
        
        self.adccs.value(0) # select
        self._in_buf = bytearray([0, 0, 0])
        
        if (channel > 2) or (channel < 1):
            raise ValueError('read_adc_voltage: channel out of range')
        if (mode > 1) or (mode < 0):
            raise ValueError('read_adc_voltage: mode out of range')
        if mode == 0:
            
            self._out_buf = bytearray([1, (1 + channel) << 6, 0])
            
            self.adccs.value(0) # select
            self.spiDevice.write_readinto(self._out_buf, self._in_buf)
            self.adccs.value(1) # turn off
            
            ret = ((self._in_buf[1] & 0x0F) << 8) + (self._in_buf[2])
        if mode == 1:
            self._out_buf = bytearray([1, 0x40, 0])
            if channel == 1:
                self._out_buf = bytearray([1, 0x00, 0])                
                
            self.adccs.value(0) # select
            self.spiDevice.write_readinto(self._out_buf, self._in_buf)
            self.adccs.value(1) # turn off
            ret = ((self._in_buf[1]) << 8) + (self._in_buf[2])
        self.adccs.value(1) 
        return ret
    

    def set_adc_refvoltage(self, voltage):
        """
        Set the reference voltage for the analogue to digital converter.
        The ADC uses the raspberry pi 3.3V power as a voltage reference so
        using this method to set the reference to match the
        exact output voltage from the 3.3V regulator will increase the
        accuracy of the ADC readings.

        :param voltage: reference voltage
        :type voltage: float
        :raises ValueError: set_adc_refvoltage: reference voltage out of range
        """
        if (voltage >= 0.0) and (voltage <= 7.0):
            self.__adcrefvoltage = voltage
        else:
            raise ValueError('set_adc_refvoltage: reference voltage \
                            out of range')
        return

    def set_dac_voltage(self, channel, voltage):
        """
        Set the voltage for the selected channel on the DAC.
        The DAC has two gain values, 1 or 2, which can be set when the ADCDAC
        object is created.
        A gain of 1 will give a voltage between 0 and 2.047 volts.
        A gain of 2 will give a voltage between 0 and 3.3 volts.

        :param channel: 1 or 2
        :type channel: int
        :param voltage: DAC target voltage
        :type voltage: float
        :raises ValueError: set_dac_voltage: DAC channel needs to be 1 or 2
        :raises ValueError: set_dac_voltage: voltage out of range
        """
        if (channel > 2) or (channel < 1):
            raise ValueError('set_dac_voltage: DAC channel needs to be 1 or 2')
        if (voltage >= 0.0) and (voltage < self.maxdacvoltage):
            rawval = (voltage / 2.048) * 4096 / self.gain
            self.set_dac_raw(channel, int(rawval))
        else:
            raise ValueError('set_dac_voltage: voltage out of range')
        return

    def set_dac_raw(self, channel, value):
        """
        Set the raw value for the selected channel on the DAC

        :param channel: 1 or 2
        :type channel: int
        :param value: 0 and 4095
        :type value: int
        :raises ValueError: set_dac_voltage: DAC channel needs to be 1 or 2
        :raises ValueError: set_dac_voltage: value out of range
        """

        if (channel > 2) or (channel < 1):
            raise ValueError('set_dac_voltage: DAC channel needs to be 1 or 2')
        if (value < 0) and (value > 4095):
            raise ValueError('set_dac_voltage: value out of range')

        self.dactx[1] = (value & 0xff)

        if self.gain == 1:
            self.dactx[0] = (((value >> 8) & 0xff) | (channel - 1) << 7 |
                             1 << 5 | 1 << 4)
        else:
            self.dactx[0] = (((value >> 8) & 0xff) | (channel - 1) << 7 |
                             1 << 4)

        # Write to device
        self.daccs.value(0) # select
        self.spiDevice.write(self.dactx)
        self.daccs.value(1) # select
        return
