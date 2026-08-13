import game_logic
from decouple import config


def start_game(your_score):
    game_list = []
    for i in range(1, 31):
        game_list.append(i)

    bid = int(input('Укажите вашу ставку, пожалуйста: '))
    x = int(input('Введите число на которое хотите поставить: '))

    if your_score is None:
        your_score = config('MY_MONEY', cast=int)

    if bid <= 0:
        print('Ваша ставка должна быть больше 0')
        return your_score

    if bid > your_score:
        print('Вы не можете сделать вашу ставку больше чем имеете на балансе')
        return your_score

    if x not in game_list:
        print('Выберите число от 1 до 30')
        return your_score

    return game_logic.game_logic(x, game_list, bid, your_score)


your_score = None

while True:
    your_score = start_game(your_score)

    if your_score <= 0:
        print('GAME OVER: You lost all your money')
        print(f'С начала игры ваш счет изменился с 1000 на {your_score}')
        break

    q = input('Хотите сыграть еще? click Y/y: ')

    if q not in ['Y', 'y']:
        print(f'С начала игры ваш счет изменился с 1000 на {your_score}')
        break