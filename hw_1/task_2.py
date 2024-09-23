# Задача 2. Треугольник
# Треугольник существует только тогда, когда сумма любых двух его сторон
# больше третьей. Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если
# хотя бы в одном случае отрезок окажется больше суммы двух других, то
# треугольника с такими сторонами не существует. Отдельно сообщить является
# ли треугольник разносторонним, равнобедренным или равносторонним.
# Подсказка № 1
# Треугольник может существовать только в том случае, если сумма длин любых двух
# его сторон больше длины третьей стороны. Проверьте это условие с помощью
# логического выражения.
# Подсказка № 2
# Внутри блока if, который проверяет существование треугольника, добавьте
# вложенные условные выражения для определения типа треугольника:
# равносторонний, равнобедренный или разносторонний.
# Подсказка № 3
# Если условие существования треугольника не выполняется, выведите сообщение, что
# треугольник с такими сторонами не существует.

a = float(input('Введите длину стороны a: '))
b = float(input('Введите длину стороны b: '))
c = float(input('Введите длину стороны c: '))

if a + b > c and a + c > b and b + c > a:
    print('Треугольник существует')
    if a == b == c:
        print('Треугольник равносторонний')
    elif a == b or a == c or b == c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print(f'Треугольник со сторонами {a}, {b}, {c} не существует')


# #Идеальное решение
# # Запрос у пользователя длин сторон треугольника
# a = float(input("Введите сторону a: "))
# b = float(input("Введите сторону b: "))
# c = float(input("Введите сторону c: "))
#
# # Проверка условия существования треугольника
# if a + b > c and a + c > b and b + c > a:
#     print("Треугольник существует.")
#     # Проверка, является ли треугольник равносторонним
#     if a == b == c:
#         print("Треугольник равносторонний.")
#     # Проверка, является ли треугольник равнобедренным
#     elif a == b or b == c or a == c:
#         print("Треугольник равнобедренный.")
#     # Если треугольник не равносторонний и не равнобедренный, то он разносторонний
#     else:
#         print("Треугольник разносторонний.")
# else:
#     print("Треугольник не существует.")