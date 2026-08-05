# ДЗ*:
# 1. Создать класс Computer (компьютер) с приватными атрибутами cpu и memory.
# 2. Добавить сеттеры и геттеры к существующим атрибутам.
# 3. Добавить в класс Computer метод make_computations, в котором бы выполнялись арифметические вычисления с атрибутами объекта cpu и memory.
# 4. Создать класс Phone (телефон) с приватным полем sim_cards_list (список симкард)
# 5. Добавить сеттеры и геттеры к существующему атрибуту.
# 6. Добавить в класс Phone метод call с входящим параметром sim_card_number и call_to_number, в котором бы распечатывалась симуляция звонка в зависимости от переданного номера сим-карты (например: если при вызове метода передать число 1 и номер телефона, распечатывается текст “Идет звонок на номер +996 777 99 88 11” с сим-карты-1 - Beeline).
# 7. Создать класс SmartPhone и наследовать его от 2-х классов Computer и Phone.
# 8. Добавить метод в класс SmartPhone use_gps с входящим параметром location, который бы распечатывал симуляцию проложения маршрута до локации.
# 9. В каждом классе переопределить магический метод str которые бы возвращали полную информацию об объекте.
# 10. Перезаписать все магические методы сравнения в классе Computer (6 шт.), для того чтоб можно было сравнивать между собой объекты, по атрибуту memory.
# 11. Создать 1 объект компьютера, 1 объект телефона и 2 объекта смартфона
# 12. Распечатать информацию о созданных объектах
# 13. Опробовать все возможные методы каждого объекта (например: use_gps, make_computations, call, а также магические методы)

class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu
    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory
    @memory.setter
    def memory(self, value):
        self.__memory  = value

    def make_computations(self, operation):
        if operation == '+':
            print(self.__cpu + self.__memory)
        elif operation == '-':
            print(self.__cpu - self.__memory)
        elif operation == '/':
            print(self.__cpu / self.__memory)
        elif operation == '*':
            print(self.__cpu * self.__memory)        
        else:
            print(f'Выберете операцию из следующих символов + - * /')

    def __str__(self):
        return f'CPU: {self.__cpu} MEMORY: {self.__memory}'



    def __gt__(self, other):
        return self.__memory > other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory
    
    
class Phone():
    def __init__(self, sim_card_list):
        self.__sim_card_list = sim_card_list

    @property
    def sim_card_list(self):
        return self.__sim_card_list
    @sim_card_list.setter
    def sim_card_list(self, value):
        self.__sim_card_list = value

    def call(self, sim_card_number, call_to_number):
        print(f'Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number}')

    def __str__(self):
        return f'SIM CARD LIST: {self.sim_card_list}'

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_card_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_card_list)
    

    def use_gps(self, location):
        print(f'Чтобы дойти до {location} вам нужно пройти по N-ному пути')

    def __str__(self):
        return Computer.__str__(self) + '   ' + Phone.__str__(self)

pc1 = Computer(5000, 10000)
print(pc1)
phone1 = Phone(['1 - Beeline', '2 - O!'])
print(phone1)
smartphone1 = SmartPhone(2500, 7500, ['1 - O!', '2 - MegaCom'])
print(smartphone1)
smartphone2 = SmartPhone(4000, 8000, ['1 - Megacom', '2 - Beeline'])
print(smartphone2)


print('Проверка методов:')
pc1.make_computations('/')
smartphone2.make_computations('+')

phone1.call(phone1.sim_card_list[0], '0553-13-18-01')
smartphone2.call(smartphone2.sim_card_list[1], '8 800 555 35 35')

smartphone1.use_gps('Ala-Archa')
smartphone2.use_gps('Успешная жизнь')
print(f'сматрфон 1 имеет больше оперативной пямити чем сматрфон 2? --> {smartphone1 > smartphone2}')
print(f'сматрфон 1 имеет больше оперативной пямити чем сматрфон 2? --> {smartphone1 < smartphone2}')
print(f'компьютер имеет больше оперативной пямити чем оба смартфона? --> {pc1 > smartphone1 and pc1 > smartphone2}')
print(f'сматрфон 2 находится посередине по объму оперативки среди трех устройств? --> {pc1> smartphone2 > smartphone1}')
print(f'Hey, Syrga, am I too good? --------------> {pc1 != smartphone1}')
print(f'You are not bad too, aren\'t you? --> {smartphone2 >= smartphone1}')
print(SmartPhone.__mro__)

# 10. Перезаписать все магические методы сравнения в классе Computer (6 шт.), для того чтоб можно было сравнивать между собой объекты, по атрибуту memory.
# 13. Опробовать все возможные методы каждого объекта (например: use_gps, make_computations, call, а также магические методы)