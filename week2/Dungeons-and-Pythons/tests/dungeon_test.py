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
        self.t_orc = Orc('Shatterer', 100, 1)
        self.small = Dungeon('d_map_small.txt')

    def test_init(self):
        self.assertEqual('dungeon.txt', self.test_dungeon.path)

    def test_set_weapons(self):
        result = []
        for weapon in self.test_dungeon.weapons:
            result.append(weapon)
        self.assertIn('BigAxe', result)
        self.assertEqual(type(self.test_dungeon.weapons['BigAxe']['details']), Weapon)
        self.assertEqual(self.test_dungeon.weapons['BigAxe']['coordinates'], ())

    def test_find_spawn_points(self):
       
        self.assertEqual(self.test_dungeon.find_spawn(), (0, 0))

        no_spawn_dungeon = Dungeon('dungeon_no_spawn_points.txt')
        self.assertFalse(no_spawn_dungeon.find_spawn())

    def test_find_instance_letter(self):
        self.assertEqual(self.test_dungeon.find_letter(self.t_hero), 'H')
        self.assertEqual(self.test_dungeon.find_letter(self.t_orc), 'O')

    def test_spawn(self):
        self.assertTrue(self.test_dungeon.spawn('player_1', self.t_hero))
        self.assertEqual(self.test_dungeon.players['player_1']['details'], self.t_hero)
        self.assertEqual(self.test_dungeon.players['player_1']['coordinates'], (0, 0))

        self.assertTrue(self.test_dungeon.spawn('player_2', self.t_orc))
        self.assertEqual(self.test_dungeon.players['player_2']['coordinates'], (4, 9))
        self.assertFalse(self.test_dungeon.spawn('player_1', self.t_orc))
        self.test_dungeon.d_map = {(0, 0): '.', (0, 1): '#'}
        self.assertFalse(self.test_dungeon.find_spawn())
        self.assertFalse(self.test_dungeon.spawn('player2', self.t_orc))

    # def test_printing(self):
        # self.test_dungeon.print_map()
        # self.test_dungeon.spawn('Player_1', self.t_hero)
        # self.test_dungeon.print_map()
        # self.test_dungeon.spawn('Player_2', self.t_orc)
        # self.test_dungeon.print_map()
        # self.assertFalse(self.test_dungeon.spawn('Player_3', self.t_hero))

    # def test_find_possible_locations(self):
    #     print(self.test_dungeon.sp_weapons())

    def test_spawn_weapons(self):
        test = (0, 4)
        result = []
        
        for i in range(200):
            dungeon = copy.deepcopy(self.test_dungeon)
            dungeon.spawn_weapons()
            result.append(dungeon.weapons['BigAxe']['coordinates'])
        self.assertIn(test, result)

    def test_get_next_coordinates(self):
        self.assertEqual(self.small.get_next_coordinates((0, 0), 'down'), (1, 0))
        self.assertEqual(self.small.get_next_coordinates((0, 0), 'right'), (0, 1))
        self.assertFalse(self.small.get_next_coordinates((0, 0), 'up'))
        self.assertFalse(self.small.get_next_coordinates((0, 0), 'left'))

    def test_get_weapon_with_coordinates(self):
        self.small.weapons['Axe']['coordinates'] = (0, 2)
        self.small.weapons['Sword']['coordinates'] = (2, 4)
        self.assertEqual(self.small.get_weapon((0, 2)).type, 'Axe')
        self.assertNotEqual(self.small.get_weapon((2, 4)).type, 'Axe')

    def test_return_enemy(self):
        self.small.players = {'player_1': {'details': self.t_hero, 'coordinates': (0, 0)}, 'player_2': {'details': self.t_orc, 'coordinates': (0, 7)}}
        self.assertEqual(self.small.return_enemy((0, 7)), self.t_orc)
        self.assertNotEqual(self.small.return_enemy((0, 7)), self.t_hero)

    def test_return_self(self):
        self.small.players = {'player_1': {'details': self.t_hero, 'coordinates': (0, 0)}, 'player_2': {'details': self.t_orc, 'coordinates': (0, 7)}}
        self.assertEqual(self.small.return_self('player_2'), self.t_orc)

    def test_move_outside_map(self):
        self.small.players = {'player_1': {'details': self.t_hero, 'coordinates': (0, 0)}}
        self.assertFalse(self.small.move('player_1', 'left'))

    def test_move_obstacle(self):
        self.small.players = {'player_1': {'details': self.t_hero, 'coordinates': (0, 0)}}
        self.assertFalse(self.small.move('player_1', 'down'))

    def test_move_path(self):
        self.small.players = {'player_1': {'details': self.t_hero, 'coordinates': (0, 0)}, 'player_2': {'details': self.t_orc, 'coordinates': (0, 7)}}
        
        self.assertTrue(self.small.move('player_1', 'right'))
        self.assertEqual(self.small.d_map[(0, 0)], '.')
        self.assertEqual(self.small.d_map[(0, 1)], 'H')

    def test_move_weapon_case(self):
        self.small.players = {'player_1': {'details': self.t_hero, 'coordinates': (0, 1)}}
        self.small.weapons['Axe']['coordinates'] = (0, 2)
 
        self.small.d_map[(0, 2)] = 'W'

        self.assertTrue(self.small.move('player_1', 'right'))
        self.assertTrue(self.small.players['player_1']['details'].has_weapon())
        self.assertEqual(self.small.players['player_1']['details'].weapon, self.small.weapons['Axe']['details'])
        self.assertEqual(self.small.d_map[(0, 2)], 'H')
        self.assertEqual(self.small.d_map[(0, 1)], '.')

    def test_move_weapon_when_already_have_one(self):
        self.small.players = {'player_1': {'details': self.t_hero, 'coordinates': (0, 2)}}
        self.small.players['player_1']['details'].weapon = self.small.weapons['Axe']['details']
        self.small.weapons['Sword']['coordinates'] = (1, 2)

        self.small.d_map[(1, 2)] = 'W'

        self.assertTrue(self.small.players['player_1']['details'].has_weapon())
        self.assertEqual(self.small.players['player_1']['details'].weapon, self.small.weapons['Axe']['details'])
        self.assertEqual(self.small.d_map[(0, 2)], '.')
        self.assertEqual(self.small.d_map[(0, 1)], '.')

        self.assertTrue(self.small.move('player_1', 'down'))
        self.assertEqual(self.small.players['player_1']['details'].weapon, self.small.weapons['Sword']['details'])
        self.assertEqual(self.small.d_map[(1, 2)], 'H')
        self.assertEqual(self.small.d_map[(0, 2)], '.')

    def test_move_enemy_case(self):
        self.small.players = {'player_1': {'details': self.t_hero, 'coordinates': (1, 2)}, 'player_2': {'details': self.t_orc, 'coordinates': (1, 3)}}
        self.small.players['player_1']['details'].weapon = self.small.weapons['Axe']['details']
        self.small.players['player_2']['details'].weapon = self.small.weapons['Axe']['details']

        result = []
        for winner in range(100):
            self.small.players['player_1']['details'].health = 100
            self.small.players['player_2']['details'].health = 100
            result.append(self.small.enemy_case((1, 3), 'player_1'))

        self.assertIn('Shosh', result)
        self.assertIn('Shatterer', result)

        
        
        
        
        


        
if __name__ == '__main__':
    unittest.main()
