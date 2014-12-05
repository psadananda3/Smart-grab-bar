import numpy as np
import matplotlib.pyplot as plt

#with open("sensorpot.txt") as f:
 #   data = f.read()

#data = data.split('\n')
data=np.loadtxt("sensorpot.txt")

pot1=data[:,0]
pot2=data[:,1]
flex1=data[:,2]
flex2=data[:,3]

#print data


fig = plt.figure()

def plotsensor(ax,x):
	ax.set_xlabel('time')
	ax.set_ylabel('Sensor reading')
	ax.plot([0.25*i for i in range(0,len(x))],x, c='r', label='sensor reading',marker='.')

#SOFTPOT1
ax1 = fig.add_subplot(221)
ax1.set_title("Softpot1")  
plotsensor(ax1,pot1)  

#SOFTPOT2
ax1 = fig.add_subplot(222)
ax1.set_title("Softpot2")    
plotsensor(ax1,pot2)  

#FLEX1
ax1 = fig.add_subplot(223)
ax1.set_title("Flex1")    
plotsensor(ax1,flex1)  

#FLEX2
ax1 = fig.add_subplot(224)
ax1.set_title("Flex2")    
plotsensor(ax1,flex2)  
plt.show()

