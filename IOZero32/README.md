AB Electronics UK IO Zero 32 MicroPython Library
=====

MicroPython Library to use the IO Zero 32 expansion board from https://www.abelectronics.co.uk with the Raspberry Pi Pico development board.

The example python files can be found in /ABElectronics_MicroPython_Libraries/IOZero32/demos  

### Downloading and Installing the library

To download to your Raspberry Pi type in terminal: 

```
git clone https://github.com/abelectronicsuk/ABElectronics_MicroPython_Libraries.git
```

To install the MicroPython Library use the Thonny Python IDE from https://thonny.org/

Create a file for your chosen board and copy the contents of the python file in that board's directory. For example for the IO Zero 32 create a new file in thonny called IOZero32.py and copy contents from  IOZero32.py into the new file and save it onto the Raspberry Pi Pico board.

Create a second file where your main program will reside and import the board library at the top of the program.  

```
from IOZero32 import IOZero32
```

Run with **"Run Current Command"** or **F5** in Thonny.  

---

Pins used on the Raspberry Pi Pico:
----------

The IO Zero 32 library uses the following pins on the Raspberry Pi Pico board.

| Pico Pin | Pico GPIO| Function | Pi Pin  | Pi GPIO |
|----------|----------|----------|---------|---------|
| 26       | 20       | I2C SDA  |3        | GPIO 2  |
| 27       | 21       | I2C SCL  |5        | GPIO 3  |

You will also need to connect 3.3V, 5V and GND on the IO Zero 32 GPIO header.


Classes:
----------  
```
IOZero32(address, sda, scl)
```
**Parameters:**  
address: i2c address for the target device. 0x20 to 0x27  
sda (optional): I2C SDA pin.  If no value is set the class will default to pin 20.  
scl (optional): I2C SCL pin.  If no value is set the class will default to pin 21.  

Functions:
----------
___
```
set_pin_direction(pin, value):
```
Sets the IO direction for an individual pin  
**Parameters:**  
pin: 1 to 16   
value: 1 = input, 0 = output  
**Returns:** null
___
```
get_pin_direction(pin)
```  
Get the IO direction for an individual pin  
**Parameters:**  
pin: pin to read, 1 to 16   
**Returns:** 1 = input, 0 = output  
___
```
set_port_direction(port, value): 
```
Sets the IO direction for the specified IO port  
**Parameters:**  
port: 0 = pins 1 to 8, 1 = pins 9 to 16   
value: number between 0 and 255 or 0x00 and 0xFF.  Each bit in the 8-bit number represents a pin on the port.  1 = input, 0 = output  
**Returns:** null
___
```
get_port_direction(port): 
```
Get the direction from an IO port  
**Parameters:**  
port: 0 = pins 1 to 8, 1 = pins 9 to 16   
**Returns:** number between 0 and 255 (0xFF)  
___
```
set_bus_direction(value): 
```
Sets the IO direction for all pins on the bus  
**Parameters:**  
value: 16-bit number 0 to 65535 (0xFFFF).  For each bit 1 = input, 0 = output  
**Returns:** null
___
```
get_bus_direction()
```
Get the direction for an IO bus  
**Returns:** 16-bit number 0 to 65535 (0xFFFF). For each bit 1 = input, 0 = output  
___
```
write_pin(pin, value)
```
Write to an individual pin 1 - 16  
**Parameters:**  
pin: 1 to 16  
value: 1 = logic high, 0 = logic low  
**Returns:** null  
___
```
write_port(port, value)
```
Write to all pins on the selected port  
**Parameters:**  
port: 0 = pins 1 to 8, 1 = pins 9 to 16  
value:  number between 0 and 255 or 0x00 and 0xFF.  Each bit in the 8-bit number represents a pin on the port.  1 = logic high, 0 = logic low    
**Returns:** null  
___
```
write_bus(value)
```
Write to all pins on the selected bus  
**Parameters:**  
value: 16-bit number 0 to 65535 (0xFFFF). For each bit 1 = logic high, 0 = logic low  
**Returns:** null  
___
```
read_pin(pin)
```
Read the value of an individual pin 1 - 16   
**Parameters:**  
pin: 1 to 16  
**Returns:** 0 = logic low, 1 = logic high  
___
```
read_port(port)
```
Read all pins on the selected port  
**Parameters:**  
port: 0 = pins 1 to 8, 1 = pins 9 to 16  
**Returns:** number between 0 and 255 or 0x00 and 0xFF.  Each bit in the 8-bit number represents a pin on the port.  0 = logic low, 1 = logic high
___
```
read_bus()
```
Read all pins on the bus  
**Returns:** 16-bit number 0 to 65535 (0xFFFF) Each bit in the 16-bit number represents a pin on the port.  0 = logic low, 1 = logic high  
___
```
set_pin_polarity(pin, value)
```
Set the polarity of the selected pin  
**Parameters:**  
pin: 1 to 16  
value: 0 = same logic state of the input pin, 1 = inverted logic state of the input pin  
**Returns:** null
___
```
get_pin_polarity(pin)
```  
Get the polarity of the selected pin  
**Parameters:**  
pin: pin to read, 1 to 16   
**Returns:** 0 = same logic state of the input pin, 1 = inverted logic state of the input pin  
___
```
set_port_polarity(port, value)
```
Set the polarity of the pins on a selected port  
**Parameters:**  
port: 0 = pins 1 to 8, 1 = pins 9 to 16  
value: number between 0 and 255 or 0x00 and 0xFF.  Each bit in the 8-bit number represents a pin on the port.  0 = same logic state of the input pin, 1 = inverted logic state of the input pin  
**Returns:** null
___
```
get_port_polarity(port): 
```
Get the polarity for the selected IO port  
**Parameters:**  
port: 0 = pins 1 to 8, 1 = pins 9 to 16   
**Returns:** number between 0 and 255 (0xFF) 
___
```
set_bus_polarity(value)
```
Set the polarity of the pins on the bus  
**Parameters:**  
value: 16-bit number 0 to 65535 (0xFFFF).  For each bit 0 = same logic state of the input pin, 1 = inverted logic state of the input pin  
**Returns:** null  
___
```
get_bus_polarity()
```
Get the polarity of the pins on the bus  
**Returns:** 16-bit number 0 to 65535 (0xFFFF). For each bit 0 = same logic state of the input pin, 1 = inverted logic state of the input pin  
___

Usage
====
To use the IO Zero 32 library in your code you must first import the library:
```
from IOZero32 import IOZero32
```

Next you must initialise the IOZero32 object with the I2C address of the I/O controller chip.  The default addresses for the IO Zero 32 are 0x20 and 0x21:

```
bus1 = IOZero32(0x20)
```

We will read the inputs 1 to 8 from bus 1 so set port 0 to be inputs.  

```
bus1.set_port_direction(0, 0xFF)
```

You can now read the pin 1 with:
```
print('Pin 1: ' + str(bus1.read_pin(1)))
```
