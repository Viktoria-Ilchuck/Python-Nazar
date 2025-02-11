from random import randint

class Astronaut:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.energy = 50
        self.morale = 50
        self.alive = True

    def explore(self):
        print(f"{self.name} досліджує Марс!")
        self.energy -= 15
        self.morale += 5

        if randint(1, 10) > 5:
            print("Отримана травма!")
            self.health -= 20


    def repair(self):
        print(f"{self.name} ремонтує базу.")
        self.energy -= 5
        self.morale -= 5


    def rest(self):
        print(f"{self.name} відпочиває.")
        self.energy += 50
        self.morale += 3


    def communicate(self):
        print(f"{self.name} зв'язується з Землею.")
        self.morale += 10
        self.energy -= 15


    def is_alive(self):

        if self.health <= 0:
            print(f"{self.name} помер від травм.")
            self.alive = False
        elif self.energy <= 0:
            print(f"{self.name} виснаження.")
            self.alive = False
        elif self.morale <= 0:
            print(f"{self.name} депресія")
            self.alive = False


    def end_of_day(self):
        print(f"Стан {self.name}: Здоров'я = {self.health}, Енергія = {self.energy}, Мораль = {self.morale}")


    def live(self, day):
        print(f"День {day}: {self.name} на Марсі")
        action = randint(1, 4)
        if action == 1:
            self.explore()
        elif action == 2:
            self.repair()
        elif action == 3:
            self.rest()
        elif action == 4:
            self.communicate()

        self.end_of_day()
        self.is_alive()


vika = Astronaut("Vika")

for day in range(365):
    if vika.alive == False:
        break

    vika.live(day)
