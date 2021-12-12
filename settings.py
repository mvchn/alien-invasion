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
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)

		self.bullets_allowed = 3
