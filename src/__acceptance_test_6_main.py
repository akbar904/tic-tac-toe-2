
import unittest
from unittest.mock import patch
from main import Main

class TestMinesweeper(unittest.TestCase):
	def test_scenario_7(self):
		user_inputs = ['flag 0 0', 'flag 0 1', 'flag 0 2', 'flag 0 3', 'flag 0 4', 'flag 0 5', 'flag 0 6', 'flag 0 7', 'flag 0 8', 
					   'flag 1 0', 'flag 1 1', 'flag 1 2', 'flag 1 3', 'flag 1 4', 'flag 1 5', 'flag 1 6', 'flag 1 7', 'flag 1 8', 
					   'flag 2 0', 'flag 2 1', 'flag 2 2', 'flag 2 3', 'flag 2 4', 'flag 2 5', 'flag 2 6', 'flag 2 7', 'flag 2 8', 
					   'flag 3 0', 'flag 3 1', 'flag 3 2', 'flag 3 3', 'flag 3 4', 'flag 3 5', 'flag 3 6', 'flag 3 7', 'flag 3 8', 
					   'flag 4 0', 'flag 4 1', 'flag 4 2', 'flag 4 3', 'flag 4 4', 'flag 4 5', 'flag 4 6', 'flag 4 7', 'flag 4 8',
					   'flag 5 0', 'flag 5 1', 'flag 5 2', 'flag 5 3', 'flag 5 4', 'flag 5 5', 'flag 5 6', 'flag 5 7', 'flag 5 8', 
					   'flag 6 0', 'flag 6 1', 'flag 6 2', 'flag 6 3', 'flag 6 4', 'flag 6 5', 'flag 6 6', 'flag 6 7', 'flag 6 8', 
					   'flag 7 0', 'flag 7 1', 'flag 7 2', 'flag 7 3', 'flag 7 4', 'flag 7 5', 'flag 7 6', 'flag 7 7', 'flag 7 8', 
					   'flag 8 0', 'flag 8 1', 'flag 8 2', 'flag 8 3', 'flag 8 4', 'flag 8 5', 'flag 8 6', 'flag 8 7', 'flag 8 8']

		with patch('builtins.input', side_effect=user_inputs):
			main = Main()
			main.run()
			self.assertTrue(main.board.is_game_over())

if __name__ == '__main__':
	unittest.main()
