from random import choice


def game_logic(x, game_list, bid, your_score):
    win_num = choice(game_list)

    if win_num == x:
        print('YOU WON!!!')
        result = your_score
        print(f'Ваш счет: {result - bid + (bid * 2)}')
        return result - bid + (bid * 2)

    else:
        print('You were close, try again')
        result = your_score
        print(result - bid)
        return result - bid