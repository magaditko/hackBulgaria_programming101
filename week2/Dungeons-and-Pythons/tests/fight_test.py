import unittest

import sys
sys.path.insert(0, '../')

from orc import Orc
from hero import Hero
from fight import Fight


class FightTest(unittest.TestCase):

    def setUp(self):
        self.zaithan_orc = Orc('Zaithan', 200, 1.7)
        self.shosh_hero = Hero('Shosh', 100, 'GraveRobber')
        self.fight = Fight(self.zaithan_orc, self.shosh_hero)

    def test_init(self):
        self.assertEqual(self.fight.orc, self.zaithan_orc)
        self.assertEqual(self.fight.hero, self.shosh_hero)

    def test_flip_coin(self):
        result = []
        for x in range(100):
            result.append(self.fight.flip_coin())
        self.assertIn(self.fight.orc, result)
        self.assertIn(self.fight.hero, result)


if __name__ == '__main__':
    unittest.main()
