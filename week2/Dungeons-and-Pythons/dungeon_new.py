import copy
from random import choice

from hero import Hero
from orc import Orc
from weapon import Weapon


class Dungeon:

    def __init__(self, path):
        self.path = path
        self.d_map = []
        self.mm = {}
        self.weapons = {}
        self.set_dungeon()
        self.players = {}

    def set_dungeon(self):
        file = open(self.path)
        content = file.read().split('\n')
        rn = 0

        for row in enumerate(content):
            if row[1] == '':
                rn = row[0]
                break
            self.d_map.append(list(row[1]))

        for row in enumerate(content):
            if row[1] == '':
                break
            for col in enumerate(row[1]):
                self.mm[(row[0], col[0])] = col[1]

        self.set_weapons(rn, content)
        file.close()

    def set_weapons(self, start_row, content):
        weapon = []
        for x in range(start_row, len(content)):
            if content[x] != '':
                weapon.append(content[x].split(' '))
        for w in weapon:
            self.weapons[w[0]] = {'details': Weapon(w[0], int(w[1]), float(w[2])), 'coordinates': []}

    def find_spawn(self):
        result = []
        for coord in self.mm:
            if self.mm[coord] == 'S':
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
        elif type(instance) == Weapon:
            return 'W'

    def spawn(self, player_name, entity):
        spawn_coordinates = self.find_spawn()
        player_letter = self.find_letter(entity)
        if player_name in self.players or not self.find_spawn():
            return False
        else:
            self.players[player_name] = {'details': entity, 'coordinates': spawn_coordinates}
            self.mm[spawn_coordinates] = player_letter
            return True
            


    
