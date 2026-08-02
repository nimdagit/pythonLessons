# name = input("what's your name? ").title()
# surname = 'admin'

# age = int (input (f'{name}, please enter your age: '))
# height = 1.78
# current_year = 2026
# born = (current_year - age)


# print(f'name: {name} surname: {surname} born: {born}')


print ('Введите ваши расходы за')
md = int(input('Понедельник: '))
tud = int(input('Вторник: '))
wd = int(input('Среду: '))
thd = int(input('Четверн: '))
fd = int(input('Пятницу: '))
st = int(input('Субботу: '))
sn = int(input('Воскресенье: '))


print ('Ваши общие расходы за неделю равны: ', md+tud+wd+thd+fd+st+sn)
print ('Ваш средний расход в день равен: ', (md+tud+wd+thd+fd+st+sn)//7)