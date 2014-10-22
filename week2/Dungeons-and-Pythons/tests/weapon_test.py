import unittest

import sys
sys.path.insert(0, '../')

from weapon import Weapon


class WeaponTest(unittest.TestCase):

    def setUp(self):
        self.destroyer_weapon = Weapon('Destroyer Axe', 30, 0.7)

    def test_init_weapon(self):
        self.assertEqual(self.destroyer_weapon.type, 'Destroyer Axe')
        self.assertEqual(self.destroyer_weapon.damage, 30)
        self.assertEqual(self.destroyer_weapon.critical_strike_percent, 0.7)

    def test_critical_hit(self):
        result = []
        for x in range(1000):
            result.append(self.destroyer_weapon.critical_hit())
        self.assertIn(True, result)
        self.assertIn(False, result)

if __name__ == '__main__':
    unittest.main()
