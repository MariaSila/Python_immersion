# Задача 5. Модуль для проверки ферзей
# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него
# напишите код, решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно
# расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8
# ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 -
# координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют
# - ложь.
# Подсказка № 1
# Убедитесь, что ферзи не находятся в одной строке или столбце, так как это приведет к
# их атаке друг на друга. Для проверки можно использовать координаты столбца и
# строки каждого ферзя.
# Подсказка № 2
# Ферзи, находящиеся на одной диагонали, также будут атаковать друг друга. Проверьте,
# находятся ли ферзи на одной диагонали, используя разность между строками и
# столбцами.
# Подсказка № 3
# Напишите вспомогательную функцию внутри основной функции для проверки,
# находится ли конкретная позиция под атакой других ферзей. Это улучшит читаемость
# кода.
# Подсказка № 4
# Убедитесь, что каждая из 8 позиций на доске уникальна по строкам и столбцам. Это
# гарантирует, что нет двух ферзей в одной строке или столбце.

from random import randint, shuffle

ROW = 0
COLUMN = 1

# 1 способ с условием: что каждая из 8 позиций на доске уникальна по строкам и столбцам.
# Это гарантирует, что нет двух ферзей в одной строке или столбце.


def generator_coordinates(count: int) -> list:
    coordinates = []
    rows = [i for i in range(1, count + 1)]
    columns = [i for i in range(1, count + 1)]
    for i in range(count):
        shuffle(rows)
        shuffle(columns)
        row = rows.pop()
        column = columns.pop()
        coordinates.append((row, column))
    return coordinates


def is_take_queen() -> bool:
    lst_coord = generator_coordinates(8)
    print(lst_coord)
    length = len(lst_coord)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if abs(lst_coord[i][ROW] - lst_coord[j][ROW]) == abs(lst_coord[i][COLUMN] - lst_coord[j][COLUMN]):
                return False
    return True


# 2 способ с условием: что исключаются ситуации когда фигуры стоят в одинаковой позиции,
# но без учета, что восемь позиций уникальны по строкам и столбцам
def generator_coordinates2(count: int) -> list:
    coordinates = []
    for i in range(count):
        coord = (randint(1, 8), randint(1, 8))
        if coord in coordinates:
            coord = (randint(1, 8), randint(1, 8))
        coordinates.append(coord)
    return coordinates


def is_take_queen2() -> bool:
    lst_coord = generator_coordinates2(8)
    print(lst_coord)
    length = len(lst_coord)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if lst_coord[i][ROW] == lst_coord[j][ROW]:
                return False
            elif lst_coord[i][COLUMN] == lst_coord[j][COLUMN]:
                return False
            elif abs(lst_coord[i][ROW] - lst_coord[j][ROW]) == abs(lst_coord[i][COLUMN] - lst_coord[j][COLUMN]):
                return False
    return True


print(is_take_queen())
print(is_take_queen2())


# # perfect solution
# # chess.py
# def are_queens_safe(positions):
#     """
#     Проверяет, не бьют ли друг друга ферзи на доске 8x8.
#     Аргументы:
#     positions -- список кортежей, где каждый кортеж содержит
#     координаты ферзя (строка, столбец)
#     Возвращает:
#     True, если ферзи не бьют друг друга; False в противном случае
#     """
#     def is_under_attack(row, col):
#         """
#         Проверяет, атакуется ли позиция (row, col) другими ферзями.
#         Аргументы:
#         row -- строка ферзя
#         col -- столбец ферзя
#         Возвращает:
#         True, если позиция находится под атакой; False в противном
#         случае
#         """
#         for i in range(8):
#             if i != row:
#                 if positions[i][1] == col or abs(positions[i][0] - row) == abs(positions[i][1] - col):
#                     return True
#         return False
#
#     for i in range(8):
#         if is_under_attack(positions[i][0], positions[i][1]):
#             return False
#     return True
#
#
# def generate_random_queens_placement():
#     """
#     Генерирует случайную расстановку 8 ферзей.
#     Возвращает:
#     Список из 8 кортежей, каждый из которых содержит случайные
#     координаты ферзя
#     """
#     import random
#
#     return [(i, random.randint(1, 8)) for i in range(8)]
#
#
# def print_valid_placements(num_placements=4):
#     """
#     Выводит заданное количество случайных валидных расстановок
#     ферзей.
#     Аргументы:
#     num_placements -- количество случайных валидных расстановок для
#     вывода
#     """
#     count = 0
#     while count < num_placements:
#         placement = generate_random_queens_placement()
#         if are_queens_safe(placement):
#             print(placement)
#             count += 1
#
#
# print(are_queens_safe(generate_random_queens_placement()))


# # Пример использования:
# # main.py
# import sys
# import chess
# # Проверяем количество аргументов командной строки
# if len(sys.argv) != 9:
#     print("Usage: python main.py row1 col1 row2 col2 ... row8 col8")
#     sys.exit(1)
#
# # Получаем координаты ферзей из аргументов командной строки
# positions = [(int(sys.argv[i]), int(sys.argv[i+1])) for i in range(1, len(sys.argv), 2)]
#
# # Проверяем, не бьют ли ферзи друг друга
# if chess.are_queens_safe(positions):
#     print("True")
# else:
#     print("False")
