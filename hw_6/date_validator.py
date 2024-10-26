# Задача 4. Модуль для проверки даты
# Создайте модуль и напишите в нём функцию, которая получает на вход дату в
# формате DD.MM.YYYY Функция возвращает истину, если дата может существовать
# или ложь, если такая дата невозможна. Для простоты договоримся, что год
# может быть в диапазоне [1, 9999]. Весь период (1 января 1 года - 31 декабря 9999
# года) действует Григорианский календарь. Проверку года на високосность
# вынести в отдельную защищённую функцию.
# Подсказка № 1
# Используйте метод split('.') для разделения строки даты на день, месяц и год.
# Преобразуйте каждую из частей в целые числа с помощью map(int, ...).
# Подсказка № 2
# Проверьте, что месяц находится в диапазоне от 1 до 12 включительно. Если нет, дата
# считается невалидной. Аналогично сделайте с годами и днями.
# Подсказка № 3
# Используйте datetime(year, month, day) для проверки корректности даты.
from datetime import datetime


def is_leap(year: int) -> bool:
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0


def is_valid_date(date: str) -> bool:
    try:
        day, month, year = map(int, date.split('.'))
        datetime(year, month, day)
    except ValueError:
        return False
    if year < 1 or year > 9999 or month < 1 or month > 12 or day < 1 or day > 31:
        return False
    elif month in (4, 6, 9, 11):
        return day < 31
    elif month == 2:
        if is_leap(year):
            return day < 30
        else:
            return day < 29
    else:
        return True


print(is_valid_date('15.04.10000'))
print(is_valid_date('01.13.2100'))
print(is_valid_date('32.11.2011'))
print(is_valid_date('29.02.2000'))
print(is_valid_date('29.02.2023'))
print(is_valid_date('28.02.2100'))


# # perfect solution
# # date_validator.py
# def _is_leap_year(year):
#     """
#     Возвращает True, если год високосный, иначе False.
#     Аргументы:
#     year -- год для проверки
#     Возвращает:
#     True, если год високосный; False в противном случае
#     """
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
#
#
# def is_valid_date(date_str):
#     """
#     Проверяет, является ли дата в формате DD.MM.YYYY валидной.
#     Аргументы:
#     date_str -- строка с датой в формате DD.MM.YYYY
#     Возвращает:
#     True, если дата валидная; False в противном случае
#     """
#     if len(date_str) != 10:
#         return False
#
#     parts = date_str.split('.')
#     if len(parts) != 3:
#         return False
#     try:
#         day, month, year = map(int, parts)
#     except ValueError:
#         return False
#     if not (1 <= month <= 12):
#         return False
#     if not (1 <= day <= 31):
#         return False
#     if month in [4, 6, 9, 11] and day > 30:
#         return False
#     if month == 2:
#         if _is_leap_year(year) and day > 29:
#             return False
#         elif not _is_leap_year(year) and day > 28:
#             return False
#     return True
#
#
# print(is_valid_date('15.04.10000'))
# print(is_valid_date('01.13.2100'))
# print(is_valid_date('32.11.2011'))
# print(is_valid_date('29.02.2000'))
# print(is_valid_date('29.02.2023'))
# print(is_valid_date('28.02.2100'))


# # Чтобы использовать модуль date_validator, создайте файл с именем date_validator.py и
# # вставьте в него код выше. Затем вы можете использовать его в другом скрипте
# # следующим образом:
# # main.py
# import sys
# # import date_validator
# # Проверяем количество аргументов командной строки
# if len(sys.argv) != 2:
#     print("Usage: python date_validator.py DD.MM.YYYY")
#     sys.exit(1)
# # Получаем дату из аргументов командной строки
# date_input = sys.argv[1]
# # Проверяем, является ли дата валидной
# if date_validator.is_valid_date(date_input):
#     print("True")
# else:
#     print("False")