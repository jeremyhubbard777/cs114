import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ui import Ui
from button import Button
from ship import Ship
from boss import Boss
import game_functions as gf

def run_game():
	
	# Initialize pygame, settings, and screen object.
	pygame.init()
	pygame.mixer.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Hell")
	# Set the games frame rate
	clock = pygame.time.Clock()
	#set up the sound channels
	channel1 = pygame.mixer.Channel(0)
	channel2 = pygame.mixer.Channel(1)
	shot = pygame.mixer.Sound('sounds/ship_shot.wav')
	hit = pygame.mixer.Sound('sounds/ship_hit.wav')
	boss_hit = pygame.mixer.Sound('sounds/boss_hit.wav')
	# Make a counter for the timed attackes
	ai_counter = 0
	# Make the Play button
	play_button = Button(ai_settings, screen, "Start") 
	# Make a ship and group of bullets and a group of boss bullets
	ship = Ship(ai_settings, screen)
	bullets = Group()
	boss_bullets = Group()
	# Make a boss.
	boss = Boss(ai_settings, screen)
	# Create an instance to store game statistics and the ui
	stats = GameStats(ai_settings)
	ui = Ui(ai_settings,screen,stats)
	# Start the main loop for the game.
	while True:
		gf.check_events(ai_settings,screen,stats,play_button,ship,bullets,shot)
		
		if stats.game_active and ai_settings.boss_health > 0:
			if ai_settings.boss_health == 700 and not ship.second_stage:
				gf.start_stage2(ai_settings,boss,ship)
			clock.tick(60)
			ai_counter = gf.update_counter(ai_counter)
			gf.update_boss_ai(ai_settings,screen,boss,boss_bullets,ai_counter,ship)
			ship.update()
			gf.update_bullets(ai_settings,screen,ship,boss,bullets,boss_hit)		
			gf.update_boss(ai_settings,ai_counter, screen, ship, boss, bullets)
			gf.update_boss_bullets(ai_settings, stats, screen, ship, boss, bullets, boss_bullets,hit)

		gf.update_screen(ai_settings,screen,stats,ship,boss,boss_bullets,bullets,play_button,ui)

run_game()