class Angle:
    _degree = 0
    _minutes = 0
    _seconds = 0

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
        self.__degree += Angle2._Angle__degree
        self.__minutes += Angle2._Angle__minutes
        self.__seconds += Angle2._Angle__seconds


class Angle2D(Angle):
    _z = 0

    def __init__(self, degree, minutes, seconds, z):
        super().__init__(degree, minutes, seconds)
        self.__z = z
    
    def read(self):
        super().read()
        self.__z = int(input("Z: "))

    def display(self):
        super().display()
        print("Z: ", self.__z)

    def round(self):
        self.__z = round(self.__z)
        self._Angle__degree += self.__z
        super().round()

    def add(self, Angle2):
        super().add(Angle2)
        self.__z += Angle2._Angle2d__z

def main():
    angle = Angle(0, 0, 0)
    angle.read()
    angle.display()
    angle.round()
    angle.display()

    angle2D = Angle2D(0, 0, 0, 0)
    angle2D.read()
    angle2D.display()
    angle2D.round()
    angle2D.display()
    
    angle.add(angle2D)
    angle.display()

if __name__ == "__main__":
    main()

