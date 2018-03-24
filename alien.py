# Author : Niroshiman
import pygame
from pygame.sprite import Sprite
from random import randint
import math

class Alien(Sprite):
	"""A class to manage clouds coming from random position."""

	def __init__(self,screen):
		""" Initialize clouds sprite."""
		super(Alien,self).__init__()
		self.screen = screen
		
		# Load the cloud image and obtain its rect
		self.image = pygame.image.load('images/alien.png').convert()
		self.image.set_colorkey((255,255,255))
		self.rect = self.image.get_rect()

		# Start cloud at a random y position
		y = randint(44,650)
		x = randint(900,2000)
		self.rect.bottom = y
		self.rect.centerx = x

		# vertical movement initial marker
		self.y_init = self.rect.centery
		self.x_rel = 0



	def update(self):
		"""Update position of cloud."""
		self.rect.centerx -= 10

		# Vertical movement follows a sine wave
		self.step = math.sin(math.radians(self.x_rel)) * 20
		self.x_rel += 10
		self.rect.centery = self.y_init + self.step


	
	def blitme(self):
		"""Draw the buller to the screen."""
		self.screen.blit(self.image,self.rect)
