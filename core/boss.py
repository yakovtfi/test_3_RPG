from core.orc import Orc

class Boss(Orc):
    def __init__(self, name):
        super().__init__(name)
        self.type = "boss"
        self.hp += 5
        self.speed += 5
        self.power += 5
        self.armor_rating += 5

    def attack(self, target, roll_dice):
        if self.hp <= 44:
            self.hp += 30
            print(f"{self.name} heals itself! HP is now up {self.hp}")
            return
        super().attack(target, roll_dice)