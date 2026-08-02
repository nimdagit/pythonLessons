
# #кортеж
# data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")

# #создание двух пустых списков
# designations = []
# codes = []

# #инициализация двух списков с помощью .isdigit который определит строковой объект это число или нет
# for d in data:
#     if d.isdigit() == True:
#         codes.append(d)
#     else:
#         designations.append(d)
# print (f'Наименования компаний:',designations)
# print (f'Коды:',codes)

# #создание словаря и его  инициализация
# operators = {}
# i = 0
# while i < len(designations):
#     operators[designations[i]] = codes[i]
#     i +=1
# print ("Словарь компаний и их кодов")
# for i in operators:
#     print (i,':', operators[i])

# #Удаление
# print ("Удаление недействующих операторов")
# operators.pop("Katel")
# del operators["Fonex"]
# for i in operators:
#     print (i,':', operators[i])

# #Добавление новых кодов с использованием списоков
# operators['O!'] = ['0505', '0705']
# operators.update({'Megacom': ['0550', '0990'], 'Beeline': ['0220', '0770']})

# print('Добавление новых кодов')
# for i in operators:
#     print(i, '-', operators[i])



# словарь, множество
# {key: value}

student = {
    'name': 'adil',
    'age': 18
}

print (student)
print (student['name'])
print (student['age'])
print (type(student))

print (student)

#add
student['height'] = 1.78
student.update({'country': 'kg', 'weight': 76, 'name': 'isa'})
print (student)


#edit
student['age'] = 19 
student['weight'] -=1.5
print (student)

#delete

student.pop('weight')
del student['height']

print (student)


for i in student:
    print(f'{i} -> {student[i]}')


# for key, value in student.items():
#     print(f'{key}, {value}')


