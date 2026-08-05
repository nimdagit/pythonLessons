class Car:
    def __init__(self, model, year, color):
        self.__model = model
        self.__year = year
        self.__color = color

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def drive(self):
        print(f' Car {self.__model} is driving')

    def __str__(self):
        return f'MODEL: {self.__model} YEAR: {self.__year} COLOR: {self.__color}'

    def __gt__(self, other):
        return self.__year > other.__year


class FuelCar(Car):
    def __init__(self, model, year, color, fuel_bank):
        Car.__init__(self, model, year, color)
        self.__fuel_bank = fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    def drive(self):
        print(f'Car {self.model} is driving by using fuel')

    def __str__(self):
        return super().__str__() + f' FUEL BANK: {self.__fuel_bank} lt'


class ElectricCar(Car):
    def __init__(self, model, year, color, battery):
        Car.__init__(self, model, year, color)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print(f'Car {self.model} is driving by using electrycity')

    def __str__(self):
        return super().__str__() + f' Battery: {self.__battery}'
    
class HybridCar(ElectricCar, FuelCar):
    def __init__(self, model, year, color, fuel_bank, battery):
        FuelCar.__init__(self, model, year, color, fuel_bank)
        ElectricCar.__init__(self, model, year, color, battery)

car = Car('BMW X6', 2020, 'Red')
print(car)

nissan_car = FuelCar('Nissan Patrol', 2009, 'Silver', 85)
print(nissan_car)
nissan_car.drive()

tesla_car = ElectricCar('Tesla Model X', 2023, 'Black', 25000)
print(tesla_car)


prius_car = HybridCar('Toyota Prius', 2000, 'Blue', 65, 15000)
print(prius_car)

prius_car.drive()



print(HybridCar.mro())


number1 = 7
number2 = 3
print(f'Number one is bigger than number two? --> {number1 > number2}')


print(f'Nissan car is better than Tesla car --> {nissan_car > tesla_car}')