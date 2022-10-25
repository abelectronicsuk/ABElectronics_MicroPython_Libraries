AB Electronics UK I2C Switch MicroPython Library
=====

MicroPython Library to use the I2C Switch expansion board from https://www.abelectronics.co.uk with the Raspberry Pi Pico development board.

The example python files can be found in /ABElectronics_MicroPython_Libraries/I2CSwitch/demos  

### Downloading and Installing the library

To download to your Raspberry Pi type in terminal: 

```
git clone https://github.com/abelectronicsuk/ABElectronics_MicroPython_Libraries.git
```

To install the MicroPython Library use the Thonny Python IDE from https://thonny.org/

Create a file for your chosen board and copy the contents of the python file in that board's directory. For example for the I2C Switch create a new file in thonny called I2CSwitch.py and copy contents from  I2CSwitch.py into the new file and save it onto the Raspberry Pi Pico board.

Create a second file where your main program will reside and import the board library at the top of the program.  

```
from I2CSwitch import I2CSwitch
```

Run with **"Run Current Command"** or **F5** in Thonny.  

---

Pins used on the Raspberry Pi Pico:
----------

The I2C Switch library uses the following pins on the Raspberry Pi Pico board.

| Pico Pin | Pico GPIO| Function |  Pi Pin  | Pi GPIO |
|----------|----------|----------|----------|---------|
| 26       | 20       | I2C SDA  | 3        | GPIO 2  |
| 27       | 21       | I2C SCL  | 5        | GPIO 3  |
| 11       | 8        | Reset    | 13       | GPIO 27 |
You will also need to connect 3.3V, 5V and GND on the I2C Switch GPIO header.


# Class: I2CSwitch #

```
I2CSwitch(address, sda, scl)
```
The I2CSwitch class provides control over the I2C Switch outputs on the PCA9546A controller.  Functions include setting and getting the I2C channel and resetting the switch.  

**Parameters:**  
address: Device i2c address. Supported I2C addresses are 0x70 to 0x77. defaults to 0x70  
sda (optional): I2C SDA pin.  If no value is set the class will default to pin 20.  
scl (optional): I2C SCL pin.  If no value is set the class will default to pin 21.  

Initialise with the I2C address for the I2C Switch. 

```
i2cswitch = I2CSwitch(0x70)
```

Functions:
----------

```
switch_channel(channel) 
```
Switch on the selected channel and switch off all other channels.  
**Parameters:** channel - 1 to 4.  
**Returns:** null  

---
```
set_channel_state(channel, state) 
```
Set the state for the selected channel.  All other channels remain in their previous state.  
**Parameters:**  
channel - 1 to 4  
state - True or False. True = channel on, False = channel off.  
**Returns:** null  

---
```
get_channel_state(channel) 
```
Get the state for the selected channel.  
**Parameters:** channel - 1 to 4  
**Returns:** True or False. True = channel on, False = channel off.  

---
```
reset() 
```
Reset the PCA9546A I2C switch.  Resetting allows the PCA9546A to recover from a situation in which one of the downstream I2C buses is stuck in a low state.  All channels will be set to an off state.  
**Returns:** null  


Usage
====

To use the I2C Switch class in your code you must first import the class:
```
from I2CSwitch import I2CSwitch
```
Next you must initialise the I2CSwitch object:
```
i2cswitch = I2CSwitch(0x70)
```
Set the I2C switch to channel 2
```
i2cswitch.switch_channel(2)  
```
