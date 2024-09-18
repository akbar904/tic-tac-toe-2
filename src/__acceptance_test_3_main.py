
import unittest
from unittest.mock import patch
from main import Main

class GameTest(unittest.TestCase):
	def setUp(self):
		self.game = Main()

	# Test Scenario 4: Flag Mines
	@patch('builtins.input', side_effect=['flag 0 0', 'flag 0 1', 'flag 0 2', 'flag 0 3', 'flag 0 4', 'flag 0 5', 'flag 0 6', 'flag 0 7', 'flag 0 8', 'flag 1 0'])
	def test_flag_all_mines(self, input):
		self.game.run()
		self.assertTrue(self.game.board.is_game_won())

if __name__ == '__main__':
	unittest.main()
