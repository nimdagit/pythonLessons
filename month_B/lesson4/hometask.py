# 1. Magic должен увеличивать атаку каждого героя после каждого раунда на n-ное количество
# 2. Thor, удар по боссу имеет шанс оглушить босса на 1 раунд, вследствие чего босс пропускает 1 раунд и не наносит урон героям
from enum import Enum
from random import choice, randint

class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    BOOST = 2
    DAMAGE_REFLECTION = 3
    HEAL = 4
    STUNNING = 5
    REVIVE = 6

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
        self.__stunning = False
    @property
    def defence(self):
        return self.__defence
    @property
    def stunning(self):
        return self.__stunning
    @stunning.setter
    def stunning(self, value: bool):
        self.__stunning = value

    def choose_defence(self, heroes):
            random_hero = choice(heroes)
            self.__defence = random_hero.ability

    def attack(self, heroes):
        if self.stunning == True:
            self.stunning = False
        else:
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
        coeff = randint(2,4)
        boss.health -= self.damage * coeff
        print(f'Warrior {self.name} hits criticaclly {self.damage * coeff} damage')

class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            hero.damage += 5

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

class Thor(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.STUNNING)

    def apply_super_power(self, boss, heroes):
        rand_num = choice(range(1,3))
        if rand_num == 1:
            boss.stunning = True
            print(f'Thor {self.name} stunned {boss.name }')
# 3. Witcher, не наносит урон боссу, но получает урон от босса. Имеет 1 шанс оживить первого погибшего героя, отдав ему свою жизнь, при этом погибает сам.
class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.REVIVE)
        self.__used_revive = False

    def attack(self, boss):
        pass

    def apply_super_power(self, boss, heroes):
        if self.__used_revive:
            return
        for hero in heroes:
            if hero.health <= 0:
                hero.health = self.health
                self.health = 0
                self.__used_revive = True
                print(f'Witcher {self.name} revived {hero.name}, sacrificing himself')
                break


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

    print('Summary')
    show_stats(boss, heroes)

def start_game():
    boss = Boss('All For One', 1000, 80)

    warrior1 = Warrior('Midoria', 280, 10)
    warrior2 = Warrior('Bakugo', 270, 15)
    magic = Magic('Yuno', 260, 20)
    berserk = Berserk('Meliodas', 250, 10)
    doc = Medic('Tsunade', 240, 5, 15)
    assistant = Medic('Sakura', 300, 5, 5)
    thor = Thor('Raiden', 250, 10)
    witcher = Witcher('German', 360, 0)
    
    heroes_list = [warrior1, warrior2, magic, berserk, doc, assistant, thor, witcher]

    show_stats(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)

start_game()











# 4. Golem, который имеет увеличенную жизнь но слабый удар. Может принимать на себя 1/5 часть урона исходящего от босса по другим игрокам
# 5. Avrora, которая может входить в режим невидимости на 2 раунда (т.е не получает урон от босса), в тоже время полученный урон в режиме невидимости возвращает боссу в последующих раундах. Она может исчезать только один раз за игру
# 6. Druid, который имеет способность рандомно призывать помощника ангела героям или же ворона боссу на 1 раунд за всю игру. "Ангел" увеличивает способность медика лечить героев на  n кол-во. А ворон прибавляет  агрессию (увеличивается урон на 50%), боссу если его жизнь менее 50%.
# 7. Hacker, который будет через раунд забирать у Босса N-ое количество здоровья и переводить его одному из героев
# 8. Tricky,  способность которого будет состоять в том, чтобы притвориться мертвым в определенном раунде(из случайного выбора), но в следующем раунде он снова вступает в бой. При этом он не получает урон и не бьет босса когда притворился мертвым
# 9. AntMan, в каждом раунде он может увеличиться или же уменьшится на N-ный размер, также увеличиваются/уменьшаются жизнь и урон, после раунда он возвращается в исходный размер
# 10 Deku (сила удара может меняться каждый раунд с шансом 50 на 50,  может усилится на 20%, 50%, 100%, но при усилении теряется хп (чем сильнее усиление, тем больше хп потеряет герой)
# 11. Герой Kamikadze  без урона но хорошое здоровье, его способность  жертвовать собой. Но он должен попасть точно в цель, иначе нанесет урон только на 50% из своего остатка жизни.
# 12. Герой Samurai кидает сюрикенами которые делятся на два вида: 1) Вирус наносит N-e кол-во урона. 2) Вакцина лечит на N-e кол-во единиц здоровье босса. сюрикены выбирает Рандом.
# 13 Герой Bomber, когда босс убивает героя он взрывается и наносит боссу дополнительный урон в 100 единиц.
# 14. Reaper(Жнец) - при уровне здоровья менее 30% увеличивается урон вдвое, а при 15% втрое
# 15. Spitfire - каждый раз когда босс убивает одного или нескольких героев то наш герой показывает  агрессию на 80 единиц урона
# 16. Герой King, не наносить урон, только получает, с 10% шансом он может призвать героя Saitama который убьет босса с 1 удара