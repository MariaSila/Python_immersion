# 5. Модуль argparse

# ------------------------------------------------------------------------------------
# В финале поговорим о модуле argparse. Мы упоминали его, когда речь шла о запуске
# скриптов с параметром через sys.argv. Поговорим о том чем же argparse лучше argv.
# Спойлер — всем. Модуль argparse по сути надстраивается над sys.argv. Он
# генерирует справку, определяет способ анализа аргументов командной строки,
# сообщает об ошибках и даёт подсказки. Чтобы разобраться во всём перечисленном
# по традиции рассмотрим простой пример.
# 💡 Внимание! Тут и далее до конца главы запускать файл будет из
# терминала ОС. Примерно так:
# $ python main.py ...
# 💡 где многоточие - передаваемые скрипту аргументы
# На выходе получаем объект Namespace(numbers=[42.0, 3.14, 73.0]). Как это работает?
#       1. Создаём объект парсер при помощи класса ArgumentParser с
#           первоначальными настройками экземпляра.
#       2. Добавляем в полученный экземпляр аргументы для парсинга через метод
#           add_argument. Количество аргументов может быть любым. И каждый может
#           содержать свои настройки.
#       3. Выгружаем результаты, переданные при запуске скрипта в терминале и
#           обработанные парсером в виде объекта Namespace. Для этого вызываем
#           метод экземпляра parse_args.
# Прежде чем разобрать каждый пунктов подробнее запустим скрипт ещё пару раз: с
# ключом --help и с каким-нибудь текстом.

# import argparse
#
# parser = argparse.ArgumentParser(description='My first argument parser')
# parser.add_argument('numbers', metavar='N', type=float, nargs='*', help='press some numbers')
# args = parser.parse_args()
#
# print(f'В скрипт передано: {args}')

# В терминала ОС:
# (venv) PS C:\Users\user\Python_immersion\Lecture_15> python .\module_argparse.py 42 3.14 73
# В скрипт передано: Namespace(numbers=[42.0, 3.14, 73.0])


# ------------------------------------------------------------------------------------------------
# Ключ --help или -h
# После создания экземпляра парсера и задания ему аргументов формируется
# справочный текст. argparse добавляет ключи --help (длинная версия) и -h (короткая
# версия) автоматически. Другие ключевые параметры мы можем создать сами, но о
# них чуть позже.

# В терминала ОС:
# (venv) PS C:\Users\user\Python_immersion\Lecture_15> python .\module_argparse.py 42 3.14 73 -h
# (venv) PS C:\Users\user\Python_immersion\Lecture_15> python .\module_argparse.py 42 3.14 73 -help


# usage: module_argparse.py [-h] [N ...]
#
# My first argument parser
#
# positional arguments:
#   N           press some numbers
#
# options:
#   -h, --help  show this help message and exit


# Первая строка даёт общее представление о строке запуска. Ниже идёт текст,
# который мы указали в по ключу description при создании экземпляра. Далее
# получаем информацию о позиционных аргументах. В нашем случае это аргумент N
# (metavar='N') и подсказки к нему (help='press some numbers'). В конце идёт
# необязательные параметры, в нашем случае - автоматически сгенерированный
# вызов помощи.


# ----------------------------------------------------------------------------------
# Запуск с неверными аргументами
# При попытке передать в скрипт Hello world! получим:
# В терминала ОС:
# (venv) PS C:\Users\user\Python_immersion\Lecture_15> python .\module_argparse.py 42 'Hello world'


# usage: module_argparse.py [-h] [N ...]
# module_argparse.py: error: argument N: invalid float value: 'Hello world'

# При создании аргумента мы указали, что хотим получать целые числа (type=float).
# Парсер автоматически создал валидатор и сообщил о несовпадении типов.
# Заметьте, что при передаче целых чисел ошибок не было, но они были
# преобразованы к вещественному типу


# -------------------------------------------------------------------------------
# Создаём парсер, ArgumentParser
# При создании экземпляра из класса ArgumentParser можно 13 различных
# аргументов. Но большинство из них имеют оптимальные настройки по умолчанию.
# Если что-то и стоит добавить, то дополнительное описание, которое выводится при
# вызове справки.
#       ● prog — заменяет название файла в первой строке справки на переданное имя,
#       ● description — описание в начале справки
#       ● epilog — описание в конце справки

# import argparse
# parser = argparse.ArgumentParser(prog='average',
#                                  description='My first argument parser',
#                                  epilog='Returns the arithmetic mean')
# ...


# ---------------------------------------------------------------------------
# Выгружаем результаты, parse_args
# Метод parse_args может принимать на вход два аргумента:
#       ● строку для анализа. По умолчанию это sys.argv
#       ● объект для сохранения результатов. По умолчанию это класс Namespace.
# Класс наследуется от object, не имеет ничего лишнего, но добавляет удобный
# вывод ключей и значений, помещённых в него.
# Изменять значения по умолчанию приходится крайне редко, почти никогда.
# В этом случае код говорит сам за себя. Прочитайте три нижние строки. Уверен, что
# вопрос не должно остаться.

# import argparse
# parser = argparse.ArgumentParser(description='My first argument parser')
# parser.add_argument('numbers', metavar='N', type=float, nargs='*', help='press some numbers')
# args = parser.parse_args()
# print(f'Получили экземпляр Namespace: {args = }')
# print(f'У Namespace работает точечная нотация: {args.numbers = }')
# print(f'Объекты внутри могут быть любыми: {args.numbers[1] = }')


