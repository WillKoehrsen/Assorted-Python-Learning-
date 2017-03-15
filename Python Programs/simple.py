def simple(num1,num2):
	pass

def simple(num1, num2 = 6):
	print(num1, num2)

def basic_window(width, height, font='TNR',
	bgc='w', scrollbar=True):
	print(width, height, font, bgc)

basic_window(500, 400, bgc='b')
