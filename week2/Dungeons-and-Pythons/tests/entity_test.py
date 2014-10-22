import unittest

import sys
sys.path.insert(0, '../')

from hero import Hero
from orc import Orc
from weapon import Weapon


class EntityTest(unittest.TestCase):
    def setUp(self):
        self.shosh_hero = Hero('Shosh', 100, 'GraveRobber')
        self.zaithan_orc = Orc('Zaithan', 150, 0.5)
        self.destroyer_weapon = Weapon('Destroyer Axe', 30, 0.7)
        self.crystal_weapon = Weapon('Crystal Dagger', 15, 0.2)
        self.molten_weapon = Weapon('Molten Sword', 27, 0.4)

    def test_init(self):
        self.assertEqual(self.shosh_hero.name, 'Shosh')
        self.assertEqual(self.shosh_hero.health, 100)
        self.assertEqual(self.shosh_hero.nickname, 'GraveRobber')

    def test_get_health(self):
        self.assertEqual(self.shosh_hero.get_health(), 100)

    def test_is_alive(self):
        self.assertTrue(self.shosh_hero.is_alive())

    def test_is_dead(self):
        self.shosh_hero.health = 0
        self.assertFalse(self.shosh_hero.is_alive())

    def test_take_damage_integer_value(self):
        self.shosh_hero.take_damage(25)
        self.assertEqual(self.shosh_hero.get_health(), 75)

    def test_take_damage_decimal_value(self):
        self.shosh_hero.take_damage(0.5)
        self.assertEqual(self.shosh_hero.get_health(), 99.5)

    def test_take_huge_amount_of_damage(self):
        self.shosh_hero.take_damage(150)
        self.assertEqual(self.shosh_hero.get_health(), 0)

    def test_take_huge_amount_of_damage_decimal(self):
        self.shosh_hero.take_damage(120.5)
        self.assertEqual(self.shosh_hero.get_health(), 0)

    def test_take_healing_when_dead(self):
        self.shosh_hero.health = 0
        self.assertFalse(self.shosh_hero.take_healing(30))

    def test_take_hiper_super_big_healing(self):
        self.shosh_hero.health = 70
        self.assertTrue(self.shosh_hero.take_healing(200))
        self.assertEqual(self.shosh_hero.health, self.shosh_hero.get_health())

    def test_take_healing(self):
        self.shosh_hero.health = 20
        self.assertTrue(self.shosh_hero.take_healing(50))
        self.assertEqual(self.shosh_hero.health, 70)

    def test_has_weapon(self):
        self.zaithan_orc.weapon = None
        self.shosh_hero.weapon = self.crystal_weapon
        self.assertTrue(self.shosh_hero.has_weapon())
        self.assertFalse(self.zaithan_orc.has_weapon())

    def test_equip_weapon(self):
        self.shosh_hero.equip_weapon(self.destroyer_weapon)
        self.assertTrue(self.shosh_hero.has_weapon())
        self.assertEqual(self.shosh_hero.weapon.type, 'Destroyer Axe')

    def test_equip_weapon_and_discard_the_old_one(self):
        self.assertFalse(self.zaithan_orc.has_weapon())
        self.zaithan_orc.equip_weapon(self.crystal_weapon)
        self.assertTrue(self.zaithan_orc.has_weapon())
        self.assertEqual(self.zaithan_orc.weapon.type, 'Crystal Dagger')
        self.zaithan_orc.equip_weapon(self.molten_weapon)
        self.assertTrue(self.zaithan_orc.has_weapon())
        self.assertNotEqual(self.zaithan_orc.weapon.type, 'Crystal Dagger')
        self.assertEqual(self.zaithan_orc.weapon.type, 'Molten Sword')

    def test_attack_without_weapon(self):
        self.assertEqual(self.shosh_hero.attack(), 0)

    def test_attack_with_weapon(self):
        self.shosh_hero.equip_weapon(self.destroyer_weapon)
        self.assertIn(self.shosh_hero.attack(), [30, 60])

if __name__ == '__main__':
    unittest.main()
