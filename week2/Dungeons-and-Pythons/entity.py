class Entity:

    def __init__(self, name, health):
        self._MAX_HEALTH = health
        self.name = name
        self.health = health
        self.weapon = None

    def get_health(self):
        return self.health

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def take_damage(self, damage_points):
        if damage_points >= self.health:
            self.health = 0
        else:
            self.health -= damage_points

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False
        elif healing_points + self.health > self._MAX_HEALTH:
            self.health = self._MAX_HEALTH
        else:
            self.health += healing_points
        return True

    def has_weapon(self):
        if not self.weapon:
            return False
        return True

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if not self.has_weapon():
            return 0
        else:
            return self.weapon.damage

