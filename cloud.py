# Author : Niroshiman
import pygame
from pygame.sprite import Sprite
from random import randint

class Cloud(Sprite):
	"""A class to manage clouds coming from random position."""

	def __init__(self,screen):
		""" Initialize clouds sprite."""
		super(Cloud,self).__init__()
		self.screen = screen
		
		# Load the cloud image and obtain its rect
		self.image = pygame.image.load('images/cloud.png')
		self.image.set_colorkey((0,0,0))
		self.rect = self.image.get_rect()

		# Start cloud at a random y position
		y = randint(44,650)
		x = randint(900,2000)
		self.rect.bottom = y
		self.rect.centerx = x

	def update(self):
		"""Update position of cloud."""
		self.rect.centerx -= 5

	def blitme(self):
		"""Draw the buller to the screen."""
		self.screen.blit(self.image,self.rect)

