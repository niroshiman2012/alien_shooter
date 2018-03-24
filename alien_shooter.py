# Author : Niroshiman
# Desc	 : A rocket that can move 4 ways through keyboard keydown event

import pygame
from pygame.sprite import Group
import sys
import game_functions as gf
from ship import Ship
from cloud import Cloud
from alien import Alien
from city import City
from settings import Settings

# RGB colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

def run_game():

	pygame.init()

	# Set screen width and height 255
	size = (800,650)
	screen = pygame.display.set_mode(size)
	sky = pygame.image.load('images/sky.png')
	city = City(screen)

	pygame.display.set_caption('Template')

	# Create object
	ai_settings = Settings()
	ship = Ship(screen,ai_settings)
	clouds = Group()
	aliens = Group()
	bullets = Group()

	clock = pygame.time.Clock()

	while True:
		# --- Main event loop

		# --- Game logic


		# --- Clearing the screen
		screen.blit(sky,(0,0))

		# --- Update the game
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update(ai_settings,screen)

		city.update()
		city.blitme()
		
		gf.create_cloud(screen,clouds)
		gf.update_clouds(screen,clouds)
		clouds.draw(screen)
		
		gf.create_aliens(screen,aliens,city)
		gf.update_aliens(screen,aliens,ship)
		aliens.draw(screen)

		bullets.draw(screen)

		ship.blitme()

		# --- Updating the screen
		pygame.display.flip()


		# --- Limit to 60 FPS
		clock.tick(60)

run_game()