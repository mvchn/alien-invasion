import sys

import pygame 

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
	"""Common class for game behaviour"""

	def __init__(self):
		"""Init game, create game resource"""

		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		
		# you can enable full-screen mode here
		#self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		#self.settings.screen_width = self.screen.get_rect().width
		#self.settings.screen_height = self.screen.get_rect().height

		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self._create_fleet()


	def run_game(self):
		""" Start main game cycle"""	
		while True:
			self._check_events()
			self.ship.update()
			self._update_bullets()
			self._update_aliens()
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
	    	    elif event.key == pygame.K_q:
	    	    	sys.exit()
	    	    elif event.key == pygame.K_SPACE:
	    	        self._fire_bullet()

	    	elif event.type == pygame.KEYUP:
	    	    if event.key == pygame.K_RIGHT:
	    	    	self.ship.moving_right = False
	    	    elif event.key == pygame.K_LEFT:
	    	    	self.ship.moving_left = False

	def _check_fleet_edges(self):
		""" Check if alien is get to the end of the screen """
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		""" Move fleet to another direction """
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1 	 		

	def _create_fleet(self):
		""" Create aliens fleet """

		# create aliens and calculate distanse between aliens 
		# distance between aliens is width of the alien
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_aliens_x = available_space_x // (2 * alien_width) 

		# check rows 
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
		number_rows = available_space_y // (2 * alien_height)

		# create aliens first row
		for row_number in range(number_rows):
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_number, row_number)
			

	def _create_alien(self, alien_number, row_number):
		""" Create alien and set to row """
		alien = Alien(self)
		alien_width = alien.rect.width
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		self.aliens.add(alien)

	def _fire_bullet(self):
		""" Create bullet and add it ti bullets group """
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_aliens(self):
		""" Refresh all aliens in fleet """
		self._check_fleet_edges()
		self.aliens.update()

		# find bullet and ship collision
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			print("Ship damage!!!")

	def _update_bullets(self):
		""" refreshg bullets positions """ 
		self.bullets.update()
		
		# remove bullets 
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)	

		self._check_bullet_alien_collisions()


	def _check_bullet_alien_collisions(self):
		""" Bullets and aliens reaction """
		# check if bullet marks to alien 
		collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

		if not self.aliens:
			# remove bullets and create new fleet
			self.bullets.empty()
			self._create_fleet()

	def _update_screen(self):
	    """ Update screen an check main scren """
	    self.screen.fill(self.settings.bg_color)
	    self.ship.blitme()
	    for bullet in self.bullets.sprites():
	    	bullet.draw_bullet()

	    self.aliens.draw(self.screen)
	    	
	    pygame.display.flip()


if __name__ == '__main__':
	# create instance and run the game 
	ai = AlienInvasion()
	ai.run_game()
