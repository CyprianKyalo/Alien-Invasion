class GameStats:
	"""Track statistics for alien invasion"""
	def __init__(self, ai_game):
		"""Initialize statictics"""
		self.settings = ai_game.settings
		self.reset_stats()

		#Start Alien Invasion in an inactive state.
		self.game_active = False

	def reset_stats(self):
		"""Initialize statistics that can change """
		self.ships_left = self.settings.ship_limit
		self.score = 0