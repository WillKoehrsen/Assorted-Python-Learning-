# exec: evaluates and compiles whatever is passed to it

exec("print('this works like eval but is more powerful')")

list_str = '[4,5,62,21,2,3]'

list_str = exec(list_str)

print(list_str)

exec("list_str2 = [3,5,1,2,12]")

print(list_str2)

exec("def test(): print('this is very powerful')")

test()

exec("""
def test2():
		print('does multi line work too?:\
 the answer appears to be definitely.')
		""")

test2()