AB Electronics UK IO Pi MicroPython Library
=====

MicroPython Library to use the IO Pi expansion board from https://www.abelectronics.co.uk with the Raspberry Pi Pico development board.

The example python files can be found in /ABElectronics_MicroPython_Libraries/IOPi/demos  

**Note:** Microchip recommends that pin 8 (GPA7) and pin 16 (GPB7) are used as outputs only.  This change was made for revision D MCP23017 chips manufactured after June 2020. See the [MCP23017 datasheet](https://www.abelectronics.co.uk/docs/pdf/microchip-mcp23017.pdf) for more information.

### Downloading and Installing the library

To download to your Raspberry Pi type in the terminal: 

```
git clone https://github.com/abelectronicsuk/ABElectronics_MicroPython_Libraries.git
```

To install the MicroPython Library use the Thonny Python IDE from https://thonny.org/

Create a file for your chosen board and copy the contents of the python file into that board's directory. For example for the IO Pi create a new file in Thonny called IOPi.py and copy contents from  IOPi.py into the new file and save it onto the Raspberry Pi Pico board.

Create a second file where your main program will reside and import the board library at the top of the program.  

```
from IOPi import IOPi
```

Run with **"Run Current Command"** or **F5** in Thonny.  

---

Pins used on the Raspberry Pi Pico:
----------

The IO Pi library uses the following pins on the Raspberry Pi Pico board.

| Pico Pin | Pico GPIO| Function | Pi Pin  | Pi GPIO |
|----------|----------|----------|---------|---------|
| 26       | 20       | I2C SDA  |3        | GPIO 2  |
| 27       | 21       | I2C SCL  |5        | GPIO 3  |

You will also need to connect 3.3V, 5V and GND on the IO Pi GPIO header.

---

Wiring Diagram:
----------
![Connecting the IO Pi Plus to a Pico!](https://github.com/abelectronicsuk/ABElectronics_MicroPython_Libraries/raw/main/images/pico-iopiplus.png "Connecting the IO Pi Plus to a Pico")

Classes:
----------  
```
IOPi(address, initialise, sda, scl)
```
**Parameters:**  
address: i2c address for the target device. 0x20 to 0x27  
initialise (optional): True = direction set as inputs, pull-ups disabled, ports not inverted. False = device state unaltered., defaults to True  
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
set_pin_pullup(pin, value)
```
Set the internal 100K pull-up resistors for an individual pin  
**Parameters:**  
pin: pin to update, 1 to 16 
value: 1 = enabled, 0 = disabled  
**Returns:** null
___
```
get_pin_pullup(pin)
```  
Get the internal 100K pull-up resistors for an individual pin  
**Parameters:**  
pin: pin to read, 1 to 16  
**Returns:** 1 = enabled, 0 = disabled  
___
```
set_port_pullups(port, value)
```
Set the internal 100K pull-up resistors for the selected IO port  
**Parameters:**  
port: 0 = pins 1 to 8, 1 = pins 9 to 16  
value: number between 0 and 255 or 0x00 and 0xFF.  Each bit in the 8-bit number represents a pin on the port.  1 = Enabled, 0 = Disabled  
**Returns:** null  
___
```
get_port_pullups(port): 
```
Get the internal pull-up status for the selected IO port  
**Parameters:**  
port: 0 = pins 1 to 8, 1 = pins 9 to 16   
**Returns:** number between 0 and 255 (0xFF)  
___
```
set_bus_pullups(value)
```
Set internal 100K pull-up resistors for an IO bus  
**Parameters:**  
value: 16-bit number 0 to 65535 (0xFFFF). For each bit 1 = enabled, 0 = disabled  
**Returns:** null
___
```
get_bus_pullups()
```
Get the internal 100K pull-up resistors for an IO bus  
**Returns:** 16-bit number 0 to 65535 (0xFFFF). For each bit 1 = enabled, 0 = disabled  
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
invert_pin(pin, value)
```
Invert the polarity of the selected pin  
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
invert_port(port, value)
```
Invert the polarity of the pins on a selected port  
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
invert_bus(value)
```
Invert the polarity of the pins on the bus  
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
```
mirror_interrupts(value)
```
Sets whether the interrupt pins INT A and INT B are independently connected to each port or internally connected.  
**Parameters:**  
value: 1 = The INT pins are internally connected, 0 = The INT pins are not connected. INT A is associated with PortA and INT B is associated with PortB    
**Returns:** null
___
```
set_interrupt_polarity(value)
```
Sets the polarity of the INT output pins  
**Parameters:**  
value: 0 = Active Low, 1 = Active High  
**Returns:** null  
___
```
get_interrupt_polarity()
```
Get the polarity of the INT output pins  
**Returns:** 1 = Active-high.  0 = Active-low.  
___
```
set_interrupt_type(port, value)
```
Sets the type of interrupt for each pin on the selected port  
**Parameters:**  
port: 0 = pins 1 to 8, 1 = pins 9 to 16  
value: number between 0 and 255 or 0x00 and 0xFF.  Each bit in the 8-bit number represents a pin on the port.  1 = interrupt is fired when the pin matches the default value, 0 = the interrupt is fired on state change  
**Returns:** null  
___
```
get_interrupt_type(port): 
```
Get the type of interrupt for each pin on the selected port  
**Parameters:**  
port: 0 = pins 1 to 8, 1 = pins 9 to 16   
**Returns:** number between 0 and 255 (0xFF)  
For each bit 1 = interrupt is fired when the pin matches the default value, 0 = interrupt fires on state change  
___
```
set_interrupt_defaults(port, value)
```
These bits set the compare value for pins configured for interrupt-on-change on the selected port.  
If the associated pin level is the opposite of the register bit, an interrupt occurs.    
**Parameters:**  
port: 0 = pins 1 to 8, 1 = pins 9 to 16, 
value: compare value between 0 and 255 or 0x00 and 0xFF.  Each bit in the 8-bit number represents a pin on the port.  
**Returns:** null  
___
```
get_interrupt_defaults(port): 
```
Get the interrupt default value for each pin on the selected port  
**Parameters:**  
port: 0 = pins 1 to 8, 1 = pins 9 to 16   
**Returns:** number between 0 and 255 (0xFF)  
___
```
set_interrupt_on_pin(pin, value)
```
Enable interrupts for the selected pin  
**Parameters:**  
pin: 1 to 16  
value: 0 = interrupt disabled, 1 = interrupt enabled  
**Returns:** null
___
```
get_interrupt_on_pin(pin)
```  
Gets whether the interrupt is enabled for the selected pin  
**Parameters:**  
pin: pin to read, 1 to 16   
**Returns:** 1 = enabled, 0 = disabled
___
```
set_interrupt_on_port(port, value)
```
Enable interrupts for the pins on the selected port  
**Parameters:**  
port: 0 = pins 1 to 8, 1 = pins 9 to 16  
value: number between 0 and 255 or 0x00 and 0xFF.  Each bit in the 8-bit number represents a pin on the port.  
**Returns:** null
___
```
get_interrupt_on_port(port): 
```
Gets whether the interrupts are enabled for the selected port  
**Parameters:**  
port: 0 = pins 1 to 8, 1 = pins 9 to 16   
**Returns:** number between 0 and 255 (0xFF).  For each bit 1 = enabled, 0 = disabled  
___
```
set_interrupt_on_bus(value)
```
Enable interrupts for the pins on the bus  
**Parameters:**  
value: 16-bit number 0 to 65535 (0xFFFF).  For each bit 1 = enabled, 0 = disabled  
**Returns:** null
___
```
get_interrupt_on_bus()
```
Gets whether the interrupts are enabled for the bus  
**Returns:** 16-bit number 0 to 65535 (0xFFFF). For each bit 1 = enabled, 0 = disabled  
___
```
read_interrupt_status(port)
```
Read the interrupt status for the pins on the selected port  
**Parameters:**  
port: 0 = pins 1 to 8, 1 = pins 9 to 16  
**Returns:**  number between 0 and 255 or 0x00 and 0xFF.  Each bit in the 8-bit number represents a pin on the port.  1 = Enabled, 0 = Disabled
___
```
read_interrupt_capture(port)
```
Read the value from the selected port at the time of the last interrupt trigger  
**Parameters:**  
port: 0 = pins 1 to 8, 1 = pins 9 to 16  
**Returns:**  number between 0 and 255 or 0x00 and 0xFF.  Each bit in the 8-bit number represents a pin on the port.  1 = Enabled, 0 = Disabled
___
```
reset_interrupts()
```
Set the interrupts A and B to 0  
**Parameters:** null  
**Returns:** null

Usage
====
To use the IO Pi library in your code you must first import the library:
```
from IOPi import IOPi
```

Next, you must initialise the IO object with the I2C address of the I/O controller chip.  The default addresses for the IO Pi are 0x20 and 0x21:

```
bus1 = IOPI(0x20)
```

We will read the inputs 1 to 8 from bus 2 so set port 0 as inputs and enable the internal pull-up resistors 

```
bus1.set_port_direction(0, 0xFF)
bus1.set_port_pullups(0, 0xFF)
```

You can now read pin 1 with:
```
print('Pin 1: ' + str(bus1.read_pin(1)))
```
