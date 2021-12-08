import pygame 

class Ship:
	""" Ship manipulation """

	def __init__(self, ai_game):
		""" Init ship. Set start position """

		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		# init ship image 
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		self.rect.midbottom = self.screen_rect.midbottom 


	def blitme(self):
		""" Draw ship in in position """
		self.screen.blit(self.image, self.rect)
