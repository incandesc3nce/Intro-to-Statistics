class Component:
    _price = 0.0
    _power = 0

    def __init__(self, price, power):
        self._price = price
        self._power = power

    def read(self, i):
        self._price = float(input(f"Цена компонента {i}: "))
        self._power = int(input(f"Расход электроэнергии компонента {i}: "))

    def display(self):
        print(f"Цена компонента: {self._price}")
        print(f"Расход электроэнергии: {self._power}\n")

    def economy(self):
        return 1 / (self._price * self._power)
    
class Computer:
    _price = 0.0
    _power = 0
    _components = [Component(0, 0), Component(0, 0), Component(0, 0)]

    def __init__(self, price, power, components):
        self._price = price
        self._power = power
        self._components = components

    def total_price(self):
        return self._price + sum([component._price for component in self._components])
    
    def total_power(self):
        return self._power + sum([component._power for component in self._components])

    def most_economical(self):
        most_economical_component = self._components[0]
        for component in self._components:
            if component.economy() > most_economical_component.economy():
                most_economical_component = component
        return most_economical_component
    
    
    def read(self):
        for i in range(3):
            self._components[i].read(i+1)

    def display(self):
        print(f"Цена компьютера: {self.total_price()}")
        print(f"Расход электроэнергии компьютера: {self.total_power()}")
        print("\nСамая экономичная компонента:")
        most_economical_component = self.most_economical()
        most_economical_component.display()

    
    
comp1 = Computer(0, 0, [Component(0, 0), Component(0, 0), Component(0, 0)])
comp1.read()
comp1.display()


