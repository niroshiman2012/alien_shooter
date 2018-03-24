# Author : Niroshiman
import pygame

class Ship():

	def __init__(self,screen,ai_settings):
		"""Initialize the ship class."""
		self.screen = screen
		self.ai_settings = ai_settings
		self.image = pygame.image.load('images/ship.png').convert()
		self.image.set_colorkey((255,255,255))
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()

		self.rect.left = self.screen_rect.left + 20
		self.rect.centery = self.screen_rect.centery

		# Store a decimal value for the ship's vertical position.
		self.centery = float(self.rect.centery)

		# Movement flag
		self.moving_up = False
		self.moving_down = False

	def update(self,screen,ai_settings):
		"""Update the ship's position based on the movement flag."""
		# Update the ship's center value not the rect
		if self.moving_up and self.rect.top > self.screen_rect.top:
			self.centery -= self.ai_settings.ship_speed_factor

		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.centery += self.ai_settings.ship_speed_factor

		# Update rect object from self.center.
		self.rect.centery = self.centery

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image,self.rect)



