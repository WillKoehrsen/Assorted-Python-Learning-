x = 5

def example():
	
	global x
	globx =  x
	x += 12
	print(x)
	return globx

x = example()