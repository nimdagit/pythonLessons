"""TASK 1"""l
numsList = [5,20.18,103,4]
theNum = 27
def nearestNum(nums, x)-> tuple:
    sortnums = sorted(nums, key=lambda i: abs(x - i))   
    return x, sortnums
print(nearestNum(numsList, theNum))


"""TASK 2"""


i = 12

while i > 0 :
    try:
        day = int(input('enter your birth day: '))
        if day < 1 or day  > 31:
            print ('Your entered birth DAY is NOT correct. CORRECT DAY IS FROM 1 UNTIL 31')
            i-=1
            print(f'Осталось попыток {i}')
            continue
        month = int(input('enter your birth month: '))
        if month < 1 or month > 12:
            print ('Your entered birth MONTH is NOT correct. CORRECT MONTH IS FROM 1 UNTIL 12')
            i-=1
            print(f'Осталось попыток {i}')
            continue

        if day > 30:
            if month == 2 or month == 4 or month == 6 or month == 9 or month == 11:
                print ('Your entered birth date is not correct, because this month has only 30 days')
                i-=1
                print(f'Осталось попыток {i}')
                continue
        if 29 < day and month == 2:
            print ('Your entered birth date is NOT correct because februare may has only 29 days')
            i-=1
            print(f'Осталось попыток {i}')
            continue
        

        #ОВЕН
        if 21 <= day <= 31 and month == 3:
                print('you are OVEN')
        elif 1 <= day <= 20 and month == 4:
                print ('you are OVEN')
        #ТЕЛЕЦ
        elif 21 <= day <= 30 and month == 4:
                print('you are TELETS')
        elif 1 <= day <= 21 and month == 5:
                print ('you are TELETS')
        #БЛИЗНЕЦЫ
        elif 22 <= day <= 31 and month == 5:
                print('you are TWINS')
        elif 1 <= day <= 21 and month == 6:
                print ('you are TWINS')
        #РАК
        elif 22 <= day <= 30 and month == 6:
                print('you are CANCER')
        elif 1 <= day <= 22 and month == 7:
                print ('you are CANCER')
        #ЛЕВ
        elif 23 <= day <= 31 and month == 7:
                print('you are LION')
        elif 1 <= day <= 21 and month == 8:
                print ('you are LION')
        #ДЕВА
        elif 22 <= day <= 31 and month == 8:
                print('you are GIRL')
        elif 1 <= day <= 23 and month == 9:
                print ('you are GIRL')

        #ВЕСЫ
        elif 24 <= day <= 30 and month == 9:
                print('you are VESY')
        elif 1 <= day <= 23 and month == 10:
                print ('you are VESY')

        #СКОРПИНЫ
        elif 24 <= day <= 31 and month == 10:
                print('you are SCORPIO')
        elif 1 <= day <= 22 and month == 11:
                print ('you are SCORPIO')


        #СТРЕЛЕЦ
        elif 23 <= day <= 30 and month == 11:
                print('you are STRELETS')
        elif 1 <= day <= 22 and month == 12:
                print ('you are STRELETS')


        #КОЗЕРОГ
        elif 23 <= day <= 31 and month == 12:
                print('you are GOAT')
        elif 1 <= day <= 20 and month == 1:
                print ('you are GOAT')

        # #ВОДОЛЕЙ
        #     elif 21 <= day <= 31 and month == 1:
        #         print('you are WATERER')
        #     elif 1 <= day <= 19 and month == 2:
        #         print ('you are WATERER')
       #ВОДОЛЕЙ
        elif day in range(21, 32)  and month == 1:
                print('you are WATERER')
        elif day in range(1, 20) and month == 2:
                print ('you are WATERER')

        #РЫБЫ
        elif 20 <= day <= 29 and month == 2:
                print('you are FISH')
        elif 1 <= day <= 20 and month == 3:
                print ('you are FISH')

     
        
        i-=1
        print(f'Осталось попыток {i}')
    except:
        print('Вводите даты только в виде чисел')
        i-=1
        print(f'Осталось попыток {i}')























#Lambda функции. обработка исключений
"""Lambda функция lambda параметры: выражение"""
#sorted(), filter(),map()
# cities = ['tokmok', 'bishkek', 'karakol', 'kant', 'cholpon-ata']
# print( cities )

# sortedCities = sorted(cities, key = lambda word: word[-1])
# print( sortedCities)

# filterCities = list(filter(lambda word: word.endswith('k'), cities))
# print ( filterCities)

# mapCities = list(map(lambda word: word.upper(), cities))
# print(mapCities)



# lambdaFunction = lambda n1, n2: n1 + n2
# print (lambdaFunction(3,4))

# def defFunction (n1, n2):
#     return n1 + n2
# print (defFunction(3,4))


# def upFirstLetter(word: str) -> str:
#     return word.title()



# def showWords(words, func):
#     for i in words:
#         print(func(i))

# showWords(cities, lambda word: word.title())


"""ОБРАБОТКА ИСКЛЮЧЕНИЙ"""
