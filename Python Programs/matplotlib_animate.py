import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import time

fig = plt.figure()


def animate(i):
	ax1 = fig.add_subplot(1,1,1)
	pullData = open('sampleText.txt' , 'r').readlines()
	dataArray = [i.split('\n',1)[0] for i in pullData]
	dataArray = [i.split(',') for i in dataArray]
	print(dataArray)

	xar = []
	yar = []
	for eachLine in dataArray:
		if len(eachLine) > 1:
			x , y = eachLine.spilt(',')
			xar.append(int(x))
			yar.append(int(y))

	ax1.clear()
	ax1.plot(xar, yar)

ani = animation.FuncAnimation(fig, animate, interval = 1000)
plt.show()