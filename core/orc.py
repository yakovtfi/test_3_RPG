import random

class Orc:
    def __init__(self, name):
        self.name = name
        self.type = "orc"
        self.hp = 50
        self.speed = random.randint(0, 5)
        self.power = random.randint(10, 15)
        self.armor_rating = random.randint(2, 8)
        self.weapon = random.choice(["knife", "sword", "axe"])

    def speak(self):
        print(f"The orc {self.name} growls!")

    def attack(self, target, roll_dice):
        roll = roll_dice(20) + self.speed
        print(f"{self.name} rolls 20 and gets {roll}")
        if roll > target.armor_rating:
            print(f"{self.name} hits {target.name}!")
            base_damage = roll_dice(6) + self.power
            if self.weapon == "knife":
                damage = base_damage * 0.5
            elif self.weapon == "sword":
                damage = base_damage * 1
            else:
                damage = base_damage * 1.5
            target.hp -= damage
            print(f"{target.name} takes {damage:.1f} damage, HP left: {target.hp}")
        else:
            print(f"{self.name} misses {target.name}!")

