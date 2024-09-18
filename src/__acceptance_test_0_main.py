
import unittest
from unittest.mock import patch
from main import Main

class TestMain(unittest.TestCase):

    @patch('builtins.input', return_value='reveal 1 1')
    @patch('builtins.print')
    def test_scenario1(self, mock_print, mock_input):
        game = Main()
        game.run()

        self.assertTrue(mock_print.called)
        self.assertTrue(mock_input.called)

if __name__ == '__main__':
    unittest.main()
