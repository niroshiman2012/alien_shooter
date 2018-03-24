# Author : Niroshiman
import pygame
from pygame.sprite import Sprite
from random import randint

class Building(Sprite):
	"""A class to manage builings."""
	def __init__(self,screen):
		"""Initialize the building class."""
		super(Building,self).__init__()
		self.screen = screen