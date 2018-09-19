import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class for one alien"""
	
	def __init__(self,ai_settings,screen):
		"""initializes the aliena and sets its starting positon"""
		super(Alien,self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		#load the alien image and set its rect attribute
		self.image = pygame.image.load('images/worm.bmp')
		self.rect = self.image.get_rect()
		
		
		#start each new alien near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#store the alien's exact position
		self.x = float(self.rect.x)
	def blitme(self):
		"""draw the alien at its current location"""
		self.screen.blit(self.image,self.rect)