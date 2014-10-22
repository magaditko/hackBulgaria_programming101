class Dungeon:

    def __init__(self, path):
        self.path = path
        self.dungeon = []
        self.set_dungeon()

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
