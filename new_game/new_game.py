import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
	# Initialize pygame, settings, and screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("New Game")

	# Make the Play button
	play_button = Button(ai_settings, screen, "Kill Your Self") 
	
	# Make a ship and group of bullets
	ship = Ship(ai_settings, screen)
	bullets = Group()
# Create an instance to store game statistics
	stats = GameStats(ai_settings)
# Start the main loop for the game.
	while True:
		gf.check_events(ai_settings,screen,stats,play_button,ship,bullets)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,ship,bullets)		
			
		gf.update_screen(ai_settings,screen,stats,ship,bullets,play_button)
		
run_game()