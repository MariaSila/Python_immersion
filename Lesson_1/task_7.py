# Задание №7
# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

LOW_LIMIT = 0
UP_LIMIT = 1000
ONE = 1
TEN = 10
HUNDRED = 100
SQUARE = 2

num = LOW_LIMIT

while num <= LOW_LIMIT or num >= UP_LIMIT:
    num = int(input(f'Введите чило от {LOW_LIMIT + ONE} до {UP_LIMIT - ONE}: '))

if num < TEN:
    result = f'Число {num} - цифра. Ее квадрат равен {num ** SQUARE}'
elif num < HUNDRED:
    prod = (num // TEN) * (num % TEN)
    result = f'Число {num} - двухзначное. Произведение цифр равно {prod}'
else:
    mirror = (num % TEN * HUNDRED) + (num // TEN % TEN * TEN) + (num // HUNDRED)
    result = f'Число {num} - трехзначное. Его зеркальное отображение {mirror}'

print(result)