import random


class Player:
    def __init__(self, name):
        self.name = name
        self.profession = random.choice(["warrior", "healer"])
        self.hp = 50 + (10 if self.profession == "healer" else 0)
        self.speed = random.randint(5, 10)
        self.power = random.randint(5, 10) + (2 if self.profession == "warrior" else 0)
        self.armor_rating = random.randint(5, 10)

    def speak(self):
        print(f"{self.name}: Ready for battle!")

    def attack(self, target, roll_dice):
        roll = roll_dice(20) + self.speed
        print(f"{self.name} rolls 20 and gets {roll}")
        if roll > target.armor_rating:
            print(f"{self.name} hits {target.name}!")
            damage = roll_dice(6) + self.power
            target.hp -= damage
            print(f"{target.name} takes {damage} damage, HP left: {target.hp}")
        else:
            print(f"{self.name} misses {target.name}!")
