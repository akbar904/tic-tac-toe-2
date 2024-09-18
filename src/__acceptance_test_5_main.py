
import unittest
from unittest.mock import patch
from main import Main

class TestMain(unittest.TestCase):
    @patch('builtins.input', side_effect=['flag 0 0', 'reveal 0 0'])
    @patch('main.print')
    def test_scenario_6(self, mock_print, mock_input):
        game = Main()
        game.run()
        self.assertTrue(game.board.is_game_over())

if __name__ == "__main__":
    unittest.main()