# --------------------------------------------------------------------------------------------
# Добавляем аргументы, add_argument
# А теперь самое интересное. Между созданием парсера и чтением результатов надо
# добавить желаемые аргументы.
# Перед нами пример функции для решения квадратных уравнений. Параметры a, b, с
# собираем в терминале.
# Первая строка превращается в имя свойства. Если она начинается с одиночного или
# двойного дефиса, параметр считается необязательным. Далее:
#       ● metavar — имя, которое выводится с справке
#       ● type — тип, для преобразования аргумента. Тип помогает контролировать
#               передачу нужных значений.
#       ● nargs — указывает на количество значений, которые надо собрать из
#               командной строки и собрать результат в список list. Целое число указывает
#               количество. Кроме этого можно передать символ
#                       “?” — один аргумент,
#                       “*” — все имеющиеся аргументы,
#                       “+” — все имеющиеся аргументы, но не пустое значение.
#       ● help - вывод подсказки об аргументе.
# Если вызвать справку для нашего кода, увидим дублирование в первой строке
# usage: main.py [-h] a b c a b c a b c

# Вызов:
# (venv) PS C:\Users\user\Python_immersion\Lecture_15> python .\module_argparse.py 2 -12 10
# Вывод:
# (5.0, 1.0)

# Вызов:
# (venv) PS C:\Users\user\Python_immersion\Lecture_15> python .\module_argparse.py 2 -12 10 -h
# Вывод:
# usage: module_argparse.py [-h] a b c a b c a b c
#
# Solving quadratic equations
#
# positional arguments:
#   a b c       enter a b c separated by a space
#
# options:
#   -h, --help  show this help message and exit
# import argparse
#
#
# def quadratic_equations(a, b, c):
#     d = b ** 2 - 4 * a * c
#     if d > 0:
#         return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
#     if d == 0:
#         return -b / (2 * a)
#     return None
#
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='Solving quadratic equations')
#     parser.add_argument('param', metavar='a b c', type=float, nargs=3, help='enter a b c separated by a space')
#     args = parser.parse_args()
#     print(quadratic_equations(*args.param))


# -------------------------------------------------------------------------------------
# Необязательные аргументы и значения по умолчанию
# Изменим наш парсер и добавим ещё несколько параметров к аргументам.
# Теперь необходимо указывать ключи а, б и с при передаче значений. Но
# дополнительный параметр default позволяет отказаться от передачи. В этом случае
# значения будут взяты из параметра по умолчанию.

# Вызов:
# (venv) PS C:\Users\user\Python_immersion\Lecture_15> python .\module_argparse.py -a 2 -b -12
# Вывод:
# (6.0, 0.0)

# Вызов:
# (venv) PS C:\Users\user\Python_immersion\Lecture_15> python .\module_argparse.py 2 -12 10 -h
# Вывод:
# usage: module_argparse.py [-h] [-a a] [-b b] [-c c]
#
# Solving quadratic equations
#
# options:
#   -h, --help  show this help message and exit
#   -a a        enter a for ax^2+bx+c=0
#   -b b        enter b for ax^2+bx+c=0
#   -c c        enter c for ax^2+bx+c=0
#
# import argparse
#
#
# def quadratic_equations(a, b, c):
#     d = b ** 2 - 4 * a * c
#     if d > 0:
#         return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
#     if d == 0:
#         return -b / (2 * a)
#     return None
#
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='Solving quadratic equations')
#     parser.add_argument('-a', metavar='a', type=float,
#                         help='enter a for ax^2+bx+c=0', default=1)
#     parser.add_argument('-b', metavar='b', type=float,
#                         help='enter b for ax^2+bx+c=0', default=0)
#     parser.add_argument('-c', metavar='c', type=float,
#                         help='enter c for ax^2+bx+c=0', default=0)
#     args = parser.parse_args()
#     print(quadratic_equations(args.a, args.b, args.c))


# ----------------------------------------------------------------------------------
# Параметр action для аргумента
# И напоследок ещё один интересный параметр уже без квадратных уравнений. Речь
# пойдёт о параметре action.
# Параметр action принимает одно из определённых строковых значений и
# срабатывает при наличии в строке вызова скрипта соответствующего параметра.
#       ● store_const — передаёт в args ключ со значением из параметра const
#       ● store_true или store_false — сохраняет в ключе истину или ложь
#       ● append — ищет несколько появлений ключа и собирает все значения после
#               него в список
#       ● append_const — добавляет значение из ключа в список, если ключ вызван.
#               ○ параметр dest переопределяет имя ключа в Namespace на своё. В
#                   результате несколько разных ключей при вызове скрипта имеют одно
#                   имя при оценке результата.
# Пожалуй это всё о основных способностях модуля argparse

# Вызов
# (venv) PS C:\Users\user\Python_immersion\Lecture_15> python .\module_argparse.py -x -y -z 42 -z 73 -i -f -s
# Вывод
# Namespace(x=42, y=True, z=['42', '73'], types=[<class 'int'>, <class 'float'>, <class 'str'>])

# import argparse
#
# parser = argparse.ArgumentParser(description='Sample')
# parser.add_argument('-x', action='store_const', const=42)
# parser.add_argument('-y', action='store_true')
# parser.add_argument('-z', action='append')
# parser.add_argument('-i', action='append_const', const=int, dest='types')
# parser.add_argument('-f', action='append_const', const=float, dest='types')
# parser.add_argument('-s', action='append_const', const=str, dest='types')
# args = parser.parse_args()
# print(args)
