import time
from typing import Callable
from functools import wraps, cache

# Дополнительные возможности декорирования предоставляет модуль functools декоратор.

# STEP 1 Декоратор wraps
# добавим строку документации в функцию factorial.
# Декоратор wraps добавляется к функции wrapper, т.е. к самой глубоко вложенной
# функции. В качестве аргумента wraps должен получить параметр декларируемой
# функции. Теперь factorial возвращает свои название и строку документации.
#
#
# def count(num: int = 1):
#     def deco(func: Callable):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             time_for_count = []
#             result = None
#             for _ in range(num):
#                 start = time.perf_counter()
#                 result = func(*args, **kwargs)
#                 stop = time.perf_counter()
#                 time_for_count.append(stop - start)
#
#             print(f'Результаты замеров {time_for_count}')
#             return result
#         return wrapper
#     return deco
#
#
# @count(10)
# def factorial(n: int) -> int:
#     """Returns the factorial of the number n."""
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f
#
#
# print(f'{factorial(1000)=}')
# print(f'{factorial.__name__=}')
# help(factorial)


# STEP 2 Декоратор cache
# Рассматривая возможности по замыканию переменных мы создали кэширующий
# декоратор. В модуле functools есть декоратор cache с подобным функционалом. При
# необходимости кэширования данных рекомендуется использовать именно его, как
# более оптимальное решение из коробки.
@cache
def factorial(n: int) -> int:
    print(f'Вычисляю факториал для числа {n}')
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(10)=}')
print(f'{factorial(15)=}')
print(f'{factorial(10)=}')
print(f'{factorial(20)=}')
print(f'{factorial(10)=}')
print(f'{factorial(20)=}')
