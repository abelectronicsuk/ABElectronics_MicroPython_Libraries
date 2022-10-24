AB Electronics UK RTC Pi MicroPython Library
=====

MicroPython Library to use the RTC Pi expansion board from https://www.abelectronics.co.uk with the Raspberry Pi Pico development board.

The example python files can be found in /ABElectronics_MicroPython_Libraries/RTCPi/demos  

### Downloading and Installing the library

To download to your Raspberry Pi type in terminal: 

```
git clone https://github.com/abelectronicsuk/ABElectronics_MicroPython_Libraries.git
```

To install the MicroPython Library use the Thonny Python IDE from https://thonny.org/

Create a file for your chosen board and copy the contents of the python file in that board's directory. For example for the RTC Pi create a new file in thonny called RTCPi.py and copy contents from  RTCPi.py into the new file and save it onto the Raspberry Pi Pico board.

Create a second file where your main program will reside and import the board library at the top of the program.  

```
from RTCPi import RTCPi
```

Run with **"Run Current Command"** or **F5** in Thonny.  

---

Pins used on the Raspberry Pi Pico:
----------

The RTC Pi library uses the following pins on the Raspberry Pi Pico board.

| Pin      | Use        |
|----------|------------|
| 20       | I2C SDA    |
| 21       | I2C SCL    |

You will also need to connect 3.3V, 5V and GND on the RTC Pi GPIO header.

Class:
----------

```
RTC(sda, scl)
```
**Parameters:**  
sda (optional): I2C SDA pin.  If no value is set the class will default to pin 20.  
scl (optional): I2C SCL pin.  If no value is set the class will default to pin 21.  
 

Functions:
----------

```
set_date(date) 
```
Set the date and time on the RTC in ISO 8601 format - YYYY-MM-DDTHH:MM:SS   
**Parameters:** date   
**Returns:** null

```
read_date() 
```
Returns the date from the RTC in ISO 8601 format - YYYY-MM-DDTHH:MM:SS   
**Returns:** date


```
enable_output() 
```
Enable the square-wave output on the SQW pin.  
**Returns:** null

```
disable_output()
```
Disable the square-wave output on the SQW pin.   
**Returns:** null

```
set_frequency(frequency)
```
Set the frequency for the square-wave output on the SQW pin.   
**Parameters:** frequency - options are: 1 = 1Hz, 2 = 4.096KHz, 3 = 8.192KHz, 4 = 32.768KHz   
**Returns:** null

```
write_memory(address, valuearray)
```
Write to the memory on the ds1307. The ds1307 contains 56-Byte, battery-backed RAM with Unlimited Writes  
**Parameters:** address - 0x08 to 0x3F  
valuearray - byte array containing data to be written to memory  
**Returns:** null

```
read_memory(address, length)
```
Read from the memory on the ds1307  
**Parameters:** address - 0x08 to 0x3F 
length - up to 32 bytes.  
length can not exceed the available address space.  
**Returns:** array of bytes

Usage
====

To use the RTC Pi library in your code you must first import the library:
```
from RTCPi import RTC
```

Next you must initialise the RTC object:

```
rtc = RTC()
```
Set the current time in ISO 8601 format:
```
rtc.set_date("2013-04-23T12:32:11")
```
Enable the square-wave output at 8.192KHz on the SQW pin:
```
rtc.set_frequency(3)
rtc.enable_output()
```
Read the current date and time from the RTC at 1 second intervals:
```
while (True):
  print rtc.read_date()
  time.sleep(1)
```
