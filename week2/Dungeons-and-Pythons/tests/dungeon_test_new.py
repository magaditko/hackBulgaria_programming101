import unittest
import copy

import sys
sys.path.insert(0, '../')

from dungeon_new import Dungeon
from hero import Hero
from orc import Orc
from weapon import Weapon


class DungeonTest(unittest.TestCase):

    def setUp(self):
        self.test_dungeon = Dungeon('dungeon.txt')
        self.t_hero = Hero('Shosh', 100, 'GraveRobber')
        self.t_orc = Orc('Shatterer', 100, 1.0)
        self.t_weapon = Weapon('Axe', 10, 0.1)

    def test_init(self):
        self.assertEqual('dungeon.txt', self.test_dungeon.path)

    def test_set_dungeon(self):
        small_dungeon = Dungeon('dungeon2.txt')
        self.assertEqual(small_dungeon.d_map, [['S','.','.','.','.','.','S']])
        print(self.test_dungeon.mm)

    def test_set_weapons(self):
        result = []
        for weapon in self.test_dungeon.weapons:
            result.append(weapon)
        self.assertIn('BigAxe', result)
        self.assertEqual(type(self.test_dungeon.weapons['BigAxe']['details']), Weapon)
        self.assertEqual(self.test_dungeon.weapons['BigAxe']['coordinates'], [])

    def test_find_spawn_points(self):
       
        self.assertEqual(self.test_dungeon.find_spawn(), [0, 0])

        self.test_dungeon.d_map = [['.', '#', '.', 'H', 'O', 'W']]
        self.assertFalse(self.test_dungeon.find_spawn())

    def test_find_instance_letter(self):
        self.assertEqual(self.test_dungeon.find_letter(self.t_hero), 'H')
        self.assertEqual(self.test_dungeon.find_letter(self.t_orc), 'O')
        self.assertEqual(self.test_dungeon.find_letter(self.t_weapon), 'W')

    def test_spawn(self):
        self.assertTrue(self.test_dungeon.spawn('player_1', self.t_hero))
        self.assertEqual(self.test_dungeon.players['player_1']['details'], self.t_hero)
        self.assertEqual(self.test_dungeon.players['player_1']['coordinates'], [0, 0])

        self.assertTrue(self.test_dungeon.spawn('player_2', self.t_orc))
        self.assertEqual(self.test_dungeon.players['player_2']['coordinates'], [4, 9])
        self.assertFalse(self.test_dungeon.spawn('player_1', self.t_orc))
        self.test_dungeon.d_map = ['.', '#']
        self.assertFalse(self.test_dungeon.find_spawn())
        self.assertFalse(self.test_dungeon.spawn('player2', self.t_orc))
        print(self.test_dungeon.players)

    def test_modify_dungeon(self):
        self.test_dungeon.modify_map([0, 3], 'Z')
        self.assertEqual(self.test_dungeon.d_map[0][3], 'Z')
        
if __name__ == '__main__':
    unittest.main()
