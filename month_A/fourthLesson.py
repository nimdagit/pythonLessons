dataTuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []


for symbol in dataTuple:
    if type(symbol) == str:
        letters.append(symbol)
    else:
        numbers.append(symbol)


print (f'Списки инициализированы', letters, numbers)


numbers.remove(6.13)


print (f'Удалено 6.13',numbers)

deleted = numbers.pop(0)
letters.append(deleted)
print (f'True был удален из numbers и добавлен в letters',letters)


numbers.insert(1,2)
print (f'Цифра 2 была добавлена между 3 и 1',numbers)

numbers.sort()
print (f'сортировка',numbers)

letters.reverse()
print (f'список был реверснут',letters)


letters[1] = 'x'
letters [2]='l' 
letters [3] = 'e'
letters [4] = 'b'
print (f'некоторые символы изменены',letters)

# i = 0
# for symbol in numbers:
#     numbers[i] = symbol ** 2
#     i +=1
numsq = [x**2 for x in numbers]
print (f'список numbers возведен в квардрат',numsq)

lettersTuple = tuple(letters)
numbersTuple = tuple(numbers)

print (f'Из списков были созданы кортежи',lettersTuple , numbersTuple)


#СПИСКИ-lists, КОРТЕЖИ. ИНДЕКСЫ И СРЕЗЫ. ВСТРОЕННЫЕ ФУНКЦИИ К НАБОРАМ ЭЛЕМЕНТОВ. 
#СПИСКОВОЕ ВКЛЮЧЕНИЕ List comprehension

#КОРТЕЖИ
# numbers = (1,2,3,4,5)
# print (numbers)
# print (type(numbers))


#СПИСКОВОЕ ВКЛЮЧЕНИЕ List comprehension. [объект цикл условие]
# cities = ['tokmok', 'kemin', 'bish', 'karakol', 'kant']
# print (cities)

# citiesNew = [city.title() for city in cities if city.startswith('k')]
# citiesNew = [city.title() for city in cities if 'i' in city]

# print (citiesNew)


# #ВСТРОЕННЫЕ ФУНКЦИИ К НАБОРАМ ЭЛЕМЕНТОВ
# numbers = [21, 32, 13, 4, 15]

# print (len(numbers))
# print (min(numbers))
# print (max(numbers))
# print (sum(numbers))


# numbers = [1,2,3,4,5]


# #ДОБАВЛЕНИЕ
# print(numbers)

# numbers.append(6)
# print (numbers)

# numbers.insert(0, 0.5)
# print (numbers)

# numbers.extend([7,8,9])
# print (numbers)


#РЕДАКТИРОВАНИЕ
# numbers.reverse()
# print (numbers)

# numbers.sort()
# print (numbers)


# numbers.sort(reverse=True)
# print (numbers)

# numbers[1] = 10
# print (numbers)


#УДАЛЕНИЕ
# deleted = numbers.pop(0)
# print (numbers)
# print (deleted)

# numbers.remove(4)
# print (numbers)

# del numbers [-2:]
# print (numbers)
# numbers.clear()
# print (numbers)

# numbers = [1, 5, 8, 3, 9]
# print (numbers)
# print (type(numbers ))


# #СРЕЗЫ [start:stop:step]
# print (numbers[2:5:1])
# print ('python'[::-1])
# print (numbers[::])
# print (numbers[::-1])
# print (numbers[2::])
# print (numbers[:2])
# print (numbers[::2])


# #ИНДЕКСЫ
# print (numbers[1])
# print (numbers[4])
# print (numbers[-3])




# cities = ['Bish', 'Osh', 'Moscow', 'St-Peterburg', 'New-York', 'Berlin', 'Tokyo']
# print (cities)

# cities.sort()
# print(cities)

# print (cities[0])

# print (cities[5:7:1])

# cities[1] = 'Frunze'
# print (cities)

# deleted = cities.pop(2)
# print(cities)

# print (deleted)