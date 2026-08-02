def is_strong_password (password):    

    def is_sp_char(char):
        spCharCount=0
        for ch in char:
            if ch.isalnum() == False:
                spCharCount +=1
        
        return spCharCount
    

    if len(password) >= 6 and is_sp_char(password) > 1 and any(char.isupper() for char in password) and any(char.isdigit() for char in password):
        print('True')
    else:
        print('False')


is_strong_password(input('Введите надежный пароль:'))









#Функции: виды параметров, возвращение данных, виды аргументов.
#def define - определить
#DRY - don't repeat yourself

"""из чего состоит функция"""
# определение наименование(параметры):
#     тело функции
#     возвращание результата


# вызов функции
# наименование(аргументы)

# def some_name(name, surname="скажим фамилию"):
#     print(f'name: {name} surname {surname}')

# some_name('xleb', 'flour')
# some_name('isa')
# some_name(surname='okto',name= 'isko')

# some_name(input("имя"), input("фамилия"))

# word='python'
# count_letter = len(word)
# print (count_letter)


# length = 8
# width = 6
# squere_2 = length * width
# print (squere_2)

# length = 15
# width = 10
# squere_hall = length * width
# print (squere_hall)



# def get_square(length: int, width: int) -> int:
#     """получает длину и ширину. возвращает площадь"""
#     return length * width

# print(help(get_square))
# print(get_square.__doc)

# square2 = get_square(8, 6)
# squarehall = get_square(15,10)
# print (square2, "  ", squarehall)

# print(print.__doc__)
# print(help(print))


# def get_fullname(surname: str, name: str, thirdname: str) -> str:
#     """Фунция берет пользовательский ввод и возвращает его ФИО в формате AAA Ooo Uuu"""
#     if surname.isalpha() == False:
#         print("Ваша фамилия содержит неподдерживаемые символы")
#     else:
#         print("Ваше ФИО в формате AAA Ooo Uuu:", surname.upper(), name.title(), thirdname.title())

# your_fullname = get_fullname(input("Введите фамилию: "), input("Введите имя: "), input("Введите отчество: "))

# print(help(get_fullname))


# def plus(*args):
#     return sum(args)

# print( plus( 2, 3, 2,6,120,123))


# def menu (**kwargs):
#     return kwargs

# mon = menu (eat ='plov', drink = 'plov')
# print (mon)


