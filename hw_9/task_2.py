# Задача 2. Замедление кода
# В программировании иногда возникает ситуация, когда работу функции нужно
# замедлить. Типичный пример — функция, которая постоянно проверяет,
# изменились ли данные на веб-странице или её код.
# Реализуйте декоратор, который перед выполнением декорируемой функции
# ждёт несколько секунд.
# Подсказка № 1
# Используйте функцию sleep из модуля time для задержки выполнения. Функция sleep
# позволяет приостановить выполнение текущего потока на указанное количество
# секунд.
# Подсказка № 2
# Убедитесь, что в функции sleep передается число секунд. Время ожидания должно
# быть указано в секундах. Если необходимо, преобразуйте время в секунды (например,
# 2000 миллисекунд = 2 секунды).

from time import sleep, time, localtime, strftime
from typing import Callable, Any
from functools import wraps


def slowdown(func: Callable):
    SECOND = 2

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Запуск замедления в {strftime('%H:%M:%S', localtime(time()))} на {SECOND}сек')
        sleep(SECOND)
        print(f'Запуск функции {func.__name__} в {strftime('%H:%M:%S', localtime(time()))}')
        result = func(*args, **kwargs)
        return result
    return wrapper


@slowdown
def test():
    """Homework 9 task_2 Проверка декоратора замедление"""
    print('<Тут что-то происходит...>')


if __name__ == '__main__':
    print(f'{test.__name__=} ')
    print(help(test))
    test()


# perfect solution
# def slowdown_2s(func: Callable[..., Any]) -> Callable[..., Any]:
#     """
#     Декоратор для замедления работы функции на 2 секунды.
#     :param func: Декорируемая функция
#     :return: Функция-обертка
#     """
#     @wraps(func)
#     def wrapper(*args: Any, **kwargs: Any) -> Any:
#         """
#         Функция-обертка, которая приостанавливает выполнение на 2
#         секунды.
#         :param args: Позиционные аргументы
#         :param kwargs: Именованные аргументы
#         :return: Результат выполнения декорируемой функции
#         """
#         sleep(2)  # Приостановка выполнения на 2 секунды
#         result = func(*args, **kwargs)  # Вызов оригинальной функции
#         return result
#     return wrapper
#
#
# @slowdown_2s
# def test() -> None:
#     """
#     Проверка декоратора и вывод простого сообщения.
#     :return: None
#     """
#     print('<Тут что-то происходит...>')
#
#
# @slowdown_2s
# def another_function() -> None:
#     """
#     Еще один пример функции для проверки декоратора.
#     :return: None
#     """
#     print('Еще один тестовый вывод.')
#
#
# if __name__ == "__main__":
#     print(f'{test.__name__= } ')
#     print(help(test))
#     test()
#     another_function()




