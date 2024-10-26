# Задание 1. Модуль для подсчета количества повторений слов
# Создайте модуль с функцией, которая получает список слов и возвращает
# словарь, в котором ключи — это слова, а значения — количество их повторений
# в списке.
# Подсказка № 1
# Начните с создания пустого словаря, который будет использоваться для хранения слов
# и их количества. В этом словаре ключами будут слова, а значениями — их количество.
# Подсказка № 2
# Проходите через каждый элемент (слово) в предоставленном списке слов.
# Используйте цикл for для этого.
# Подсказка № 3
# В словаре используйте метод get() для получения текущего значения по ключу. Если
# ключа нет в словаре, get() вернет значение по умолчанию, которое вы указываете (в
# данном случае 0).
# Подсказка № 4
# Обновляйте количество повторений слова в словаре, добавляя 1 к текущему
# значению. Это позволяет аккуратно увеличивать счетчик для каждого слова.


# # first way
# _data = {}
#
#
# def count_repeat(words: list):
#     unique = set(words)
#     for el in unique:
#         count = words.count(el)
#         _data[el] = _data.get(el, 0) + count
#
#
# count_repeat(['end', 'dog', 'wow', 'cat', 'dog', 'end', 'dog'])
# count_repeat(['wow', 'dog', 'dog'])
# print(*_data.items())


# second way
def count_repeat(words: list) -> dict:
    data = {}
    unique = set(words)
    for el in unique:
        count = words.count(el)
        data[el] = count
    return data


print(count_repeat(['end', 'dog', 'wow', 'cat', 'dog', 'end', 'dog']))
print(count_repeat(['wow', 'dog', 'dog']))


# perfect solution
# word_count.py
# def count_word_occurrences(words):
#     word_count = {}
#     for word in words:
#         word_count[word] = word_count.get(word, 0) + 1
#     return word_count
#
#
# print(count_word_occurrences(['apple', 'banana', 'apple', 'orange']))


# Чтобы использовать модуль word_count, создайте файл с именем word_count.py и
# вставьте в него код выше. Затем вы можете использовать его в другом скрипте
# следующим образом:
# import word_count
# print(word_count.count_word_occurrences(['apple', 'banana', 'apple','orange']))