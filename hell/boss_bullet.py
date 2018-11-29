import pygame
from pygame.sprite import Sprite

class Boss_bullet(Sprite):
    
	def __init__(self, ai_settings, screen, boss):
		super(Boss_bullet, self).__init__()
		self.screen = screen
		
		self.rect = pygame.Rect(0,0,ai_settings.boss_bullet_width, ai_settings.boss_bullet_height)
		self.rect.centerx = boss.rect.centerx
		self.rect.top = boss.rect.bottom
		
		self.y = float(self.rect.y)
		
		self.color = ai_settings.boss_bullet_color
		self.speed_factor = ai_settings.boss_bullet_speed_factor
		
	def update(self):
		self.y += self.speed_factor
		self.rect.y= self.y
		
	def draw_bullet(self):
		pygame.draw.rect(self.screen,self.color,self.rect)