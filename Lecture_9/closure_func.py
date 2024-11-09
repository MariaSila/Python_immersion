from typing import Callable


# # STEP 1 Рассмотрим простой пример функции:
# def add_str(a: str, b: str) -> str:
#     return a + ' ' + b
#
#
# print(add_str('Hello', 'world!'))


# # STEP 2 Создадим замыкание через передачу в функцию другую функцию
# возвращая из внешней функции внутреннюю создаём замыкания.
# # Результат получили такой же, но код работает иначе
# def add_one_str(a: str) -> Callable[[str], str]:
#     def add_two_str(b: str) -> str:
#         return a + ' ' + b
#     return add_two_str
#
#
# print(add_one_str('Hello')('world!'))


# STEP 3 Замыкаем функцию с параметрами.
# Создали две переменные hello и bye и поместили в них результат работы функции add_one_str с разными
# аргументами. Теперь мы можем вызывать новые функции и получать объединённые
# строки передавая только окончание. Первая часть строки оказалась замкнута в
# локальной области видимости. И у каждой из двух новых функций область своя и
# начало строки своё.
# def add_one_str(a: str) -> Callable[[str], str]:
#     def add_two_str(b: str) -> str:
#         return a + ' ' + b
#     return add_two_str
#
#
# hello = add_one_str('Hello')
# bye = add_one_str('Good bye')
#
# print(hello('world!'))
# print(hello('friend!'))
# print(bye('wonderful world!'))
# print(f'{type(add_one_str)=}, {add_one_str.__name__=}, {id(add_one_str)=}')
# print(f'{type(hello)=}, {hello.__name__=}, {id(hello)=}')
# print(f'{type(bye)=}, {bye.__name__=}, {id(bye)=}')


# STEP 4.1 Замыкаем изменяемые и неизменяемые объекты
# Во внешнюю функцию добавлен список names. При каждом вызове внутренней
# функции в список добавляется новое значение из параметра b и возвращается
# полное содержимое списка в виде строки. У каждой из двух функций hello и bye
# оказывается свой список names. Они не связаны между собой, но каждый хранит
# список имён до конца работы программы. Обратите внимание, что list является
# изменяемым типом данных
# def add_one_str(a: str) -> Callable[[str], str]:
#     names = []
#
#     def add_two_str(b: str) -> str:
#         names.append(b)
#         return a + ', ' + ', '.join(names)
#     return add_two_str
#
#
# hello = add_one_str('Hello')
# bye = add_one_str('Good bye')
#
# print(hello('Alex'))
# print(hello('Karina'))
# print(bye('Alina'))
# print(hello('John'))
# print(bye('Neo'))


# STEP 4.2 перепишем код и заменим list на неизменяемый str
# ВАЖНО - неизменяемый тип данных у строки text. Без добавления строчки
# кода nonlocal text была бы получена ошибка UnboundLocalError: local variable 'text'
# referenced before assignment. Мы явно указали, что хотим обращаться к
# неизменяемому объекту для изменения его значения.
# Изменения способа получения строки c join для списка на конкатенацию для строки
# не принципиально. Но стоит помнить, что сложение строк более дорогая операция
# по времени и по памяти, особенно если она находится внутри цикла.
# def add_one_str(a: str) -> Callable[[str], str]:
#     text = ''
#
#     def add_two_str(b: str) -> str:
#         nonlocal text
#         text += ', ' + b
#         return a + text
#     return add_two_str
#
#
# hello = add_one_str('Hello')
# bye = add_one_str('Good bye')
#
# print(hello('Alex'))
# print(hello('Karina'))
# print(bye('Alina'))
# print(hello('John'))
# print(bye('Neo'))


