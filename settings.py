class Settings:
	""" Game settings saving """

	def __init__(self):
		""" Init settings """

		# screeen settings 
		self.screen_width = 1200
		self.screen_height = 800
		self.ship_speed = 0.3
		self.bg_color = (0, 0, 255)

		# bullet settings
		self.bullet_speed = 1.5
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)

		self.bullets_allowed = 3

		self.alien_speed = 0.05
		self.fleet_drop_speed = 1

		# fleet_direction is way of movement. 1 - to the right, -1 - to the left
		self.fleet_direction = 1
