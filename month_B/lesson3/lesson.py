from enum import Enum

class Color(Enum):
    RED = '\033[31m'
    BLUE = '\033[34m'
    YELLOW = '\033[33m'
    GREEN = '\033[32m'

class MusicPlayable:
    @staticmethod
    def play_music(song):
        print(f'Now is playing{song}')

    @staticmethod
    def stop_music():
        print('Music stop')


class Drawble:
    @staticmethod
    def draw(emoji):
        print(emoji)

class Car(MusicPlayable, Drawble):
    def __init__(self, model, year, color):
        self.__model = model
        self.__year = year

        if type(color) == Color:
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
        return f'MODEL: {self.__model} YEAR: {self.__year} COLOR: {self.__color.value}' + '\033[0m'


    def __gt__(self, other):
        return self.__year > other.__year
    

class FuelCar(Car):
    __total_fuel_amount = 1000

    @staticmethod
    def get_fuel_type():
        return 'AI 95'
    @classmethod
    def get_total_fuel_amount(cls):
        return cls.__total_fuel_amount
    @classmethod
    def fill_total_fuel_amount(cls, amount):
        cls.__total_fuel_amount += amount

    

    def __init__(self, model, year, color, fuel_bank):
        Car.__init__(self, model, year, color)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel_amount -= fuel_bank
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

class SmartPhone(MusicPlayable, Drawble):
    pass


print(f'We have {FuelCar.get_total_fuel_amount()}')
car = Car('BMW X6', 2020, Color.BLUE)
print(car)

nissan_car = FuelCar('Nissan Patrol', 2009, Color.RED, 85)
print(nissan_car)
nissan_car.drive()

tesla_car = ElectricCar('Tesla Model X', 2023, Color.YELLOW, 25000)
print(tesla_car)


prius_car = HybridCar('Toyota Prius', 2000, Color.GREEN, 65, 15000)
print(prius_car)

prius_car.drive()



print(HybridCar.mro())


number1 = 7
number2 = 3
print(f'Number one is bigger than number two? --> {number1 > number2}')


print(f'Nissan car is better than Tesla car --> {nissan_car > tesla_car}')

FuelCar.fill_total_fuel_amount(500)
# FuelCar.total_fuel_amount -= 100
print(f'We have {FuelCar.get_total_fuel_amount()} ({FuelCar.get_fuel_type()})')


tesla_car.play_music('song1')
tesla_car.stop_music()

samsung = SmartPhone()
samsung.play_music(' Best Song')

tesla_car.draw('🏎️')

samsung.draw('📱')


if tesla_car.model == 'Tesla Model X':
    print('This car is cool')



if tesla_car.color == Color.YELLOW:
    print('This car is pretty')