#!/usr/bin/env python
"""
================================================
AB Electronics UK I2CSwitch | Channel select demo for MicroPython Library

Run using Thonny Python IDE from https://thonny.org/

Create a file in Thonny called I2CSwitch.py, copy contents from I2CSwitch.py 
to the file and save it onto the Raspberry Pi Pico

Create a file named demo_switch.py, copy the code from this file and save
onto the Raspberry Pi Pico

Run with "Run Current Command" or F5 in Thonny

================================================

This demo shows how to set the I2C output channel using the channel set in the
variable channelparam as a number 1 to 4.
"""

from I2CSwitch import I2CSwitch


def main():
    """
    Main program function
    """

    # Create an instance of the I2CSwitch class on i2c address 0x70 with SDA on pin 20 and SCL on pin 21
    i2cswitch = I2CSwitch(0x70,20 ,21)

    # Reset the switch
    i2cswitch.reset()
    
    # Set channel to 3
    channelparam = 3

    

    if (channelparam < 1 or channelparam > 4):
        print('error: channel must be between 1 and 4')
    else:
        # Set the I2C channel
        i2cswitch.switch_channel(channelparam)
        
        # Get the state of the selected channel from the I2C switch
        status = i2cswitch.get_channel_state(channelparam)
        
        # Print the result from get_channel_state()
        if status is True:
            print('Channel set to ', channelparam)
        else:
            print('Error setting channel')


if __name__ == "__main__":
    main()

