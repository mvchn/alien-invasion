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


	def run_game(self):
		""" Start main game cycle"""	
		while True:
			self._check_events()
			self.ship.update()
			self._update_screen()


	def _check_events(self):
	    """ Check mouse and keyboard """
	    for event in pygame.event.get():
	    	if event.type == pygame.QUIT:
	    		sys.exit()
	    	elif event.type == pygame.KEYDOWN:
	    	    if event.key == pygame.K_RIGHT:
	    	    	self.ship.moving_right = True
	    	    elif event.key == pygame.K_LEFT:
	    	    	self.ship.moving_left = True
	    	elif event.type == pygame.KEYUP:
	    	    if event.key == pygame.K_RIGHT:
	    	    	self.ship.moving_right = False
	    	    elif event.key == pygame.K_LEFT:
	    	    	self.ship.moving_left = False

	def _update_screen(self):
	    """ Update screen an check main scren """
	    self.screen.fill(self.settings.bg_color)
	    self.ship.blitme()

	    pygame.display.flip()

if __name__ == '__main__':
	# create instance and run the game 
	ai = AlienInvasion()
	ai.run_game()
