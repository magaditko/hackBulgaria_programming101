import unittest

import sys
sys.path.insert(0, '../')

from orc import Orc
from hero import Hero
from weapon import Weapon
from fight import Fight


class FightTest(unittest.TestCase):

    def setUp(self):
        self.zaithan_orc = Orc('Zaithan', 200, 1.7)
        self.shosh_hero = Hero('Shosh', 100, 'GraveRobber')

        self.fight = Fight(self.zaithan_orc, self.shosh_hero)

        self.destroyer_weapon = Weapon('Destroyer Axe', 20, 0.7)
        self.molten_weapon = Weapon('Molten Sword', 30, 0.4)

    def test_init(self):
        self.assertEqual(self.fight.orc, self.zaithan_orc)
        self.assertEqual(self.fight.hero, self.shosh_hero)

    def test_flip_coin(self):
        result = []
        for x in range(10):
            result.append(self.fight.flip_coin())
        self.assertIn(self.fight.orc, result)
        self.assertIn(self.fight.hero, result)

    def test_check_for_weapons(self):
        self.assertFalse(self.fight.check_for_weapons())
        self.fight.hero.equip_weapon(self.molten_weapon)
        self.assertTrue(self.fight.check_for_weapons())
        self.fight.orc.equip_weapon(self.destroyer_weapon)
        self.assertTrue(self.fight.check_for_weapons())

    def test_simulate_fight_without_weapons(self):
        self.assertFalse(self.fight.simulate_fight())

    def test_simulate_fight_equivalent_hero_and_orc(self):
        hero = Hero('Sho', 100, 'Asura')
        orc = Orc('Shat', 100, 1)
        hero.weapon = self.destroyer_weapon
        orc.weapon = self.destroyer_weapon
        fight = Fight(orc, hero)

        result = []
        for x in range(100):
            hero.health = 100
            orc.health = 100
            result.append(fight.simulate_fight())

        self.assertIn('Sho', result)
        self.assertIn('Shat', result)

if __name__ == '__main__':
    unittest.main()
