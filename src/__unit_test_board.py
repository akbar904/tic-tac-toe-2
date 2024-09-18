
import unittest
from board import Board

class TestBoard(unittest.TestCase):
	def setUp(self):
		self.board = Board(9, 9, 10)

	def test_init(self):
		self.assertEqual(self.board.rows, 9)
		self.assertEqual(self.board.cols, 9)
		self.assertEqual(self.board.mines, 10)

	def test_display_board(self):
		board_string = self.board.display_board()
		self.assertEqual(len(board_string.split('\n')), self.board.rows)

	def test_reveal_tile(self):
		self.assertTrue(self.board.reveal_tile(1, 1))

	def test_flag_tile(self):
		self.board.flag_tile(1, 1)
		tile = self.board.tiles[1][1]
		self.assertTrue(tile.is_flagged())

	def test_is_game_over(self):
		self.assertFalse(self.board.is_game_over())
		self.board.reveal_tile(1, 1)
		if self.board.tiles[1][1].is_mine():
			self.assertTrue(self.board.is_game_over())

	def test_is_game_won(self):
		self.assertFalse(self.board.is_game_won())
		for i in range(self.board.rows):
			for j in range(self.board.cols):
				if not self.board.tiles[i][j].is_mine():
					self.board.reveal_tile(i, j)
		self.assertTrue(self.board.is_game_won())

if __name__ == '__main__':
	unittest.main()
