from random import randint


class Fight:

    def __init__(self, orc, hero):
        self.orc = orc
        self.hero = hero

    def flip_coin(self):
        coin = randint(0, 100)
        if coin < 50:
            return self.orc
        return self.hero

    
