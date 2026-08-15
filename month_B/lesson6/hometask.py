from random import randint

# 1. Написать функцию bubble_sort или selection_sort, принимающую в качестве входящего параметра не отсортированный список.
# 2. Алгоритм функции должен сортировать список методом пузырьковой сортировки или методом сортировки выбором.
# 3. Функция в итоге должна возвращать отсортированный список. Применить 1 раз данную функцию

def bubble_sort(some_list: list):


    for i in range(0,M-1):
        for j in range(0, M-1):
            if some_list[j] > some_list[j+1]:
                temp = some_list[j+1]
                some_list[j+1] = some_list[j]
                some_list[j] = temp

    return some_list


M = 53
some_list = []
for i in range(0, M):
    some_list.append(randint(0,M-1))
print(f'{some_list} --- Не отсортированный список')
print(f'{bubble_sort(some_list)} --- Отсортирован пузыриком')

# 4. Написать функцию binary_search, принимающую в качестве входящего параметра элемент для поиска и список в котором необходимо искать.
# 5. Алгоритм должен искать с помощью двоичного поиска, изображенного на блок-схеме презентации.
# 6. Функция в итоге должна распечатать результат. Применить 1 раз эту функцию

def binary_search(val,arr):
    N = len(arr)
    result = False
    first = 0
    last = N - 1
    pos = None
    while first <= last:
        middle = (first + last) // 2
        if val == arr[middle]:
            first = middle
            last = first
            result = True
            pos = middle
            break

        elif val > arr[middle]:
            first = middle + 1
        else:
            last = middle - 1


    if result == True:
        print('Элемент найден на позиции')
        print(f'{pos}')
    else:
        print('Элемент не найден')

arr = list(range(1, 5000 + 1)) # Создаем отсортированный список от 1 до 5000


user_input = int(input('Введите число которое хотите найти: '))



print (arr)
binary_search(user_input,arr)