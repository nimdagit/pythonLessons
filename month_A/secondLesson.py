# # time = input('enter time: ').lower()


# # if time == 'morning' or time == 'утро':
# #     print ('good morning')
# # elif time == 'day' or time == 'день':
# #     print ('good afternoon')
# # elif time == 'evening' or time == 'вечер':
# #     print ('good evening')
# # else:
# #     print ('hello baby')





# # age = int(input('Введите ваш возраст целым числом: '))
# # if age >= 18 and age <120:
# #     print ('Вы совершеннолетний!')
# # elif age <= 0 or age >= 120:
# #     print ('Введеный вами возраст некорректен!')
# # else:
# #     print ('Вы маленький!')





# # холодно от 0 до -30
# # прохладно от 1 до 10
# # тепло от 11 до 25
# # жарко от 26 до 40


# temperature = int(input('Enter temperature: '))
# if temperature >= -30 and temperature <= 0:
#     print ('Холодно!')
# elif temperature >= 1 and temperature <= 10:
#     print ( 'Прохладно!')
# elif temperature >=11 and temperature <= 25:
#     print ('Тепло!')
# elif 26 <= temperature <= 40:
#     print ('Жарко!')
# else:
#     print (f'Несовместимая с жизнью температура, опасно! ({te})')

# if day >= 1 and day  <= 31:
#     print ('Your entered birth DATE is correct, great')


day = int(input('enter your birth day: '))
if day < 1 or day  > 31:
    print ('Your entered birth DAY is NOT correct. CORRECT DAY IS FROM 1 UNTIL 31')
month = int(input('enter your birth month: '))
if month < 1 or month > 12:
     print ('Your entered birth MONTH is NOT correct. CORRECT MONTH IS FROM 1 UNTIL 12')

if day > 30:
    if month == 2 or month == 4 or month == 6 or month == 9 or month == 11:
        print ('Your entered birth date is not correct, because this month has only 30 days')
if 29 < day and month == 2:
    print ('Your entered birth date is NOT correct because februare may has only 29 days')

else:
#ОВЕН
    if 21 <= day <= 31 and month == 3:
        print('you are oven')
    elif 1 <= day <= 20 and month == 4:
        print ('you are oven')
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

#РЫБЫ
    elif 20 <= day <= 29 and month == 2:
        print('you are FISH')
    elif 1 <= day <= 20 and month == 3:
        print ('you are FISH')


#ВОДОЛЕЙ
    elif day in range(21, 31)  and month == 1:
        print('you are WATERER')
    elif day in range(1, 19) and month == 2:
        print ('you are WATERER')