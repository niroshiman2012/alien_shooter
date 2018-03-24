# Author : Niroshiman
import pygame
from pygame.sprite import Sprite
from random import randint

class City():
	"""A class to manage city background."""

	def __init__(self,screen):
		""" Initialize clouds sprite."""
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		
		# Load the cloud image and obtain its rect
		self.image = pygame.image.load('images/city.png')
		self.image.set_colorkey((255,255,255))
		self.rect = self.image.get_rect()

		# Start city at a fixed position
		self.rect.left = self.screen_rect.left
		self.rect.bottom = self.screen_rect.bottom

	def update(self):
		"""Update position of cloud."""
		self.rect.centerx -= 5

	def blitme(self):
		"""Draw the buller to the screen."""
		self.screen.blit(self.image,self.rect)

