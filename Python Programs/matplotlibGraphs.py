from matplotlib import pyplot as plt 
from matplotlib import style
import numpy
import math
import random


x = []
i = 0
while i < 100:
	x.append(100* random.random())
	i += 1

ysquare=[]
ysqrt=[]
for num in x:
	ysquare.append(num**2)
	ysqrt.append(math.sqrt(num))

style.use('seaborn-dark')
plt.bar(x,ysquare, label = 'squares')
plt.scatter(x, ysqrt, label = 'square root')
plt.xlabel('Independent Variable')
plt.ylabel('Dependent Variable')
plt.title('A minor improvement')
plt.grid(True)
plt.show()
