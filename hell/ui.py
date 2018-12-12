import pygame.font
from pygame.sprite import Group
from ship import Ship
class Ui():
	"""A class to give relitive information."""
	
	def __init__(self, ai_settings, screen, stats):
		"""Initialize attributes."""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats
		# Font settings for ui information.
		self.font = pygame.font.SysFont(None, 48)
		
	def prep_ui(self):
		"""Turn the boss health into a rendered image."""
		self.text_color = self.ai_settings.ui_text_color
		boss_hp_str = str(self.ai_settings.boss_health)
		self.ui_image = self.font.render('HP ' + boss_hp_str, True, self.text_color,self.ai_settings.bg_color)
		# Display the score at the top right of the screen.
		self.ui_rect = self.ui_image.get_rect()
		self.ui_rect.right = self.ui_rect.right + 15
		self.ui_rect.top = 20
	
	def prep_ships(self):
		"""show how many ships are left"""
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.ai_settings, self.screen)
			ship.rect.x = 1150 - ship_number * ship.rect.width
			ship.rect.y = 650
			self.ships.add(ship)
			
	def show_ui(self):
		"""Draw score to the screen."""
		self.screen.blit(self.ui_image, self.ui_rect)
		# Draw ships
		self.ships.draw(self.screen)