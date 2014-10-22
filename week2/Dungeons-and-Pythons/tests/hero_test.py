import unittest

import sys
sys.path.insert(0, '../')

from hero import Hero


class HeroTest(unittest.TestCase):

    def setUp(self):
        self.shosh_hero = Hero('Shosh', 100, 'GraveRobber')

    def test_hero_known_as(self):
        self.assertEqual(self.shosh_hero.known_as(), 'Shosh the GraveRobber')


if __name__ == '__main__':
    unittest.main()
