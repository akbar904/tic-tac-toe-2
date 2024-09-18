
from random import sample
from tile import Tile

class Board:
	def __init__(self, rows, cols, mines):
		self.rows = rows
		self.cols = cols
		self.mines = mines
		self.tiles = [[Tile(i, j) for j in range(cols)] for i in range(rows)]
		self.game_over = False
		self.game_won = False
		self.place_mines()

	def place_mines(self):
		mine_positions = sample([(i, j) for i in range(self.rows) for j in range(self.cols)], self.mines)
		for i, j in mine_positions:
			self.tiles[i][j].set_mine()

	def display_board(self):
		return '\n'.join([' '.join([tile.get_display_symbol() for tile in row]) for row in self.tiles])

	def reveal_tile(self, x, y):
		tile = self.tiles[x][y]
		if tile.is_mine():
			self.game_over = True
		else:
			tile.reveal()
		return not tile.is_mine()

	def flag_tile(self, x, y):
		self.tiles[x][y].flag()

	def is_game_over(self):
		return self.game_over

	def is_game_won(self):
		unrevealed_tiles = sum([sum([not tile.is_revealed() and not tile.is_mine() for tile in row]) for row in self.tiles])
		self.game_won = unrevealed_tiles == 0
		return self.game_won
