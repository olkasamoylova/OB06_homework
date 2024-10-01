import random


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        damage = random.randint(10, self.attack_power)
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона")

    def is_alive(self):
        return self.health > 0

    class Game():
        def __init__(self, player_name):
            self.player = Hero(player_name)
            self.computer = Hero("Компьютер")


        def start(self):
            print("Игра начинается")
            round_counter = 1

            while self.player.is_alive() and self.computer.is_alive():
                print(f"\nРаунд {round_counter}")
                round_counter += 1




