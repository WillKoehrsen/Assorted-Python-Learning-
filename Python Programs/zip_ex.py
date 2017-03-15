x = [1, 2, 3, 4, 5, 6]
y = [8, 9, 10, 12, 15] # PEP8 convention is value, space 7, 8 for list declaration
z = ['a', 'b', 'c', 'd', 'e']

for a, b, c in zip(x, y, z):
	print(a, b, c)

print(zip(x,y,z)) # zip object

for i in zip(x,y,z):
	print(i)  # tuples

a = list(zip(x,y,z))
print(a[0][1])
# print(list(zip(x,y,z)))
# print(dict(zip(x,z)))

[print(a,b) for a,b in zip(x,y)]

print(x)


