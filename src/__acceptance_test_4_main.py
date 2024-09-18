
import unittest
from unittest.mock import patch
from main import Main

class AcceptanceTest(unittest.TestCase):
    @patch('builtins.input', side_effect=['flag 1 1', 'reveal 1 1'])
    @patch('main.Board.is_game_over', return_value=True)
    @patch('main.Board.is_game_won', return_value=False)
    @patch('main.Board.flag_tile')
    @patch('main.Board.reveal_tile')
    @patch('main.Board.display_board', return_value='')
    def test_scenario_5_incorrect_flag(self, mock_display, mock_reveal, mock_flag, mock_won, mock_over, mock_input):
        main = Main()
        main.run()
        mock_flag.assert_called_once_with(1, 1)
        mock_reveal.assert_called_once_with(1, 1)

if __name__ == '__main__':
    unittest.main()
