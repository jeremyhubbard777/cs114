import sys
from time import sleep
from bullet import Bullet
from boss import Boss
import pygame

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()

def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
def check_events(ai_settings,screen,stats,play_button,ship,bullets):
	"""Respond to keypresses and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings,screen,stats,play_button,ship,bullets,mouse_x,mouse_y)
		
def check_play_button(ai_settings,screen,stats,play_button,ship,bullets,mouse_x,mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active: 
        # Hide the mouse cursor
        pygame.mouse.set_visible(False)
        # Reset the game statistics
        stats.reset_stats() 
        stats.game_active = True
        #empty the list of bullets
        bullets.empty()
        # Create a new fleet and center the ship
        ship.center_ship()


def  fire_bullet(ai_settings,screen,ship,bullets):
	"""fires as bullet"""
	if len(bullets) < ai_settings.bullets_allowed:
			new_bullet = Bullet(ai_settings,screen,ship)
			bullets.add(new_bullet)


def create_boss(ai_settings,screen,boss):
	"""create an alien and place it in the row"""
	boss = Boss(ai_settings,screen)
	boss_width = boss.rect.width
	boss.x = boss_width
	boss.rect.x = boss.x
	boss.rect.y = boss.rect.height
	boss.add(boss)
    
def check_boss_edges(ai_settings, boss):
    """Respond appropriately if any aliens have reached an edge."""
    if boss.check_edges():
        ai_settings.boss_direction *= -1

def update_bullets(ai_settings,screen,ship,bullets):
	"""updates the position and gets rid of old bullets"""
	#update the bullet position
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def update_boss(ai_settings, screen, ship, boss, bullets):
	"""Update the postions of the boss."""
	check_boss_edges(ai_settings, boss)
	boss.update()
	
    
def update_screen(ai_settings,screen,stats,ship,boss,bullets,play_button):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    boss.blitme()
    # Draw the play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button() 

    # Make the most recently drawn screen visible.
    pygame.display.flip()