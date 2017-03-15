from matplotlib import pyplot as plt
import math
import numpy
from pylab import *


x = [num * 0.1 for num in range(1,100)]
y =[]
y2 = []
theta = numpy.arange(0, 12 , 0.01)[1:]

def f(x):
	return 1/x

for num in x:
	y.append(math.sin(num))
	y2.append(math.cos(num))

plt.style.use('dark_background')
plt.figure(1)
plt.plot(x, y, x, y2)
plt.title('First Chart')
plt.xlabel('Time')
plt.ylabel('Consumption')
plt.figure(2)
plt.polar(theta, f(theta))
plt.axis([0,100, 0, 1.5])
plt.show()

