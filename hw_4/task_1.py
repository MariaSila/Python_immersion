# Задание 1. Апгрейд калькулятора
# Степан использует калькулятор для расчёта суммы и разности чисел, но на
# работе ему требуются не только обычные арифметические действия. Он ничего
# не хочет делать вручную, поэтому решил немного расширить функционал
# калькулятора.
# Напишите программу, запрашивающую у пользователя число и действие,
# которое нужно сделать с числом: вывести сумму его цифр, максимальную или
# минимальную цифру. Каждое действие оформите в виде отдельной функции, а
# основную программу зациклите.
# Запрошенные числа должны передаваться в функции суммы, максимума и
# минимума при помощи аргументов.
# Подсказка № 1
# Создайте функцию для расчёта суммы цифр числа. В этой функции нужно
# использовать цикл, чтобы извлекать и суммировать каждую цифру числа. Не забудьте
# использовать оператор % для получения последней цифры и // для удаления
# последней цифры из числа.
# Подсказка № 2
# Создайте функцию для нахождения максимальной цифры числа. В этой функции также
# используйте цикл для извлечения и сравнения каждой цифры, чтобы определить
# максимальное значение.
# Подсказка № 3
# Создайте функцию для нахождения минимальной цифры числа. Начните с
# предположения, что минимальная цифра равна последней цифре числа. Сравните её
# с другими цифрами в цикле и обновите минимальное значение, если найдёте
# меньшую цифру.
# Подсказка № 4
# Создайте основной цикл программы, который будет запрашивать у пользователя число
# и действие. В зависимости от выбора действия (1, 2, 3), вызывайте соответствующую
# функцию для обработки числа.

def sum_digits_number(num: int) -> int:
    if num == 0:
        return 0
    if num < 0:
        num = abs(num)
    result = 0
    while num:
        result += num % 10
        num //= 10
    return result


def max_digit_number(num: int) -> int:
    if num < 0:
        num = abs(num)
    max_digit = num % 10
    while num:
        n = num // 10 % 10
        if max_digit < n:
            max_digit = n
        num //= 10
    return max_digit


def min_digit_number(num: int) -> int:
    if num < 0:
        num = abs(num)
    min_digit = num % 10
    while num:
        if num // 10 == 0:
            return min_digit
        n = num // 10 % 10
        if min_digit > n:
            min_digit = n
        num //= 10
    return min_digit


while True:
    number = int(input('Enter number: '))
    action = input(f'1 - sum digits number\
                   \n2 - max digit\
                   \n3 - min digit\
                   \n0 - exit\
                    \nSelect action: ')
    match action:
        case '1':
            res = sum_digits_number(number)
            print(f'Сумма цифр числа {number} равна {res}')
        case '2':
            res = max_digit_number(number)
            print(f'В числе {number} самая большая цифра {res}')
        case '3':
            res = min_digit_number(number)
            print(f'В числе {number} самая маленькая цифра {res}')
        case '0':
            break
        case _:
            print('Неверная команда')


# # perfect solution
# def digits_summ(num):
#     summ = 0
#     while num > 0:
#         digit = num % 10
#         summ += digit
#         num //= 10
#     print('Сумма цифр:', summ)
#
#
# def max_digit(num):
#     maximum = 0
#     while num > 0:
#         digit = num % 10
#         if digit > maximum:
#             maximum = digit
#         num //= 10
#     print('Максимальная цифра:', maximum)
#
#
# def min_digit(num):
#     minimum = num % 10
#     while num > 0:
#         digit = num % 10
#         if digit < minimum:
#             minimum = digit
#         num //= 10
#     print('Минимальная цифра:', minimum)
#
#
# while True:
#     number = int(input('Введите число: '))
#     action = int(input('Введите номер действия: 1 - сумма цифр, 2 -максимальная цифра, 3 - минимальная цифра: '))
#     if action == 1:
#         digits_summ(number)
#     elif action == 2:
#         max_digit(number)
#     elif action == 3:
#         min_digit(number)
#     else:
#         print('Ошибка: неверная команда.')
