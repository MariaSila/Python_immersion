# Задача 4. Генератор подстрок
# Напишите генераторную функцию substrings(s), которая принимает строку
# s и возвращает генератор всех возможных подстрок этой строки.
# На вход подается строка abc
# На выходе будут выведены обозначения:
# a
# ab
# abc
# b
# bc
# c
# Подсказка № 1
# Чтобы создать генератор подстрок, начните с определения всех возможных начальных
# и конечных позиций для подстрок. Перебирайте начальные позиции, затем для каждой
# начальной позиции перебирайте все возможные конечные позиции.
# Подсказка № 2
# Используйте два вложенных цикла для генерации всех подстрок. Внешний цикл будет
# проходить по начальным позициям подстрок, а внутренний цикл будет проходить по
# конечным позициям, начиная с текущей начальной позиции и до конца строки.
# Подсказка № 3
# Внутри вложенного цикла используйте оператор yield для возврата подстроки,
# которая начинается на текущей начальной позиции и заканчивается на текущей
# конечной позиции. Убедитесь, что конечная позиция не выходит за пределы строки
# s.count(s[0]) > 1

# def substrings(s):
#     prefix_str = [i for i in s]
#     suffix_str = [s[1:i] for i in range(2, len(s) + 1)]
#     for pr in prefix_str:
#         if pr == prefix_str[0]:
#             yield pr
#         for sf in suffix_str:
#             if sf.startswith(pr):
#                 yield sf
#             elif pr == prefix_str[-1]:
#                 yield pr
#                 break
#             else:
#                 yield pr + sf
#
#
# for i in substrings('abc'):
#     print(i)


# perfect solution
def substrings(s):
    length = len(s)
    for start in range(length):
        for end in range(start + 1, length + 1):
            yield s[start:end]


for substring in substrings('abcdef'):
    print(substring)
