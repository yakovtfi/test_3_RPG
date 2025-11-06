import random

class Goblin:
    def __init__(self, name):
        self.name = name
        self.type = "goblin"
        self.hp = 20
        self.speed = random.randint(5, 10)
        self.power = random.randint(5, 10)
        self.armor_rating = 1
        self.weapon = random.choice(["knife", "sword", "axe"])

    def speak(self):
        print(f"The goblin {self.name} screeches!")

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


    def run_away(self, roll_dice):
        if self.hp < 10:
            if random.randint(1, 100) <= 30:
                print(f"{self.name} attempts to flee!")
                roll = roll_dice(20) + self.speed
                return roll
            else:
                print(f"{self.name} considers fleeing but decides to fight!")
                return None
        return None


