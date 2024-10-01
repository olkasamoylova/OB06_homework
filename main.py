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

            # Ход игрока
            self.player_turn()

            if not self.computer.is_alive():
                print(f"\n{self.computer.name} побежден!")
                print(f"{self.player.name} победил в битве!")
                break

            # Ход компьютера
            self.computer_turn()

            if not self.player.is_alive():
                print(f"\n{self.player.name} побежден!")
                print(f"{self.computer.name} победил в битве!")
                break

        print("игра окончена")


    def player_turn(self):
        print(f"{self.player.name} имеет {self.player.health} здоровья")
        print(f"{self.computer.name} имеет {self.computer.health} здоровья")
        input("Нажмите Enter, чтобы атаковать...")
        self.player.attack(self.computer)
        print(f"У {self.computer.name} осталось {self.computer.health} здоровья")


    def computer_turn(self):
        print(f"{self.player.name} имеет {self.player.health} здоровья")
        print(f"{self.computer.name} имеет {self.computer.health} здоровья")
        input("Нажмите Enter, чтобы пропустить ход компьютера...")
        self.computer.attack(self.player)
        print(f"У {self.player.name} осталось {self.player.health} здоровья.")

player_name = input("Введите имя вашего героя: ")
game = Game(player_name)
game.start()


