import random

x = [i for i in range(6)] # list comprehension

y = (i for i in range(6)) # generator: much quicker as not stored in memory


def simple_gen():
	yield 'Oh'
	yield 'hello'
	yield 'there'

for i in simple_gen():
	print(i)

ex_tuple = (1, 3, 6)

ex_list = []
for i in ex_tuple:
	ex_list.append(i)
c1 = random.randint(0, 100)
c2 = random.randint(0, 100)
c3 = random.randint(0, 100)
correct_combination = (c1, c2, c3)

'''
for c1 in range(100):
	for c2 in range(100):
		for c3 in range(100):
			if (c1, c2, c3) == correct_combination:
				print('Found the combo: {}' .format(correct_combination)) # string formatting
				break
'''

# own generator, saves memory because values are not stored in memory
# using the list, the number are stored in memory and break statement needs to be repeated
def combo_gen():
	for c1 in range(100):
		for c2 in range(100):
			for c3 in range(100):
				yield c1, c2, c3

for (c1, c2, c3) in combo_gen():
	if (c1, c2, c3) == correct_combination:
		print('Found the combination: {}'. format(correct_combination))
		break
	
