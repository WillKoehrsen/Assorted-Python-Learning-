import random

class Blob:
	# methods look and act like functions
	# dunder-init method, runs whenever an instance of a class is created
	def __init__(self, color, x_boundary = 800, y_boundary = 600, size_range = (4,8), movement_range = (-1, 2)):
		self.size = random.randrange(size_range[0], size_range[1])
		self.color = color
		self.x_boundary = x_boundary
		self.y_boundary = y_boundary
		self.x = random.randrange(0, self.x_boundary)
		self.y = random.randrange(0, self.y_boundary)
		self.size_range = size_range
		self.movement_range = movement_range

	def move(self):
		self.move_x = random.randrange(self.movement_range[0], self.movement_range[1])
		self.move_y = random.randrange(self.movement_range[0], self.movement_range[1])
		self.x += self.move_x
		self.y += self.move_y

	def move_fast(self):
		self.x += random.randrange(-8, 8)
		self.y += random.randrange(-8, 8)
	# impose as little as possible on user
	# allow user to check if bounds have been exceeded
	def check_bounds(self):
		if self.x < 0: self.x = 0
		elif self.x > self.x_boundary: self.x = self.x_boundary

		if self.y < 0: self.y = 0
		elif self.y > self.y_boundary: self.y = self.y_boundary