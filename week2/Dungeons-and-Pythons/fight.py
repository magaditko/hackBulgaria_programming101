from random import randrange


class Fight:

    def __init__(self, orc, hero):
        self.orc = orc
        self.hero = hero

    def flip_coin(self):
        coin = randrange(0, 100)
        if coin < 50:
            return self.orc
        else:
            return self.hero

    def check_for_weapons(self):
        if self.hero.has_weapon() or self.orc.has_weapon():
            return True
        else:
            return False

    def simulate_fight(self):
        if not self.check_for_weapons():
            return False

        attacker = self.flip_coin()
        if attacker == self.orc:
            attacked = self.hero
        else:
            attacked = self.orc

        while self.hero.is_alive() and self.orc.is_alive():
            damage = attacker.attack()
            attacked.take_damage(damage)

            attacker, attacked = attacked, attacker

        if attacker.is_alive():
            return attacker.name
        else:
            return attacked.name



