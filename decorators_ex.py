from functools import wraps

def add_wrapping_with_style(style):
	def add_wrapping(item):
		@wraps(item) # allows the name to be displayed
		def wrapped_item():
			return 'An {} wrapped-up box of {}'.format(style, str(item()))
		return wrapped_item
	return add_wrapping
# decorators

@add_wrapping_with_style('intruiging')
def new_gpu():
	return 'A New Tesla P100 GPU?'

@add_wrapping_with_style('Practical')
def new_desk():
	return 'A new desk!'

print(new_gpu())
print(new_desk())
