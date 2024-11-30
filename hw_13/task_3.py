# Задача 3. Счастливое число
# Напишите программу, которая запрашивает у пользователя число до тех пор, пока
# сумма этих чисел не станет больше либо равна 777. Каждое введенное число при этом
# дозаписывается в файл. Сделайте так, чтобы перед дозаписью программа с
# вероятностью 1 к 13 выбрасывала пользователю случайное исключение и
# завершалась.
#       Пример 1:
#           Введите число: 10
#           Введите число: 500
#           Введите число: 200
#           Введите число: 67
#           Вы успешно выполнили условие для выхода из порочного цикла!
#       Содержимое файла out_file.txt:
#           10
#           500
#           200
#           67
#       Пример 2:
#           Введите число: 10
#           Введите число: 500
#           Вас постигла неудача!
#       Содержимое файла out_file.txt:
#           10
# Подсказка № 1
#   Используйте методы класса для обработки файлов. В классе создайте методы для
#   работы с файлами, такие как удаление файла и запись данных. Это улучшит
#   организацию кода и сделает его более читаемым.
# Подсказка № 2
#   Обрабатывайте исключения для ввода данных. Используйте конструкцию try-except
#   для обработки исключений, возникающих при вводе данных пользователем. Это
#   гарантирует, что программа корректно реагирует на неправильный ввод и продолжает работу.
# Подсказка № 3
#   Реализуйте метод, который случайным образом выбрасывает исключения с
#   определенной вероятностью. Это можно сделать, используя функцию
#   random.randint() для генерации случайных чисел.
# Подсказка № 4
#   Удаляйте файл перед началом записи, чтобы начать запись в новый файл, сначала
#   удалите существующий файл, если он есть. Это можно сделать с помощью метода
#   os.remove(). Убедитесь, что вы обрабатываете возможные ошибки при удалении файла.

from os import remove
from pathlib import Path
from random import randint


class LuckyNumber:
    FILE_NAME = 'out_file.txt'
    RANDOM_MIN = 1
    RANDOM_MAX = 13
    MAX_NUMBER = 777

    def __init__(self):
        self.path_file = Path(self.FILE_NAME)
        if Path(self.FILE_NAME).is_file():
            self.remove()

    @staticmethod
    def get_number():
        try:
            num = int(input('Введите число: '))
        except ValueError:
            print('Введено не число')
        else:
            return num

    def remove(self):
        try:
            remove(self.FILE_NAME)
        except OSError:
            print('Ошибка. Файла нет')

    def add(self, number):
        with open(self.path_file, 'a', encoding='utf-8') as f:
            f.write(f'{number}\n')

    def random_except(self):
        return randint(self.RANDOM_MIN, self.RANDOM_MAX) == 7

    def run(self):
        res = 0
        while res < self.MAX_NUMBER:
            num = self.get_number()
            if self.random_except():
                print('Вас постигла неудача!')
                break
            self.add(num)
            res += num
        else:
            print('Вы успешно выполнили условие для выхода из порочного цикла!')


if __name__ == '__main__':
    lotto = LuckyNumber()
    lotto.run()


# PERFECT SOLUTION
# import os
# import random
#
# MAGIC_NUMBER = 777
#
#
# class MagicFileProcessor:
#     def __init__(self, filename):
#         """Инициализация с именем файла и определение пути к
#         файлу."""
#         self.filename = filename
#         self.file_path = self.get_file_path()
#         self.magic_sum = 0
#
#     def get_file_path(self):
#         """Возвращает полный путь к файлу."""
#         return os.path.join(os.path.abspath('.'), self.filename)
#
#     def is_exception_raise(self):
#         """Возвращает True с вероятностью 1 из 13, чтобы имитировать
#         ошибку."""
#         return random.randint(1, 13) == 7
#
#     def pre_init(self):
#         """Удаляет файл, если он существует."""
#         try:
#             os.remove(self.file_path)
#         except OSError as ex:
#             print(ex)
#             print('Данный файл не может быть удален')
#
#     def process_input(self):
#         """Обрабатывает ввод пользователя и записывает его в файл."""
#         try:
#             input_number = int(input('Введите число: '))
#             self.magic_sum += input_number
#             if self.is_exception_raise():
#                 raise Exception('Вас постигла неудача!')
#             with open(self.file_path, 'a') as out_fd:
#                 out_fd.write(str(input_number) + '\n')
#
#         except (ValueError, KeyboardInterrupt) as ex:
#             print(ex)
#             print('Возникли проблемы при вводе.')
#             print('Попробуйте еще раз')
#
#     def run(self):
#         """Основной метод для запуска процесса обработки ввода."""
#         self.pre_init()  # Удаляет старый файл, если он существует
#         while self.magic_sum < MAGIC_NUMBER:
#             self.process_input()
#         print('Вы успешно выполнили условие для выхода из порочного цикла!')
#
#
# # Запуск программы
# if __name__ == "__main__":
#     processor = MagicFileProcessor('out_file.txt')
#     processor.run()




