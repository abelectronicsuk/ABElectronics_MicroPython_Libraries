AB Electronics UK MicroPython Libraries
=====

MicroPython Libraries to use the Raspberry Pi expansion boards from https://www.abelectronics.co.uk with the Raspberry Pi Pico development board.

### Downloading and Installing the library

To download to your Raspberry Pi type in the terminal: 

```
git clone https://github.com/abelectronicsuk/ABElectronics_MicroPython_Libraries.git
```

To install the MicroPython Library use the Thonny Python IDE from https://thonny.org/

Create a file for your chosen board and copy the contents of the python file into that board's directory. For example for the ADC DAC Pi create a new file in Thonny called ADCDACPi.py and copy contents from  ADCDACPi.py into the new file and save it onto the Raspberry Pi Pico board.

Create a second file where your main program will reside and import the board library at the top of the program.  

For example:  

```
from ADCDACPi import ADCDACPi
```

Run with **"Run Current Command"** or **F5** in Thonny.  

---

### ADCDACPi
This directory contains ADC DAC Pi MicroPython Library with ADC read and DAC write demos to use with the [ADC DAC Pi](https://www.abelectronics.co.uk/p/74/adc-dac-pi-zero-raspberry-pi-adc-and-dac-expansion-board)

---
### ADCPi 
This directory contains ADC Pi MicroPython Library  and a read voltage demo to use with the [ADC Pi](https://www.abelectronics.co.uk/p/69/adc-pi-raspberry-pi-analogue-to-digital-converter)

---
### ADCDifferentialPi 
This directory contains ADC Differential Pi MicroPython Library and a read voltage demo to use with the [ADC Differential Pi](https://www.abelectronics.co.uk/p/65/adc-differential-pi-raspberry-pi-analogue-to-digital-converter)  
This library is also compatible with the [Delta-Sigma Pi](https://www.abelectronics.co.uk/kb/article/1041/delta-sigma-pi)

---
### I2C Switch  
This directory contains the I2C Switch MicroPython Library and a demo to use with the 4-channel [I2C switch](https://www.abelectronics.co.uk/p/84/i2c-switch)  

---
### IOPi
This directory contains IO Pi MicroPython Library and demos to use with the [IO Pi Plus](https://www.abelectronics.co.uk/p/54/io-pi-plus)

---
### IOZero32
This directory contains IO Zero 32 MicroPython Library and demos to use with the [IO Zero 32](https://www.abelectronics.co.uk/p/86/io-zero-32)

---
### RTCPi
This directory contains RTC Pi MicroPython Library and demos to use with the [RTC Pi](https://www.abelectronics.co.uk/p/70/rtc-pi)  
