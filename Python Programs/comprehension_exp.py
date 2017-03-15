input_list = [10, 20, 54, 76, 89, 34, 30, 45, 23]

def div_by_five(num):
	if num % 5 == 0:
		return True
	else:
		return False

xyz = (i for i in input_list if div_by_five(i))   # generator, not stored in memory as with list

print(xyz)  # will output generator object

# [print(i) for i in xyz]  # will print all the numbers that were divisible by 5

ex_list = []


#[ex_list.append(i) for i in xyz]
# xyz can only be iterated through once 

# after iterating through once, generator will be empty

for i in xyz:
	print(i)
	ex_list.append(i)

print(xyz) # generator is now empty

print(ex_list)

ex_array = [[[i, ii] for ii in range(6)] for i in range(6)]
print(ex_array)
print(len(ex_array[0][0]))

# with large generators: run out of time
# with large lists:      run out of memory

xyz = (print(i) for i in range(6))

for i in xyz: 
	(i) # will print out the numbers because each element of the generator is a print statement

