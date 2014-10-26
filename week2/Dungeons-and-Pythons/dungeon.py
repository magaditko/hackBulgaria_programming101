from hero import Hero
from orc import Orc


class Dungeon:

    def __init__(self, path):
        self.path = path
        self.dungeon = []
        self.set_dungeon()
        self.players = {}

    def set_dungeon(self):
        file = open(self.path)
        content = file.read().split('\n')

        for row in content:
            self.dungeon.append(list(row))
        self.dungeon.pop()

        file.close()

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
        next_pos = current
        if direction == 'left':
            next_pos[1] -= 1
        elif direction == 'right':
            next_pos[1] += 1
        elif direction == 'up':
            next_pos[0] -= 1
        elif direction == 'down':
            next_pos[0] += 1

        if next_pos[0] < 0 or next_pos[0] > len(self.dungeon) or next_pos[1] < 0 or next_pos[1] > len(self.dungeon[0]):
            return False
        else:
            return next_pos

    def move(self, player, direction):
        current_position = self.players[player][1]
        next_position = self.get_next_position(current_position, direction)
        if not next_position:
            return False
