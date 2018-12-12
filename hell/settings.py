class Settings():
	def __init__(self):
		"""Initialize the game's static settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 700
		self.bg_color = (0, 0, 0)
		self.ui_text_color = (255, 255, 255)
		# Ship settings
		self.ship_default_speed = 13
		self.ship_speed_factor = 13
		self.ship_slow_speed = 2.7
		self.ship_limit = 3

		#bullet settings
		self.bullet_speed_factor = 10
		self.bullet_width = 15
		self.bullet_height = 35
		self.bullet_color = 250, 0, 0
		self.bullets_allowed = 20
		self.bullet_dmg = 100

		# boss stage 1 settings
		self.boss_speed_factor = 10
		self.boss_direction = 1
		self.boss_health = 6000
		self.boss_health_default = 6000

		#boss bullet settings
		self.boss_bullet_speed_factorD = 5
		self.boss_bullet_speed_factor = 5
		self.boss_bullet_width = 25
		self.boss_bullet_height = 50
		self.boss_bullet_color = 255, 255, 255