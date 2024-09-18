
import unittest
from tile import Tile

class TestTile(unittest.TestCase):
	def setUp(self):
		self.tile = Tile(0, 0)

	def test_init(self):
		self.assertEqual(self.tile.x, 0)
		self.assertEqual(self.tile.y, 0)
		self.assertFalse(self.tile.revealed)
		self.assertFalse(self.tile.flagged)
		self.assertFalse(self.tile.mine)
		self.assertEqual(self.tile.adjacent_mines, 0)

	def test_reveal(self):
		self.tile.reveal()
		self.assertTrue(self.tile.revealed)

	def test_flag(self):
		self.tile.flag()
		self.assertTrue(self.tile.flagged)

	def test_unflag(self):
		self.tile.flag()
		self.tile.flag()
		self.assertFalse(self.tile.flagged)

	def test_is_revealed(self):
		self.assertFalse(self.tile.is_revealed())
		self.tile.reveal()
		self.assertTrue(self.tile.is_revealed())

	def test_is_flagged(self):
		self.assertFalse(self.tile.is_flagged())
		self.tile.flag()
		self.assertTrue(self.tile.is_flagged())

	def test_set_mine(self):
		self.tile.set_mine()
		self.assertTrue(self.tile.mine)

	def test_is_mine(self):
		self.assertFalse(self.tile.is_mine())
		self.tile.set_mine()
		self.assertTrue(self.tile.is_mine())

	def test_set_adjacent_mines(self):
		self.tile.set_adjacent_mines(5)
		self.assertEqual(self.tile.adjacent_mines, 5)

	def test_get_display_symbol(self):
		self.assertEqual(self.tile.get_display_symbol(), ' ')
		self.tile.reveal()
		self.assertEqual(self.tile.get_display_symbol(), '0')
		self.tile.set_adjacent_mines(1)
		self.assertEqual(self.tile.get_display_symbol(), '1')
		self.tile.flag()
		self.assertEqual(self.tile.get_display_symbol(), 'F')
		self.tile.set_mine()
		self.assertEqual(self.tile.get_display_symbol(), '*')

if __name__ == '__main__':
	unittest.main()
