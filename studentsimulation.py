from random import randint

class Student:

    def __init__(self,name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Час навчатися")
        self.progress +=0.12
        self.gladness -= 5

    def to_sleep(self):
        print("Я йду поспати!!!")
        self.gladness += 3

    def to_chill(self):
        print("Час відпочити")
        self.gladness += 5
        self.progress -=0.1


    def is_alive(self):
        if self.progress < -0.5:
            print("Мене вигнали з академії")
            self.alive = False

        elif self.gladness <= 0:
            print("В мене дипресія")
            self.alive = False

        elif self.progress >=5:
            print("Закінчив автоматом навчання")
            self.alive = False

    def end_of_day(self):
        print(f"Радість = {self.gladness}")
        print(f"Прогрес = {self.progress}")

    def live(self,day):
        print(f"День:{day} - студент: {self.name}")
        live_cube = randint(1,3)

        if live_cube == 1:
            self.to_study()

        elif live_cube == 2:
            self.to_study()

        elif live_cube == 3:
            self.to_chill()

        self.end_of_day()
        self.is_alive()

nazar = Student("Nazar")

for day in range(365):
    if nazar.alive == False:
        break

    nazar.live(day)