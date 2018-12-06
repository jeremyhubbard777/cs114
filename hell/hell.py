import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from boss import Boss
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Hell")
    # Set the games frame rate
    clock = pygame.time.Clock()
    # Make a counter for the timed attackes
    ai_counter = 0
    # Make the Play button
    play_button = Button(ai_settings, screen, "start") 

    # Make a ship and group of bullets and a group of boss bullets
    ship = Ship(ai_settings, screen)
    bullets = Group()
    boss_bullets = Group()
    # Make a boss.
    boss = Boss(ai_settings, screen)
    # Create an instance to store game statistics
    stats = GameStats(ai_settings)
    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings,screen,stats,play_button,ship,bullets)
        
        if stats.game_active and ai_settings.boss_health > 0:
            clock.tick(60)
            ai_counter = gf.update_counter(ai_counter)
            gf.update_boss_ai(ai_settings,screen,boss,boss_bullets,ai_counter)
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,boss,bullets)		
            gf.update_boss(ai_settings,ai_counter, screen, ship, boss, bullets)
            gf.update_boss_bullets(ai_settings, stats, screen, ship, boss, bullets, boss_bullets)
        else:
            stats.game_active = False
            pygame.mouse.set_visible(True)
        gf.update_screen(ai_settings,screen,stats,ship,boss,boss_bullets,bullets,play_button)

run_game()