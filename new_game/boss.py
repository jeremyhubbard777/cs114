import pygame
from pygame.sprite import Sprite

class Boss(Sprite):
    """A class to represent the boss."""
    def __init__(self, ai_settings, screen):
        """Initialize the boss and set its starting position."""
        super(Boss, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        
        # Load the boss image and set its rect attribute.
        self.image = pygame.image.load('images/boss1.bmp')
        self.rect = self.image.get_rect()
        
        # Start each the boss near the top left of the screen.
        self.rect.x = self.screen_rect.centerx - (self.rect.width/2)
        self.rect.y = self.screen_rect.top
        
        # Store the boss's exact position.
        self.x = float(self.rect.x)
    
    def update(self):
        """Move the boss right or left"""
        self.x += (self.ai_settings.boss_speed_factor * 
						self.ai_settings.boss_direction)
        self.rect.x = self.x


    def check_edges(self):
        """Return True if the boss is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= self.screen_rect.right:
            return True
        elif self.rect.left <= self.screen_rect.left:
            return True

    def blitme(self):
        """Draw the boss at its current location."""
        self.screen.blit(self.image, self.rect)