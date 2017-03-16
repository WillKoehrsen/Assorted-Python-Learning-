import os

names = ['Glen', 'Paul', 'Gary', 'Martha', 'Millie', 'Teresa']

for name in names:
	#print('Have a great day, ' + name)
	print(' '.join(['Have a great day', name]))  # performance gains using join

#print(' , '.join(names))

# [print(name) for name in names]

location_of_file = 'C:\\Users\\Will Koehrsen\\Python3.6\\PP3.6'
file_name = 'string_examples.txt'

# print(location_of_file + '\\' + file_name)


# correct way to join a path for opening a file
with open(os.path.join(location_of_file, file_name), 'r+') as f:
	print(f.read())
	

who = 'Glen'
how_many = 16

print(who, 'bought', how_many, 'oranges today?')  # easy way to do string formatting
print('%s bought %s oranges today?' % (who, how_many)) # easy way to do string formatting
print('{} bought {} oranges today?'.format(who, how_many)) # correct way to do string formatting


