class Animal:
    def __init__(self, name, age):
        self.__name = name
        if type(age) == int and age > 0:
            self.__age = age
        else:
             raise ValueError('Wrong value for attribute age. It must be positive number')
        self.__was_born()

    def __was_born(self):
         print(f'Animal {self.__name} was born!!!')

    
    def set_name(self, new_name):
        self.__name = new_name

    def set_age(self, new_age):
        if type(new_age) == int and new_age > 0:
            self.__age = new_age
        else:
             raise ValueError('Wrong value for attribute age. It must be positive number')

    def get_age(self):
        return self.__age

    def get_name(self):
            return self.__name

    
    def info(self):
        return (f'NAME: {self.__name} AGE: {self.__age}'
        f' BIRTH YEAR: {2026 - self.__age}')


class Dog(Animal):
    def __init__(self, name, age, commands):
        super(Dog, self).__init__(name, age)
        self.__commands = commands


    @property
    def commands(self):
         return self.__commands

    @commands.setter
    def commands(self, value):
        self.__commands = value

    def info(self):
         return super().info() + f' COMMANDS: {self.__commands}'

class FightingDog(Dog):
    def __init__(self, name, age, commands, wins):
        super(FightingDog, self).__init__(name, age, commands)
        self.__wins = wins

    @property
    def wins(self):
         return super().__wins

    @wins.setter
    def wins(self, value):
         self.__wins =  value

    def info(self):
         return super().info() + f' WINS: {self.__wins}'


class Cat(Animal):
     def __init__(self, name, age):
          super(Cat, self).__init__(name, age)                   

some_animal = Animal('Anim', 2)
print(some_animal.info())

some_animal.__age = 5
print(some_animal.info())

print(some_animal.get_name())


some_animal.set_age(10)
print(some_animal.get_age())




bobik_dog = Dog('Bobik', 10, 'Sit')
print(bobik_dog.commands)

bobik_dog.commands = 'Sit, run'


print(bobik_dog.info())


tom_cat = Cat ('Tom', 5)
print(tom_cat.info())



reks_f_dog = FightingDog('Reks', 1, 'Fight', 15)
print(reks_f_dog.info())