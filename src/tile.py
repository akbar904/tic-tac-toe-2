
class Tile:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.revealed = False
		self.flagged = False
		self.mine = False
		self.adjacent_mines = 0

	def reveal(self):
		if not self.flagged:
			self.revealed = True

	def flag(self):
		self.flagged = not self.flagged

	def is_revealed(self):
		return self.revealed

	def is_flagged(self):
		return self.flagged

	def set_mine(self):
		self.mine = True

	def is_mine(self):
		return self.mine

	def set_adjacent_mines(self, count):
		self.adjacent_mines = count

	def get_display_symbol(self):
		if self.flagged:
			return 'F'
		elif self.revealed:
			if self.mine:
				return '*'
			else:
				return str(self.adjacent_mines)
		else:
			return ' '
