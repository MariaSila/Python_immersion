# Задача 3. Число наоборот
# Пользователь вводит два числа: N и K. Напишите программу, которая заменяет
# каждое число на число, которое получается из исходного записью его цифр в
# обратном порядке, затем складывает их, снова переворачивает и выводит
# ответ на экран.
# Пример:
# Введите первое число: 102
# Введите второе число: 123
# Первое число наоборот: 201
# Второе число наоборот: 321
# Сумма: 522
# Сумма наоборот: 225
# Подсказка № 1
# Функция reversal(x) должна обрабатывать каждую цифру числа, начиная с
# последней и добавляя её в новое число. Преобразование можно сделать, используя
# остаток от деления и целочисленное деление.
# Подсказка № 2
# В функции reversal(x) переменная count отслеживает количество цифр, а
# revers_x хранит перевёрнутое число. Не забудьте обновлять revers_x на каждой
# итерации.
# Подсказка № 3
# После ввода чисел и их переворачивания с помощью функции reversal, сложите
# перевёрнутые числа. Затем примените reversal к результату суммы, чтобы получить
# окончательный результат.


def reversal(num: str) -> int:
    count = 0
    revers_x = 0
    lst_digits = []
    number = int(num)
    while number:
        lst_digits.append(number % 10)
        count += 1
        number //= 10
    for i in range(len(lst_digits)):
        count -= 1
        revers_x += 10 ** count * lst_digits[i]
    return revers_x


number_1 = input('Enter first number: ')
number_2 = input('Enter second number: ')
print(f'Первое число наоборот: {reversal(number_1)}')
print(f'Второе число наоборот: {reversal(number_2)}')
print(f'Сумма: {reversal(number_1) + reversal(number_2)}')
print(f'Сумма наоборот: {int(number_1) + int(number_2)}')


# # perfect solution
# def reversal(x):
#     count = 0
#     revers_x = 0
#     for _ in str(x):
#         count += 1
#     while x > 0:
#         count -= 1
#         revers_x += (x % 10) * (10 ** count)
#         x = x // 10
#     return revers_x
#
#
# num_1 = int(input('Введите первое число: '))
# num_2 = int(input('Введите второе число: '))
#
# revers_num1 = reversal(num_1)
# revers_num2 = reversal(num_2)
#
# print('\nПервое число наоборот:', revers_num1)
# print('Второе число наоборот:', revers_num2)
#
# amount = revers_num1 + revers_num2
# revers_summ = reversal(amount)
#
# print('\nСумма:', amount)
# print('Сумма наоборот:', revers_summ)

