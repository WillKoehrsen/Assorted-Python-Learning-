import random, pygame
from Blob_def import Blob

STARTING_RED_BLOBS = 4
STARTING_GREEN_BLOBS = 14
WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)  # I think this might be yellow

game_display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Blob World')
clock = pygame.time.Clock()

# one line of whitespace between functions
# two lines of whitespace between classes

# parent class (base class: a class that takes a class)
class GreenBlob(Blob):
	def __init__(self, x_boundary, y_boundary):
		super().__init__(self, x_boundary, y_boundary)
		self.color = GREEN # this overwrites the color passed in the child instantiation

class YellowBlob(Blob):
	def __init__(self, x_boundary, y_boundary):
		super().__init__(self, x_boundary, y_boundary)
		self.color = YELLOW


class RedBlob(Blob):
	def __init__(self, x_boundary, y_boundary):
		super().__init__(self, x_boundary, y_boundary)
		self.color = RED



def draw_environment(blob_list):
	game_display.fill(WHITE)
	for blob_dict in blob_list:
		for blob_id in blob_dict:
			blob = blob_dict[blob_id]
			pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
			# blob.move_fast()
			blob.move()
			blob.check_bounds() # let user make the decision, but include option in class
	
	pygame.display.update()

def main():
	green_blobs = dict(enumerate([GreenBlob(WIDTH, HEIGHT) for i in range(STARTING_GREEN_BLOBS)]))
	red_blobs = dict(enumerate([RedBlob(WIDTH, HEIGHT) for i in range(STARTING_RED_BLOBS)]))
	# print(green_blobs, red_blobs)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.QUIT
				quit()

		draw_environment([green_blobs, red_blobs])

		clock.tick(60) # update the environment at frames per second

# prevent script from running if imported into another script
if __name__=="__main__":
	main()
