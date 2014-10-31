import copy
from random import choice

from hero import Hero
from orc import Orc
from weapon import Weapon
from fight import Fight


class Dungeon:

    def __init__(self, path):
        self.path = path
        self.d_map = {}
        self.weapons = {}
        self.set_dungeon()
        self.players = {}

    def set_dungeon(self):
        file = open(self.path)
        content = file.read().split('\n')
        row = 0

        for row in enumerate(content):
            if row[1] == '':
                row = row[0]
                break
            for col in enumerate(row[1]):
                self.d_map[(row[0], col[0])] = col[1]

        self.set_weapons(row, content)
        file.close()

    def set_weapons(self, start_row, content):
        weapon = []
        for x in range(start_row, len(content)):
            if content[x] != '':
                weapon.append(content[x].split(' '))
        for w in weapon:
            self.weapons[w[0]] = {'details': Weapon(w[0], int(w[1]), float(w[2])), 'coordinates': ()}

    def find_spawn(self):
        result = []
        for coord in self.d_map:
            if self.d_map[coord] == 'S':
                result = coord
                break
        if result:
            return result
        else:
            return False

    def find_letter(self, instance):
        if type(instance) == Hero:
            return 'H'
        elif type(instance) == Orc:
            return 'O'

    def spawn(self, player_name, entity):
        spawn_coordinates = self.find_spawn()
        player_letter = self.find_letter(entity)
        if player_name in self.players or not self.find_spawn():
            return False
        else:
            self.players[player_name] = {'details': entity, 'coordinates': spawn_coordinates}
            self.d_map[spawn_coordinates] = player_letter
            return True

    def print_map(self):
        coordinates = []
        for c in self.d_map:
            coordinates.append(c)
        coordinates.sort()
        col_count = 1
        for c in range(len(coordinates) - 1):
            if coordinates[c][0] == coordinates[c + 1][0]:
                col_count += 1
            else:
                break
                
        board = [coordinates[i: i + col_count] for i in range(0, len(coordinates), col_count)]

        for row in board:
            for col in row:
                print(self.d_map[col], end='')
            print()

    def sp_weapons(self):
        coordinates = []
        for k in self.d_map:
            if self.d_map[k] == '.':
                coordinates.append(k)
        return coordinates

    def spawn_weapons(self):
        sp_coordinates = self.sp_weapons()
        for weapon in self.weapons:
            coordinates = choice(sp_coordinates)
            self.weapons[weapon]['coordinates'] = coordinates
            self.d_map[coordinates] = 'W'
            sp_coordinates.remove(coordinates)

    def get_next_coordinates(self, current_coordinates, direction):
        next_coordinates = list(current_coordinates)
        if direction == 'right':
            next_coordinates[1] += 1
        elif direction == 'left':
            next_coordinates[1] -= 1
        elif direction == 'up':
            next_coordinates[0] -= 1
        elif direction == 'down':
            next_coordinates[0] += 1

        if tuple(next_coordinates) not in self.d_map:
            return False
        else:
            return tuple(next_coordinates)

    def get_weapon(self, coordinates):
        for weapon in self.weapons:
            if self.weapons[weapon]['coordinates'] == coordinates:
               return self.weapons[weapon]['details']

    def return_enemy(self, next_coordinates):
        for player in self.players:
            if self.players[player]['coordinates'] == next_coordinates:
                return self.players[player]['details']

    def return_self(self, player_name):
        return self.players[player_name]['details']

    def move(self, player_name, direction):
        p_current = self.players[player_name]['coordinates']
        p_letter = self.find_letter(self.players[player_name]['details'])
        p_next = self.get_next_coordinates(p_current, direction)
        
        enemy = lambda p_letter: 'O' if p_letter == 'H' else 'H'
        
        if not p_next:
            return False
        elif self.d_map[p_next] == '#':
            return False
        elif self.d_map[p_next] == '.':
            self.d_map[p_current] = '.'
            self.d_map[p_next] = p_letter
            self.players[player_name]['coordinates'] = p_next
            return True
        elif self.d_map[p_next] == 'W':
            self.weapon_case(player_name, p_next, p_current, p_letter)
            return True
        elif self.d_map[p_next] == enemy:
            self.enemy_case(p_next, player_name)
            
    def enemy_case(self, p_next, player_name):
        if type(self.return_self(player_name)) == Hero:
            second = self.return_self(player_name)
            first = self.return_enemy(p_next)
        else:
            second = self.return_enemy(p_next)
            first = self.return_self(player_name)

        print('Wild {} appeared!'.format(self.return_enemy(p_next)))
        print('FIGHT!')
        fight = Fight(first, second)
        winner = fight.simulate_fight()
        print('{} WINS!'.format(winner))
        return winner
        
    def weapon_case(self, player_name, p_next, p_current, p_letter):
        weapon = self.get_weapon(p_next)
        self.players[player_name]['details'].equip_weapon(weapon)
        self.d_map[p_current] = '.'
        self.d_map[p_next] = p_letter
        self.players[player_name]['coordinates'] = p_next
