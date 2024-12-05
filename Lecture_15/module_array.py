# Модуль array

# --------------------------------------------------------------------------
# А вот ещё один модуль, предоставляющий доступ к типу данных массив. Как вы
# помните список list является массивом ссылок на объекты. А сами объекты хранятся
# отдельно, вне массива. array из модуля array является классическим массивом.
# Внутри него можно хранить целые или вещественные числа, а также символы Unicode.
# Первый аргумент — строковой символ код типа. Буква указывает на то какие
# данные хранятся в массиве и выделяет нужное число байт под данные.
# Вторым аргументом передают последовательность для помещения в массив.
# Переменная typecodes выводит все допустимые коды типа:
#       ● 'b' — целое со знаком, 1 байт
#       ● 'B' — целое без знака, 1 байт
#       ● 'u' — Юникод-символ в 2 или 4 байта
#       ● 'h' — целое со знаком, 2 байта
#       ● 'H' — целое без знака, 2 байта
#       ● 'i' — целое со знаком, 4 байта
#       ● 'I' — целое без знака, 4 байта
#       ● 'l' — целое со знаком, 4 байта
#       ● 'L' — целое без знака, 4 байта
#       ● 'q' — целое со знаком, 8 байт
#       ● 'Q' — целое без знака, 8 байт
#       ● 'f' — вещественное обычной точности, 4 байта
#       ● 'd' — вещественное двойной точности, 8 байт

# from array import array, typecodes
#
# byte_array = array('B', (1, 2, 3, 255))
# print(byte_array)
# print(typecodes)


# ------------------------------------------------------------------------------
# Массивы поддерживают методы списка list, поэтому использование их интуитивно
# понятно. Привыкать надо лишь к указанию хранимого типа данных.

# from array import array
#
# long_array = array('l', [-6000, 800, 100500])
# long_array.append(42)
# print(long_array)
# print(long_array[2])
# print(long_array.pop())


# ------------------------------------------------------------------------------
# При этом массив не позволит добавить значение, если оно выходит за пределы
# диапазона, заданного кодом типа при создании. Так же будет поднята ошибка при
# несоответствии типа.
# Массивы array являются более экономичной по памяти структурой данных, чем
# списки list.

# from array import array
#
# long_array = array('l', [-6000, 800, 100500])
# long_array.append(2**32) # OverflowError: Python int too large to convert to C long
# long_array.append(3.14) # TypeError: 'float' object cannot be interpreted as an integer


# ----------------------------------------------------------------------------------
# Задание
# Перед вами несколько строк кода. Напишите что выведет программа, не запуская
# код. У вас 3 минуты.

# from collections import namedtuple
#
# Data = namedtuple('Data', ['mathematics', 'chemistry', 'physics', 'genetics'], defaults=[5, 5, 5, 5])
# d = {
#     'Ivanov': Data(4, 5, 3, 5),
#     'Petrov': Data(physics=4, genetics=3),
#     'Sidorov': Data(),
# }