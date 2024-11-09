import time
from typing import Callable
#  STEP 1.1 Простой декоратор без параметров
# Передача функции в качестве аргумента
#
#
# def main(func: Callable):
#     def wrapper(*args, **kwargs):
#         print(f'Запуск функции {func.__name__} в {time.time()}')
#         result = func(*args, **kwargs)
#         print(f'Результат функции {func.__name__}: {result}')
#         print(f'Завершение функции {func.__name__} в {time.time()}')
#         return result
#     return wrapper
#
#
# def factorial(n: int) -> int:
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f
#
#
# print(f'{factorial(1000)=}')
# control = main(factorial)
# print(f'{control.__name__=}')
# print(f'{control(1000)=}')


# STEP 1.2 Синтаксический сахар Python, @
# В языке Python есть более элегантная возможность создания декораторов —
# синтаксический сахар. Для этого используется символ “@” слитно с именем
# декоратора. Строка кода пишется непосредственно над определением функции или метода.
# Добавили декоратор @main к функции factorial. Необходимость в присваивании
# значения новой переменной отпала. Несколько нижних строк кода из старого
# примера удалили за ненадобностью. Кроме того мы сохранили старое имя функции.
# 🔥 Важно! Функция декоратор должна быть определена в коде раньше, чем
# использована. В противном случае получим ошибку NameError
# def main(func: Callable):
#     def wrapper(*args, **kwargs):
#         print(f'Запуск функции {func.__name__} в {time.time()}')
#         result = func(*args, **kwargs)
#         print(f'Результат функции {func.__name__}: {result}')
#         print(f'Завершение функции {func.__name__} в {time.time()}')
#         return result
#     return wrapper
#
#
# @main
# def factorial(n: int) -> int:
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f
#
#
# print(f'{factorial(1000)=}')


# STEP 1.3 Множественное декорирование.
# Python позволяет использовать несколько декораторов на одной функции.
# Обратите внимание на порядок декораторов у функции main. Ближайший к функции
# декоратор A. Декоратор С находится первым в списке, т.е. он максимально удалён от основной функции.
# При запуске кода процесс декорирования начинает снизу вверх, с A, далее B и лишь потом C.
# Прежде чем выполнить код основной функции запускается код верхнего
# декоратора С, далее B, в конце нижний A и только потом код функции main. После
# того как декорированная функция завершила работу и вернула результат
# декораторы завершают работу в обратном старту порядке, снизу вверх. В
# зависимости от решаемых задач порядок декорирования может привести к разным результатам
# def deco_a(func: Callable):
#     def wrapper_a(*args, **kwargs):
#         print('Старт декоратора A')
#         print(f'Запускаю {func.__name__}')
#         res = func(*args, **kwargs)
#         print(f'Завершение декоратора A')
#         return res
#
#     print('Возвращаем декоратор A')
#     return wrapper_a
#
#
# def deco_b(func: Callable):
#     def wrapper_b(*args, **kwargs):
#         print('Старт декоратора B')
#         print(f'Запускаю {func.__name__}')
#         res = func(*args, **kwargs)
#         print(f'Завершение декоратора B')
#         return res
#
#     print('Возвращаем декоратор B')
#     return wrapper_b
#
#
# def deco_c(func: Callable):
#     def wrapper_c(*args, **kwargs):
#         print('Старт декоратора C')
#         print(f'Запускаю {func.__name__}')
#         res = func(*args, **kwargs)
#         print(f'Завершение декоратора C')
#         return res
#
#     print('Возвращаем декоратор C')
#     return wrapper_c
#
#
# @deco_c
# @deco_b
# @deco_a
# def main():
#     print('Старт основной функции')
#
#
# main()


# STEP 1.4 Дополнительные переменные в декораторе
# Внутри декоратора cache создали пустой словарь _cache_dict. При каждом вызове
# функции factorial внутри обёртки wrapper происходит проверка. Если переданное
# для нахождения факториала число не является ключём словаря, создаём
# соответствующий ключ и в качестве значения присваиваем ему результат
# вычисления факториала. Когда в словаре есть ключ, декорируемая функция не
# вызывается, а ответ сразу возвращается из словаря.
# 🔥 Важно! Мы специально исключили параметр **kwargs из функции
# wrapper, т.к. это словарь ключевых аргументов. Попытка использования в
# качестве ключа словаря _cache_dict другого словаря kwargs приведёт к ошибке.
# Ключом может выступать только неизменяемые объекты
# def cache(func: Callable):
#     _cache_dict = {}
#
#     def wrapper(*args):
#         if args not in _cache_dict:
#             _cache_dict[args] = func(*args)
#         return _cache_dict[args]
#     return wrapper
#
#
# @cache
# def factorial(n: int) -> int:
#     print(f'Вычисляю факториал для числа {n}')
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f
#
#
# print(f'{factorial(10)=}')
# print(f'{factorial(15)=}')
# print(f'{factorial(10)=}')
# print(f'{factorial(20)=}')
# print(f'{factorial(10)=}')
# print(f'{factorial(20)=}')


# STEP 2.1 Декоратор с параметрами
# До этого мы вкладывали одну функцию в другую для создания замыкания. Если мы
# хотим передавать в декоратор дополнительные параметры, понадобится третий уровень вложенности
# Декоратор с параметром может принимать любые значения в зависимости от предназначения
# 🔥 Важно! Последняя строка дублируется не случайно. Каждый из двух
# запусков делает по 10 замеров. Если бы список time_for_count был создан на
# уровень выше, в функции deco, произошло бы его замыкание. В результате
# каждый новый вызов функции factorial дополнял бы уже существующий список,
# а не создавал бы новые 10 значений.
# 🔥 Важно! Для оценки быстродействия кода рекомендуется использовать
# модуль timeit из “батареек Python”, а не созданный выше декоратор.
def count(num: int = 1):
    def deco(func: Callable):
        def wrapper(*args, **kwargs):
            time_for_count = []
            result = None
            for _ in range(num):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                stop = time.perf_counter()
                time_for_count.append(stop - start)

            print(f'Результаты замеров {time_for_count}')
            return result
        return wrapper
    return deco


@count(10)
def factorial(n: int) -> int:
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(1000)=}')
print(f'{factorial(1000)=}')




