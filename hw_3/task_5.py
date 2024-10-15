# Задача 5. Нахождение анаграмм
# Напишите программу, которая принимает два слова и определяет, являются ли
# они анаграммами.
# Подсказка № 1
# Сначала проверьте, равна ли длина двух слов. Если они имеют разную длину, они не
# могут быть анаграммами.
# Подсказка № 2
# Создайте два пустых словаря для хранения частоты символов каждого слова. Один
# словарь для первого слова, другой для второго.
# Подсказка № 3
# Пройдитесь по каждому символу в первом слове и увеличьте счётчик в словаре.
# Повторите это для второго слова.
# Подсказка № 4
# После подсчета символов сравните оба словаря. Если они идентичны, слова являются
# анаграммами.

# антиквар - травинка

word_1 = input('Enter first word: ')
word_2 = input('Enter second word: ')

result = ''

if len(word_1) != len(word_2):
    result = f'Слово {word_1} не является анаграммой слова {word_2}'
else:
    lst_word_1 = []
    lst_word_2 = []
    lst_word_1.extend(word_1)
    lst_word_2.extend(word_2)
    result = f'Слово {word_1} является анаграммой слова {word_2}'
    for el in lst_word_1:
        if el in lst_word_2:
            lst_word_2.remove(el)
        else:
            result = f'Слово {word_1} не является анаграммой слова {word_2}'
            break

print(result)


# # perfect solution
# word1 = input("Введите первое слово: ")
# word2 = input("Введите второе слово: ")
#
# if len(word1) != len(word2):
#     print("Слова не являются анаграммами")
# else:
#     char_count1 = {}
#     char_count2 = {}
#     for char in word1:
#         if char in char_count1:
#             char_count1[char] += 1
#         else:
#             char_count1[char] = 1
#     for char in word2:
#         if char in char_count2:
#             char_count2[char] += 1
#         else:
#             char_count2[char] = 1
#
#     if char_count1 == char_count2:
#         print("Слова являются анаграммами")
#     else:
#         print("Слова не являются анаграммами")
