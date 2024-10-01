# Задача 3. Перевод целого числа в римское число
# Программа принимает целое число и возвращает его римское представление в
# виде строки.
# Подсказка № 1
# Определите два массива: один для числовых значений (например, 1000, 900, 500 и так
# далее), другой для их римских эквивалентов (например, "M", "CM", "D" и так далее).
# Подсказка № 2
# Используйте цикл while, чтобы повторять процесс преобразования, пока ваше число
# больше нуля. Внутри цикла while используйте другой цикл for, чтобы определить,
# сколько раз текущее значение из массива может быть вычтено из числа.
# Подсказка № 3
# Для каждого значения из массива чисел добавляйте соответствующий римский символ
# к результирующей строке. Уменьшайте число на соответствующую величину каждый
# раз, когда добавляете римский символ.
# Подсказка № 4
# После обработки текущего значения числа, переходите к следующему элементу
# массивов значений и символов, чтобы продолжить процесс преобразования.

# Вариант 1
ARABIC = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
ROMAN = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')

n = int(input('Enter arabic integer: '))
num_arabic = n
num_roman = ''

for i in range(len(ARABIC)):
    res = num_arabic // ARABIC[i]

    if res == 0:
        continue
    else:
        num_roman += res * ROMAN[i]
        num_arabic %= ARABIC[i]

print(num_roman)


# # Вариант 2
# UNITS = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
# TENS = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
# HUNDREDS = ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
# THOUSAND = ['M', 'MM', 'MMM', 'MV', 'V', 'VM', 'VMM', 'VMMM', 'MX']
#
# n = int(input('Enter arabic integer: '))
# num_arabic = n
# num_roman = ''
#
# tho = num_arabic // 1000
# if tho > 0:
#     num_roman += THOUSAND[tho-1]
#
# hun = (num_arabic - 1000 * tho) // 100
# if hun > 0:
#     num_roman += HUNDREDS[hun-1]
#
# ten = (num_arabic - 1000 * tho - 100 * hun) // 10
# if ten > 0:
#     num_roman += TENS[ten - 1]
#
# uni = num_arabic - 1000 * tho - 100 * hun - 10 * ten
# if uni > 0:
#     num_roman += UNITS[uni - 1]
#
# print(num_roman)


# # Идеальное решение
# num = int(input("Введите целое число: "))
# # Массив значений чисел в десятичной системе
# val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
# # Массив соответствующих римских символов
# syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
#
# roman_num = ''  # Инициализируем пустую строку для результата
# i = 0           # Индекс для итерации по массивам
#
# while num > 0:  # Пока значение num больше 0
#     # Выполняем цикл для текущего значения в массиве val
#     for _ in range(num // val[i]): # num // val[i] дает количество раз, которое val[i] помещается в num
#         roman_num += syb[i] # Добавляем соответствующий римский символ в результат
#         num -= val[i] # Уменьшаем значение num на val[i]
#     i += 1 # Переходим к следующему значению в массиве
# # Печатаем результат
# print("Результат:", roman_num)
