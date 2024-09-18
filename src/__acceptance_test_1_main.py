
import unittest
from unittest.mock import patch
from io import StringIO
from main import Main

class TestMinesweeper(unittest.TestCase):
    @patch('builtins.input', side_effect=['reveal 0 0', 'reveal 0 1', 'reveal 0 2', 'reveal 1 0', 'reveal 1 1', 'reveal 1 2', 
                                          'reveal 2 0', 'reveal 2 1', 'reveal 2 2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_game_win(self, mock_stdout, mock_input):
        game = Main()
        game.run()
        self.assertTrue("Congratulations, you have won!" in mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()
