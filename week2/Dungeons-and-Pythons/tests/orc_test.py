import unittest

import sys
sys.path.insert(0, '../')

from orc import Orc
from weapon import Weapon


class OrcTest(unittest.TestCase):

    def setUp(self):
        self.zaithan_orc = Orc('Zaithan', 200, 1.7)
        self.destroyer_weapon = Weapon('Destroyer Axe', 30, 0.7)

    def test_set_berserk_factor(self):
        self.shatterer_orc = Orc('Shatterer', 250, 30.3)
        self.assertEqual(self.shatterer_orc.berserk_factor, 2)

    def test_return_attack_with_weapon(self):
        self.zaithan_orc.equip_weapon(self.destroyer_weapon)
        self.assertIn(self.zaithan_orc.attack(), [51, 102])

    def test_return_attack_without_weapon(self):
        self.assertEqual(0, self.zaithan_orc.attack())


if __name__ == '__main__':
    unittest.main()
