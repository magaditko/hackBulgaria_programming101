import unittest

import sys
sys.path.insert(0, '../')

from dungeon import Dungeon


class DungeonTest(unittest.TestCase):

    def setUp(self):
        self.dungeon = Dungeon('dungeon.txt')

    def test_init(self):
        self.assertEqual('dungeon.txt', self.dungeon.path)
        self.dungeon.print_map()


if __name__ == '__main__':
    unittest.main()
