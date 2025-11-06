import random
from core.player import Player
from core.orc import Orc
from core.goblin import Goblin
from core.boss import Boss

class Game:
    def roll_dice(self, sides):
        return random.randint(1, sides)

    def choose_random_monster(self):
        monster_type = random.choice(["orc", "goblin"])
        name = random.choice(["Bob", "Jon", "Tyson", "Brog"])
        if monster_type == "orc":
            return Orc(name)
        else:
            return Goblin(name)

    def battle(self, player, monster):
        print(f"A wild {monster.type} appears!")
        monster.speak()
        player.speak()
        while player.hp > 0 and monster.hp > 0:
            p_roll = self.roll_dice(6) + player.speed
            m_roll = self.roll_dice(6) + monster.speed
            if p_roll >= m_roll:
                attacker, defender = player, monster
            else:
                attacker, defender = monster, player
            print(f"{attacker.name} attacks first!")
            attacker.attack(defender, self.roll_dice)
            if defender.hp <= 0:
                print(f"{defender.name} is defeated!")
                break
            attacker, defender = defender, attacker
            attacker.attack(defender, self.roll_dice)
            if defender.hp <= 0:
                print(f"{defender.name} is defeated!")
                break

    def start_dungeon(self, player):
        rooms = [None]*8
        positions = random.sample(range(8), random.randint(3, 6))
        for i in positions:
            rooms[i] = self.choose_random_monster()
        print("\nDungeon begins!")
        for i in range(8):
            print(f"\nEntering room {i + 1}")
            if rooms[i]:
                monster = rooms[i]
                self.battle(player, monster)
                if player.hp <= 0:
                    print("You died in the dungeon.")
                    return
        boss = Boss("Zed")
        print("\nBoss fight!")
        self.battle(player, boss)
        if player.hp > 0:
            print("You defeated the boss and cleared the dungeon!")
        else:
            print("You were slain by the boss.")

    def start(self):
        name = input("Enter player name: ")
        player = Player(name)
        while True:
            print("\n1. Battle\n2. start_dungeon\n3. Exit")
            choice = input("Choose: ")
            if choice == "1":
                monster = self.choose_random_monster()
                self.battle(player, monster)
                if player.hp <= 0:
                    print("You died. Game over.")
                    break
            elif choice == "2":
                self.start_dungeon(player)
                break
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

                print("Invalid choice.")

