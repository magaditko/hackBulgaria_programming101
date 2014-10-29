import copy
from random import choice

from hero import Hero
from orc import Orc
from weapon import Weapon


class Dungeon:

    def __init__(self, path):
        self.path = path
        self.dungeon = []
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
            self.dungeon.append(list(row[1]))

        self.set_weapons(rn, content)
        file.close()

    def set_weapons(self, start, content):
        weapon = []
        for x in range(start, len(content)):
            if content[x] != '':
                weapon.append(content[x].split(' '))
        for w in weapon:
            self.weapons[w[0]] = [Weapon(w[0], int(w[1]), float(w[2])), []]
                
    def print_map(self):
        for row in self.dungeon:
            for col in row:
                print(col, end = '')
            print()

    def find_spawn(self):
        result = []
        for row in enumerate(self.dungeon):
            if 'S' in row[1]:
                index_spawn = row[1].index('S')
                result.append((row[0], index_spawn))

        if result == []:
            return False
        else:
            return result

    def get_entity_type(self, entity):
        if isinstance(entity, Hero):
            return 'H'
        elif isinstance(entity, Orc):
            return 'O'

    def spawn(self, player, entity):
        spawn_points = self.find_spawn()
        if not spawn_points:
            return False
        else:
            x, y = spawn_points[0][0], spawn_points[0][1]
            self.players[player] = [entity, [x, y]]
            self.dungeon[x][y] = self.get_entity_type(entity)
            return True

    def get_next_position(self, current, direction):
        step = 1
        next_pos = copy.copy(current)
        if direction == 'left':
            next_pos[1] -= step
        elif direction == 'right':
            next_pos[1] += step
        elif direction == 'up':
            next_pos[0] -= step
        elif direction == 'down':
            next_pos[0] += step

        if next_pos[0] < 0 or next_pos[0] > len(self.dungeon) or next_pos[1] < 0 or next_pos[1] > len(self.dungeon[0]):
            return False
        else:
            return next_pos

    def check_for_obstacle(self, coordinates):
        x, y = coordinates[0], coordinates[1]
        if self.dungeon[x][y] == '#':
            return True
        else:
            return False

    def move(self, player, direction):

        current_position = self.players[player][1]
        next_position = self.get_next_position(current_position, direction)

        if not next_position:
            return False
        elif self.check_for_obstacle(next_position):
            return False
        else:
            if check_for_weapon(next_position)
            self.dungeon = self.modify_dungeon(current_position, '.')
            self.dungeon = self.modify_dungeon(next_position, self.get_entity_type(self.players[player][0]))
            
            self.players[player][1] = next_position

    def modify_dungeon(self, coordinates, value):
        dungeon = copy.deepcopy(self.dungeon)
        dungeon[coordinates[0]][coordinates[1]] = value
        return dungeon

    def spawn_weapons(self):
        free_spots = []
        for row in enumerate(self.dungeon):
            for col in enumerate(row[1]):
                if col[1] == '.':
                    free_spots.append([row[0], col[0]])

        for weapon in self.weapons:
            spawn_coordinates = choice(free_spots)
            self.weapons[weapon][1] = spawn_coordinates
            free_spots.remove(spawn_coordinates)
    
            self.dungeon = self.modify_dungeon(spawn_coordinates, 'W')
            
            

    # ToDo:
    # check for player
    # start new fight
    # check for weapon
