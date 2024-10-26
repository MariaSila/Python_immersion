# Задача 3. Генератор последовательности чисел Фибоначчи
# Напишите генераторную функцию fibonacci(n), которая принимает на вход
# одно целое число n и возвращает последовательность первых n чисел
# Фибоначчи. Числа Фибоначчи — это последовательность, в которой каждое
# число является суммой двух предыдущих, начиная с 0 и 1.
# Подсказка № 1
# В последовательности Фибоначчи каждое число является суммой двух предыдущих,
# начиная с 0 и 1. Начальные числа задаются как 0 и 1.
# Подсказка № 2
# Генераторная функция использует ключевое слово yield для возврата значения и
# сохранения состояния функции. Это позволяет приостановить выполнение функции и
# продолжить его с того места, где оно было приостановлено, при следующем вызове.
# Подсказка № 3
# Начните с двух переменных, a и b, равных 0 и 1 соответственно. Эти значения
# соответствуют первым двум числам Фибоначчи. В цикле обновляйте значения a и b
# следующим образом: a принимает значение b, а b — сумму предыдущих a и b. Это
# позволяет получать следующее число в последовательности.


def fibonacci(n):
    f1 = 0
    yield f1
    f2 = 1
    yield f2
    n -= 2
    while n:
        res = f1 + f2
        yield res
        f1 = f2
        f2 = res
        n -= 1


for i in fibonacci(7):
    print(i, end=', ')


# # perfect solution
# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
#
#
# for number in fibonacci(10):
#     print(number)
