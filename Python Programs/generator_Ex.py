import timeit
for i in range(6): # is a generator, i not stored in memory
	print('Number: ', i)


xyz = [i for i in range(6)] # list comprehension

xyz = []
for i in range(6):
	xyz.append(i)

xyz = (i for i in range(6)) # generator object, not stored in memory, can still be iterated over
print(xyz)

print(timeit.timeit('''
xyz = (i for i in range(6))
a = [i ** 3 for i in xyz]
print(a)''', number = 200))
# generator takes longer to iterate over, but is not stored in memory
# with large generator: run out of time   (generators are not stored but are slower than list comprehension)
# with large list     : run out of memory (lists are stored in RAM)