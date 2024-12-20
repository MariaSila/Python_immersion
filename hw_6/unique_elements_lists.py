# Задача 3. Модуль для нахождения уникальных для обоих списков
# элементов
# Создайте модуль с функцией, которая принимает два списка и возвращает
# список, содержащий только элементы, которые уникальны для обоих списков.
# Подсказка № 1
# Преобразуйте оба списка в множества с помощью функции set(). Это позволит легко
# выполнять операции над уникальными элементами.
# Подсказка № 2
# Используйте операции над множествами для нахождения элементов, которые
# уникальны для каждого из множества. set1 - set2 даст элементы, которые
# присутствуют в set1, но отсутствуют в set2. Аналогично, set2 - set1 даст
# элементы, присутствующие в set2, но отсутствующие в set1.
# Подсказка № 3
# Объедините два результата (set1 - set2 и set2 - set1) с помощью операции |
# (объединение множеств), чтобы получить все уникальные элементы.
# Подсказка № 4
# Преобразуйте множество уникальных элементов обратно в список с помощью функции
# list(), чтобы вернуть результат в виде списка.


def unique_elem_lists(lst1: list, lst2: list) -> list:
    d1 = set(lst1) - set(lst2)
    d2 = set(lst2) - set(lst1)
    uniq_set = d1.union(d2)
    return list(uniq_set)


lst1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
lst2 = [2, 2, 3, 3, 9, 9, 8, 8, 7, 7, 7]

print(unique_elem_lists(lst1, lst2))


# # perfect solution
# # unique_to_both_lists.py
# def unique_to_both_lists(list1, list2):
#     """
#     Функция для нахождения уникальных элементов в двух списках.
#     Аргументы:
#     list1 -- первый список
#     list2 -- второй список
#     Возвращает:
#     Список уникальных элементов, которые присутствуют только в одном
#     из двух списков.
#     """
#     set1, set2 = set(list1), set(list2)
#     unique_elements = (set1 - set2) | (set2 - set1)
#     return list(unique_elements)
#
#
# print(unique_to_both_lists([1, 2, 3], [3, 4,5]))
#
#
# # Чтобы использовать модуль unique_to_both_lists, создайте файл с именем
# # unique_to_both_lists.py и вставьте в него код выше. Затем вы можете использовать его
# # в другом скрипте следующим образом:
# #
# # import unique_to_both_lists
# # print(unique_to_both_lists.unique_to_both_lists([1, 2, 3], [3, 4,5]))
# # # Output: [1, 2, 4, 5]

