import timeit
example = ['up' , 'down', 'right', 'left']


for i in range(len(example)):
	print(i, example[i])


for i, j in enumerate(example):
	print(i, j)

new_dict = dict(enumerate(example))

print(new_dict)

[print(key, new_dict[key]) for key in (new_dict)]