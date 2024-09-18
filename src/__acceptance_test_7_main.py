
import unittest
from unittest.mock import patch
from main import Main


class TestMinesweeper(unittest.TestCase):
    def setUp(self):
        self.game = Main()

    @patch('builtins.input', side_effect=['reveal 0 0', 'reveal 0 1', 'reveal 0 2', 'reveal 0 3', 'reveal 0 4',
                                          'reveal 1 0', 'reveal 1 1', 'reveal 1 2', 'reveal 1 3', 'reveal 1 4',
                                          'reveal 2 0', 'reveal 2 1', 'reveal 2 2', 'reveal 2 3', 'reveal 2 4',
                                          'reveal 3 0', 'reveal 3 1', 'reveal 3 2', 'reveal 3 3', 'reveal 3 4',
                                          'reveal 4 0', 'reveal 4 1', 'reveal 4 2', 'reveal 4 3', 'reveal 4 4'])
    def test_uncover_all_squares(self):
        self.game.run()


if __name__ == '__main__':
    unittest.main()
