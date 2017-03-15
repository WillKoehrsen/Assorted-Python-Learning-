'''
x = (i for i in range(6)) # generator expression

next(x)
next(x)

x.__next__()
x.__getattribute__('there')

for i in x:
	print(i)
'''

class range_examp:
	def __init__(self, end, step = 1):
		self.current = 0
		self.end = end
		self.step = step

	def __iter__(self):
		return self

	def __next__(self):
		if self.current >= self.end:
			raise StopIteration()
		else:
			return_val = self.current
			self.current += self.step
			return return_val



x = range_examp(6)

x.__next__()
next(x)

# for i in x:
#	print(i)

# print(dir(x))

def range_gen(end):
	current = 0
	while current < end:
		yield current
		current += 1

for i in range_gen(6):
	print(i)

x = range_gen(6)

x.__next__()

for i in x:
	print(i)

	
