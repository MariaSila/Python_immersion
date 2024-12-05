# Задача 4. Опции и флаги
# Напишите скрипт, который принимает два аргумента командной строки: число и
# строку. Добавьте следующие опции:
#       ● --verbose, если этот флаг установлен, скрипт должен выводить
#           дополнительную информацию о процессе.
#       ● --repeat, если этот параметр установлен, он должен указывать,
#           сколько раз повторить строку в выводе.
# Подсказка № 1
#   Используйте import argparse, чтобы работать с аргументами командной строки.
# Подсказка № 2
#   Используйте argparse.ArgumentParser для создания объекта парсера, который
#   будет обрабатывать входные параметры.
# Подсказка № 3
#   Примените метод add_argument для добавления обязательных аргументов number и
#   text. Укажите типы данных и описания.
# Подсказка № 4
#   Добавьте опцию --verbose с action='store_true' для флага, который активирует
#   дополнительный вывод, и --repeat для указания количества повторений строки.

import argparse


parser = argparse.ArgumentParser(description='My first argument parser')
parser.add_argument('-number', type=int, help='Integer number')
parser.add_argument('-text', type=str, help='Any text')
parser.add_argument('-v', '--verbose', action='store_true', help='If used, additional help is displayed')
parser.add_argument('-r', '--repeat', type=int, default=1, help='Specifies how many times to repeat a line in the output')
args = parser.parse_args()
# print(args)


def func(num: int, txt: str):
    return txt * num


if __name__ == '__main__':
    if args.verbose:
        print('Repeating the text the specified number of times')
    elif args.repeat:
        for i in range(args.repeat):
            print(func(args.number, args.text))
    else:
        print(func(args.number, args.text))


# PERFECT SOLUTION
# import argparse
#
#
# def main():
#     # Создание парсера аргументов
#     parser = argparse.ArgumentParser(description='Процессинг числа и строки с дополнительными опциями.')
#
#     # Добавление обязательных аргументов
#     parser.add_argument('number', type=int, help='Число для вывода')
#     parser.add_argument('text', type=str, help='Строка для вывода')
#
#     # Добавление опций
#     parser.add_argument('--verbose', action='store_true', help='Вывод дополнительной информации')
#     parser.add_argument('--repeat', type=int, default=1, help='Количество повторений строки')
#
#     # Парсинг аргументов
#     args = parser.parse_args()
#
#     # Вывод дополнительной информации, если опция verbose установлена
#     if args.verbose:
#         print(f'Полученные аргументы: number={args.number}, text="{args.text}", repeat={args.repeat}')
#
#     # Вывод строки, повторенной указанное количество раз
#     print(f'Число: {args.number}, Строка: {args.text * args.repeat}')
#
#
# if __name__ == '__main__':
#     main()

