import sys

import pygame 

from settings import Settings
from ship import Ship

class AlienInvasion:
	"""Common class for game behaviour"""
	def __init__(self):
		"""Init game, create game resource"""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		
		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)


		# set game color 
		self.bg_color = (230, 230, 230)


	def run_game(self):
		"""Startm main game cycle"""	
		while True:
			# check mouse and keyboard
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			self.screen.fill(self.settings.bg_color)	
			self.ship.blitme()

			# show last screen 
			pygame.display.flip()

if __name__ == '__main__':
	# create instance and run the game 
	ai = AlienInvasion()
	ai.run_game()
