# Задача 3. Счётчик
# Реализуйте декоратор counter, считающий и выводящий количество вызовов
# декорируемой функции.
# Для решения задачи нельзя использовать операторы global и nonlocal.
# Пример: Из файла products.json нужно создать products.csv.
# Подсказка № 1
# Создайте атрибут обертки для хранения счетчика. Добавьте переменную `count`
# непосредственно в функцию-обертку, чтобы она могла отслеживать количество
# вызовов без использования глобальных переменных.
# Подсказка № 2
# Инициализируйте счетчик по умолчанию. Перед возвратом обертки, установите
# `wrapper.count = 0`, чтобы счетчик начинал отсчет с нуля при каждом новом
# декорировании функции.
# Подсказка № 3
# Увеличивайте счетчик при каждом вызове обертки. Внутри функции-обертки
# увеличивайте значение атрибута `wrapper.count` на единицу каждый раз, когда
# вызывается декорируемая функция.
# Подсказка № 4
# Используйте `functools.wraps` для сохранения метаданных функции. К применению
# декоратора добавьте `@wraps(func)` к функции-обертке, чтобы сохранить
# оригинальные имя и документацию декорируемой функции.
# Подсказка № 5
# Выводите количество вызовов функции после ее выполнения. После вызова
# декорируемой функции в обертке добавьте вывод, который покажет, сколько раз
# функция была вызвана до текущего момента.
import json
import csv
from typing import Callable, Any, Optional
from functools import wraps


def counter(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        wrapper.count += 1
        print(f'Количество вызовов функции {func.__name__} = {wrapper.count}')
        return res

    wrapper.count = 0
    return wrapper


@counter
def json_to_csv(input_file: str, output_file: str) -> None:
    """Конвертация файла .json в .csv"""
    with (
        open(input_file, 'r', encoding='utf-8') as f_read,
        open(output_file, 'w', newline='', encoding='utf-8') as f_write
    ):
        json_file = json.load(f_read)

        keys = json_file[0].keys()
        csv_file = csv.DictWriter(f_write, fieldnames=keys, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
        csv_file.writeheader()
        csv_file.writerows(json_file)


if __name__ == '__main__':
    print(f'{json_to_csv.__name__=} ')
    print(help(json_to_csv))
    json_to_csv('products.json', 'products.csv')
    json_to_csv('products.json', 'products.csv')
    json_to_csv('products.json', 'products.csv')


# # perfect solution
# def counter(func: Callable) -> Callable:
#     """
#     Декоратор для подсчета количества вызовов функции.
#     :param func: Декорируемая функция.
#     :return: Обертка функции с подсчетом вызовов.
#     """
#     @wraps(func)
#     def wrapper(*args, **kwargs) -> Any:
#         """
#         Функция-обертка для увеличения и вывода счётчика вызовов
#         функции.
#         :param args: Позиционные аргументы декорируемой функции.
#         :param kwargs: Именованные аргументы декорируемой функции.
#         :return: Результат вызова декорируемой функции.
#         """
#         wrapper.count += 1
#         result = func(*args, **kwargs)
#         print(f"Функцию '{func.__name__}' вызвали {wrapper.count} раз")
#         return result
#
#     wrapper.count = 0 # Инициализируем счетчик вызовов.
#     return wrapper
#
#
# @counter
# def greeting(name: str, age: Optional[int] = None) -> str:
#     """
#     Приветствие с возрастом и именем.
#     :param name: Имя человека.
#     :param age: Возраст человека (по умолчанию None).
#     :return: Строка с приветствием.
#     """
#     if age:
#         return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
#     else:
#         return "Привет, {name}!".format(name=name)
#
#
# @counter
# def greeting2(name: str) -> None:
#     """
#     Приветствие с именем. Вывод в консоль.
#     :param name: Имя человека.
#     :return: None.
#     """
#     print(f'Привет, {name}!')
#
#
# def main() -> None:
#     """
#     Основная функция для запуска.
#     :return: None.
#     """
#     print(greeting("Том"))  # Вызов функции greeting с одним аргументом.
#     print(greeting("Миша", age=100))  # Вызов функции greeting с двумя аргументами.
#     greeting2("Маша")  # Вызов функции greeting2.
#     print(greeting(name="Катя", age=16))  # Вызов функции greeting с именем и возрастом.
#
#
# main()  # Запуск основной функции.
