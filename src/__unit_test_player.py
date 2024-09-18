
import unittest
from player import Player

class TestPlayer(unittest.TestCase):

	def setUp(self):
		self.player = Player()

	def test_init(self):
		self.assertIsNotNone(self.player)

	def test_get_move(self):
		# assuming get_move() method returns a tuple (x, y) for the move coordinates
		move = self.player.get_move()
		self.assertIsInstance(move, tuple)
		self.assertEqual(len(move), 2)

if __name__ == "__main__":
	unittest.main()
