keywords = """
False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not
""".split()


dictionary = {}
count = 0
known = 0
unknown = 0
for keyword in keywords:
    while True:
        answer = input(f'проходили ли мы ключевое слово "{keyword}"? ')
        if answer == '1':
            known+=1
            break
        elif answer == '0':
            unknown +=1
            break
        else:
            print('Ответ приемлем лишь в формате: 1 или 0')
    dictionary[keyword] = answer
    count +=1


print(f'Всего слов: {count}')
print(f'Пройденные слова: {known}')
print(f'Непройденные слова: {unknown}')
print(f'В процентном соотношении пройдено: {100/count * known}' )
for i in dictionary:
    print('{',i,':', dictionary[i],'}')

"""ДОМАШНЕЕ ЗАДАНИЕ №8
1) Создать словарь из ключевых слов, где ключом будет слово а значением 1 или 0 в зависимости от знаем / не знаем
2) Вывести общее количество слов
3) Вывести количество пройденных слов
4) Вывести количество не пройденных слов
5) Вывести процентное соотношение 'пройдено из общего количества'
6) Вывести словарь в паре 'ключ: значение'
"""



