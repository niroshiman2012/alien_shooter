# Author : Niroshiman

import pygame
import sys
from cloud import Cloud
from alien import Alien
from bullet import Bullet

def check_events(ai_settings,screen,ship,bullets):
	"""Respond to keypresses and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ship,ai_settings,screen,bullets)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)


def check_keydown_events(event,ship,ai_settings,screen,bullets):
	"""Respond to key presses."""
	if event.key == pygame.K_UP:
		# Move the ship to the right
		ship.moving_up = True

	elif event.key == pygame.K_DOWN:
		# Move the ship to the left
		ship.moving_down = True

	elif event.key == pygame.K_SPACE:
		# Create bullets
		bullet = Bullet(ai_settings,screen,ship)
		bullets.add(bullet)
		bullets.draw_bullet()

	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_events(event,ship):
	"""Respond to key release."""
	if event.key == pygame.K_UP:
		# Stop the ship to the right
		ship.moving_up = False

	elif event.key == pygame.K_DOWN:
		# Stop the ship to the left
		ship.moving_down = False

def create_cloud(screen,clouds):
	"""Create a cloud and place it in the screen."""
	if len(clouds) < 6:
		cloud = Cloud(screen)
		clouds.add(cloud)

def update_clouds(screen,clouds):
	"""Update position of clouds and get rid of old ones."""
	clouds.update()

	# Get rid of clouds that have disappeared
	for cloud in clouds.copy():
		if cloud.rect.right < 0:
			clouds.remove(cloud)

def create_aliens(screen,aliens,city):
	"""Create aliens place it in the screen."""
	# Create alien after city object has moved out of frame.
	if len(aliens) < 3 and city.rect.right < 0:
		alien = Alien(screen)
		aliens.add(alien)

def update_aliens(screen,aliens,ship):
	"""Update position of clouds and get rid of old ones."""
	aliens.update()

	# Get rid of clouds that have disappeared
	for alien in aliens.copy():
		if alien.rect.right < 0:
			aliens.remove(alien)

		if pygame.sprite.collide_rect(ship,alien):
			aliens.remove(alien)
		



