class Course:
    def __init__(self,name,instructor,duration):
        self.name = name
        self.instructor = instructor
        self.duration = duration

    def corse_info(self):
        print (f"Курс:{self.name},Викладач:{self.instructor} Тривалість:{self.duration}")

    def is_long_course(self):
        print( self.duration > 2)

course1 = Course("Python", " Лакуста Назар", 2.5)
course1.is_long_course()
course1.corse_info()
course2 = Course("Веб-розробка", "Лакуста Назар", 3)
course1.is_long_course()
course1.corse_info()
course3 = Course("HTML","Лакуста Назар",2)
course1.is_long_course()
course1.corse_info()




