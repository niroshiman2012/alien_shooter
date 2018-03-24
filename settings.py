# Author : Niroshiman

class Settings():

	def __init__(self):
		"""Initialize game settings."""
		# Ship settings
		self.ship_speed_factor = 8

			#---Bullet settings.
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 0,0,0
		self.bullets_allowed = 3