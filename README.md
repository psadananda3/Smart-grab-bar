Smart-grab-bar
==============

arduino code, python codes to visualise and plot data

** smartbath.ino is the Arduino code. It is a simple serial read code that just prints the analog outputs from each of the four sensors: 2 Softpots and 2 pressure sensors.

** newserialpy.py is used to visualise the sensor readings in real time and save the data in a text file. In the code, it is necessary to specify the serial port and filename before running. (Modify lines 50 and 74)

** plotcode.py is used to plot the sensor data from the saved text file. The filename needs to be modified before running. (Modify line 8)

