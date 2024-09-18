
import unittest
from unittest.mock import patch
from main import Main

class TestMinesweeper(unittest.TestCase):
    @patch('builtins.input', side_effect=['reveal 0 0'])
    def test_game_loss(self, mock_input):
        game = Main()

        # Mock a mine at the initial position (0, 0)
        game.board.board[0][0].set_mine()

        # Run the game
        game.run()

        # Since the initial move revealed a mine, the game should be over
        self.assertTrue(game.board.is_game_over())
        self.assertFalse(game.board.is_game_won())

if __name__ == "__main__":
    unittest.main()
