import sys, serial
import numpy as np
from time import sleep
from collections import deque
from matplotlib import pyplot as plt
 
# class that holds analog data for N samples
class AnalogData:
	# constr
	def __init__(self, maxLen):
		self.ax = deque([0.0]*maxLen)
		self.maxLen = maxLen
 
	# ring buffer
	def addToBuf(self, buf, val):
		if len(buf) < self.maxLen:
			buf.append(val)
		else:
			buf.pop()
			buf.appendleft(val)
 
	# add data
	def add(self, data):
		self.addToBuf(self.ax, data)

		
# plot class
class AnalogPlot:
	# constr
	def __init__(self, analogData,i):
		# set plot to animated
		plt.subplot(2,2,i)
		plt.ion()
		self.axline, = plt.plot(analogData.ax,marker='o')
		plt.ylim([0, 1023])
		plt.show()
 
	# update plot
	def update(self, analogData):
		self.axline.set_ydata(analogData.ax)
		plt.draw()
 
# main() function
def main():
	x=[]
	analogData=[]
	analogPlot=[]

 
	strPort = '/dev/cu.usbmodem1421'
	#strPort = sys.argv[1];
	print range(0,3)
	# plot parameters
	plt.figure(1)
	for i in range(0,4):
		analogData.append(AnalogData(100))
		analogPlot.append(AnalogPlot(analogData[i],i+1))

 
	print 'plotting data...'
 
	# open serial port
	ser = serial.Serial(strPort, 9600)
	while True:
		try:
			line = ser.readline()
			data=[int(float(s)) for s in line.split()]
			if (len(data)==4):
				for i in range(0,4):
				 analogData[i].add(data[i])
				 plt.subplot(2,2,i+1)
				 analogPlot[i].update(analogData[i])
				 x.append(data)
				np.savetxt("/Users/pri/Desktop/coding/sensorpot.txt",x)   #name of file to save the sensor readings
		except KeyboardInterrupt:
			print 'exiting'
			break
	# close serial
	ser.flush()
	ser.close()
 
# call main
if __name__ == '__main__':
	main()
