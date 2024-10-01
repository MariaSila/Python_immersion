# Задача 4. Сумма и произведение дробей
# Программа принимает две строки вида "a/b" - дробь с числителем и
# знаменателем. Возвращает сумму и произведение дробей. Для проверки
# используется модуль fractions.
# Подсказка № 1
# Используйте метод split('/') для разделения строки на числитель и знаменатель.
# Преобразуйте полученные части в целые числа с помощью функции map(int, ...).
# Подсказка № 2
# Импортируйте класс Fraction из модуля fractions, чтобы легко работать с
# дробями. Создайте объекты Fraction, передав числитель и знаменатель.
# Подсказка № 3
# Используйте операторы + и * для нахождения суммы и произведения дробей
# соответственно. Класс Fraction автоматически упрощает дроби и выполняет
# операции корректно.

import math
import fractions

NUMERATOR = 0
DENOMINATOR = 1

num_1 = input('Enter first fraction in format a/b: ')
num_2 = input('Enter second fraction in format a/b: ')
sum_frac = [NUMERATOR, DENOMINATOR]
product_frac = [NUMERATOR, DENOMINATOR]

# преобразуем полученное значение от пользователя в список
frac_1 = list(map(int, num_1.split('/')))
frac_2 = list(map(int, num_2.split('/')))

# lcm - least common multiple (наименьшее общее кратное)
lcm = int(frac_1[DENOMINATOR] * frac_2[DENOMINATOR] / math.gcd(frac_1[DENOMINATOR], frac_2[DENOMINATOR]))

# увеличиваем числитель соответственно lcm
summand = int(frac_1[NUMERATOR] * lcm / frac_1[DENOMINATOR])    # summand -первое слагаемое
addend = int(frac_2[NUMERATOR] * lcm / frac_2[DENOMINATOR])     # addend - второе слагаемое

# вычисляем сумму дробей
sum_frac[NUMERATOR] = summand + addend
sum_frac[DENOMINATOR] = lcm

# вычисляем произведение дробей
product_frac[NUMERATOR] = frac_1[NUMERATOR] * frac_2[NUMERATOR]
product_frac[DENOMINATOR] = frac_1[DENOMINATOR] * frac_2[DENOMINATOR]


def gdc_frac(array):
    # вычисляем НОД для сокращения дроби
    gcd_f = math.gcd(array[NUMERATOR], array[DENOMINATOR])
    # сокращаем дроби если возможно
    if gcd_f > 1:
        array[NUMERATOR] = int(array[NUMERATOR] / gcd_f)
        array[DENOMINATOR] = int(array[DENOMINATOR] / gcd_f)
    return array


sum_frac = gdc_frac(sum_frac)
product_frac = gdc_frac(product_frac)

# проверка
f1 = fractions.Fraction(frac_1[NUMERATOR], frac_1[DENOMINATOR])
f2 = fractions.Fraction(frac_2[NUMERATOR], frac_2[DENOMINATOR])
f_sum = f1 + f2
f_prod = f1 * f2

print(f'{num_1} + {num_2} = {sum_frac[NUMERATOR]}/{sum_frac[DENOMINATOR]}, проверка {f_sum}')
print(f'{num_1} * {num_2} = {product_frac[NUMERATOR]}/{product_frac[DENOMINATOR]}, проверка {f_prod}')


# # Идеальное решение
# from fractions import Fraction
#
# frac1 = input("Введите первую дробь (a/b): ")   # Вводим первую дробь
# frac2 = input("Введите вторую дробь (a/b): ")   # Вводим вторую дробь
#
# # Разделяем строки и преобразуем числитель и знаменатель первой дроби в целые числа
# numerator1, denominator1 = map(int, frac1.split('/'))
#
# # Разделяем строки и преобразуем числитель и знаменатель второй дроби в целые числа
# numerator2, denominator2 = map(int, frac2.split('/'))
#
# # Создаем объекты Fraction для первой и второй дроби
# f1 = Fraction(numerator1, denominator1)
# f2 = Fraction(numerator2, denominator2)
#
# sum_frac = f1 + f2  # Находим сумму дробей
# product_frac = f1 * f2  # Находим произведение дробей
#
# print("Сумма:", sum_frac)
# print("Произведение:", product_frac)



