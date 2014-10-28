import unittest

import sys
sys.path.insert(0, '../')

from dungeon import Dungeon
from hero import Hero
from orc import Orc
from weapon import Weapon


class DungeonTest(unittest.TestCase):

    def setUp(self):
        self.test_dungeon = Dungeon('dungeon.txt')
        self.sho_hero = Hero('Shosh', 100, 'GraveRobber')
        self.shatterer_orc = Orc('Shatterer', 100, 1.0)

    def test_init(self):
        self.assertEqual('dungeon.txt', self.test_dungeon.path)

    def test_find_spawn_points(self):
        self.assertEqual([(0, 0), (4, 9)], self.test_dungeon.find_spawn())

    def test_get_entity_type(self):
        self.assertEqual(self.test_dungeon.get_entity_type(self.sho_hero), 'H')
        self.assertEqual(self.test_dungeon.get_entity_type(self.shatterer_orc), 'O')

    def test_spawn(self):
    
        self.assertTrue(self.test_dungeon.spawn('player_1', self.sho_hero))
        self.assertEqual([(4, 9)], self.test_dungeon.find_spawn())
        self.assertTrue(self.test_dungeon.spawn('player_2', self.shatterer_orc))
        self.assertFalse(self.test_dungeon.find_spawn())

    def test_get_next_position(self):
        self.assertEqual(self.test_dungeon.get_next_position([0, 0], 'right'), [0, 1])

    def test_move_out_of_board(self):
        self.test_dungeon.players['player_1'] = [self.sho_hero, [0, 0]]
        self.assertFalse(self.test_dungeon.move('player_1', 'left'))

    def test_check_for_obstacle(self):
        self.assertFalse(self.test_dungeon.check_for_obstacle([0, 0]))
        self.assertTrue(self.test_dungeon.check_for_obstacle([1, 0]))
        
    def test_move(self):
        self.test_dungeon.players['player_1'] = [self.sho_hero, [0, 0]]
        self.assertFalse(self.test_dungeon.move('player_1', 'left'))
        self.test_dungeon.move('player_1', 'right')
        self.assertEqual(self.test_dungeon.dungeon[0][1], 'H')
        self.assertEqual(self.test_dungeon.dungeon[0][0], '.')

        self.assertEqual(self.test_dungeon.players['player_1'][1], [0, 1])
        self.test_dungeon.move('player_1', 'down')
        self.assertEqual(self.test_dungeon.players['player_1'][1], [1, 1])
        self.assertFalse(self.test_dungeon.move('player_1', 'right'))

    def test_set_weapons(self):
        self.assertEqual(self.test_dungeon.weapons[0].type, 'BigAxe')
        self.assertEqual(self.test_dungeon.weapons[1].type, 'SmallAxe')

if __name__ == '__main__':
    unittest.main()
