start_num = input('Enter the num you want to convert: ')
start_num_sys = int(input('Enter the numeral system your num from 2 until 36: '))
goal_num_sys = int(input('Enter the your goal numeral system from 2 until 36: '))
print('Nums in numerals system bigger 10 will show in letters from A until Z')

def start_num_to_dec(start_num, start_num_sys):
    actual_digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:start_num_sys:]
    asdf = []
    decnum = 0
    if start_num:
        for num in start_num:
            asdf.append(actual_digits.index(num.upper()))
        s = 0
        for num in asdf[::-1]:
            x = num * (start_num_sys ** s)
            s += 1
            decnum += x
        return decnum
    else:
        return 0

decnum = (start_num_to_dec(start_num, start_num_sys))
print(decnum)


def dec_to_goal_num(decnum, goal_num_sys):
    actual_digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:goal_num_sys:]
    goal_num = ''
    while decnum >= 1:
        q = actual_digits[decnum % goal_num_sys]
        decnum //= goal_num_sys
        goal_num += q

    return goal_num[::-1]

goal_num = dec_to_goal_num(decnum, goal_num_sys)    
print(goal_num)