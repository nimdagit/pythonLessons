from enum import Enum
from random import choice, randint

class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    BOOST = 2
    DAMAGE_REFLECTION = 3
    HEAL = 4

class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health
    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage
    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None
    @property
    def defence(self):
        return self.__defence
    # @defence.setter
    # def defence(self, value):
    #     self.__defence = value
        

    def choose_defence(self, heroes):
            random_hero = choice(heroes)
            self.__defence = random_hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                if hero.ability == SuperAbility.DAMAGE_REFLECTION and self.__defence != SuperAbility.DAMAGE_REFLECTION:
                    hero.blocked = int(self.damage / 5)
                    hero.health -= (self.damage - hero.blocked)
                else:
                    hero.health -= self.damage
            

    def __str__(self):
        return 'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        if type(ability) == SuperAbility:
            self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass

class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coeff = randint(2,6)
        boss.health -= self.damage * coeff
        print(f'Warrior {self.name} hits criticaclly {self.damage * coeff} damage')

class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):
        pass

class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.DAMAGE_REFLECTION)
        self.__blocked = 0

    @property
    def blocked(self):
        return self.__blocked
    @blocked.setter
    def blocked(self, value):
        self.__blocked = value


    def apply_super_power(self, boss, heroes):
        boss.health -= self.__blocked
        print(f'Berserk {self.name} reflexed {self.__blocked} damage')

class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_points

round_num = 0

def is_game_over(boss, heroes):
    if boss.health <= 0:
        print('HEROES WON!!!')
        return True

    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break

    if all_heroes_dead == True:
        print('BOSS WON!!!')
    return all_heroes_dead
    
def show_stats(boss, heroes):
    print(f'ROUND: {round_num} -------------')
    print(boss)
    for hero in heroes:
        print(hero)

def play_round(boss, heroes):
    global round_num
    round_num += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 and boss.defence != hero.ability:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)

    show_stats(boss, heroes)

def start_game():
    boss = Boss('All For One', 1000, 50)

    warrior1 = Warrior('Midoria', 280, 10)
    warrior2 = Warrior('Bakugo', 270, 15)
    magic = Magic('Yuno', 260, 20)
    berserk = Berserk('Meliodas', 250, 10)
    doc = Medic('Tsunade', 240, 5, 15)
    assistant = Medic('Sakura', 300, 5, 5)

    heroes_list = [warrior1, warrior2, magic, berserk, doc, assistant]

    show_stats(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)

start_game()
