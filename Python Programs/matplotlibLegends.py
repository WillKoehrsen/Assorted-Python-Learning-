from matplotlib import pyplot as plt 
from matplotlib import style
import numpy
import math

print(style.available)


style.use('dark_background')

x = numpy.arange(0, 10, 0.01)

print(x)

ysin =[]
ycos = []

for num in x:
	ysin.append(math.sin(num))
	ycos.append(math.cos(num))

plt.plot(x , ysin, label = 'sin function')

plt.plot(x, ycos, label = 'cos function')

plt.title('This will do for now...')
plt.ylabel('Dependent Value')
plt.xlabel('Independent Value')
plt.legend()
plt.grid(True)
plt.show()