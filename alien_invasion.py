import sys

import pygame 

class AlienInvasion:
	"""Common class for game behaviour"""
	def __init__(self):
		"""Init game, create game resource"""
		pygame.init()

		self.screen = pygame.display.set_mode((1200, 800))
		pygame.display.set_caption("Alien Invasion")


	def run_game(self):
		"""Startm main game cycle"""	
		while True:
			# check mouse and keyboard
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

		# show last screen 
		pygame.display.flip()

if __name__ == '__main__':
	# create instance and run the game 
	ai = AlienInvasion()
	ai.run_game()
