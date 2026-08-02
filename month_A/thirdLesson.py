while True:
    userWord = input('Enter your word or "exit" for the end the programm: ')
    if userWord in ('EXIT', 'Exit', 'exit'):
        break
    print(f'Слово: ', userWord)
    print (f'Количество букв: ', userWord.count('')-1)

    vowel = 0
    consonant = len(userWord)
    i = 0
    while i < len(userWord):
        letter = userWord[i]
        if letter in 'aeiouyAEIOUYАОУЭЫЯЕЁЮИаоуэыяеёюи':
            vowel +=1
            consonant = consonant -1
        i += 1
    
    vowelProcent = 100 / len(userWord) * vowel
    consonantProcent = 100 - vowelProcent
    print (f'Гласных букв: ', vowel)
    print (f'Согласных букв: ', consonant)
    print (f'Гласные/Согласные: ',vowelProcent,'% ', consonantProcent,'%')

# TODO: улучшить код







#ОПЕРАТОРЫ: ПРИНАДЛЕЖНОСТИ, НАЗНАЦЧЕНИЯ
#ЦИКЛЫ
#ОПЕРАТОРЫ НАЗНАЧЕНИЯ
# num = 5
# num = num + 3
# num += 3
# num **= 2
# print ( num )


# word = 'python'
# word += 'KG'
# word *= 2
# print (word)

# #ОПЕРАТОР ПРИНАДЛЕЖНОСТИ "IN"
# print ('p' in 'python')
# print ('yp' in 'python')

# print (11 in range(1, 11))

# counter = 0
# while counter < 100:
#     counter +=1
    
#     if counter == 72:
#         break


#     if counter in (24, 33, 14, 67):
#         continue
    
#     print(counter)



# for num in range(1,11):
#     if num in(7,8,9):
#         print ('...')
#         continue
#     print (num)




# word = 'KYRGYZSTAN'
# for letter in word:
#     if letter == 'S':
#         break
#     if letter in 'YR':
#         continue
#     print (letter)



# total_sum = int(input())
# percent = 0.1
# for i in range (1, 6):
#     total_sum = total_sum + total_sum * percent
#     print(f'деньги за {i} год: ', total_sum)
#     i +=1


# word = 'qwer'
# print('qw' in word)  # Выведет: True




