from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np 

print(style.available)
style.use('dark_background')

x , y = np.loadtxt('examplenum.csv',unpack=True, delimiter =',')

plt.plot(x,y)

plt.title('CSV data plotted')
plt.ylabel('Dependent Value')
plt.xlabel('Independent Value')

plt.grid(True)
plt.show()