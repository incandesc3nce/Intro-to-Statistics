class Angle:
    __degree = 0
    __minutes = 0
    __seconds = 0

    def __init__(self, degree, minutes, seconds):
        self.__degree = degree
        self.__minutes = minutes
        self.__seconds = seconds
    
    def read(self):
        self.__degree = int(input("Градусы: "))
        self.__minutes = int(input("Минуты: "))
        self.__seconds = int(input("Секунды: "))

    def display(self):
        print(f"{self.__degree}° {self.__minutes}' {self.__seconds}\"")
    
    def round(self):
        self.__degree += (self.__minutes + 30 + self.__seconds / 60) // 60
        self.__minutes = 0
        self.__seconds = 0

    def add(self, Angle2):
        self.__degree += Angle2.__degree
        self.__minutes += Angle2.__minutes
        self.__seconds += Angle2.__seconds


angle = Angle(0, 0, 0)
angle.read()
angle.display()

angle2 = Angle(0, 0, 0)
angle2.read()
angle2.display()

angle.add(angle2)
angle.display()

angle.round()
angle.display()