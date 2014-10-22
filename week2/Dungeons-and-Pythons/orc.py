from entity import Entity


class Orc(Entity):

    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        self.set_berserk_factor(berserk_factor)

    def set_berserk_factor(self, berserk_factor):
        if berserk_factor >= 1 and berserk_factor <= 2:
            self.berserk_factor = berserk_factor
        else:
            if berserk_factor < 1:
                self.berserk_factor = 1
            else:
                self.berserk_factor = 2

    def attack(self):
        if not self.weapon:
            return 0
        else:
            if self.weapon.critical_hit():
                return self.berserk_factor * self.weapon.damage * 2
            else:
                return self.berserk_factor * self.weapon.damage
