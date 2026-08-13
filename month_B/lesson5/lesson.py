from random import randint, choice
import calculator
from person import Person
from termcolor import colored, cprint
from decouple import config




print(randint(2, 10))
print(calculator.multiplication(9, 2))

friend = Person('Jew', 45 )
print(friend)

cprint("Hello, World!", "blue", "on_red")
print(config('DATABASE_URL'))

commented = config('COMMENTED', default = 0, cast = int)
print(commented * 2)