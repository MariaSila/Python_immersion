# Задание 1. Карма
# Один буддист-программист решил создать свой симулятор жизни, в котором
# нужно набрать 500 очков кармы (это константа), чтобы достичь просветления.
# Каждый день вызывается специальная функция one_day(), которая возвращает
# количество кармы от 1 до 7 и может с вероятностью 1 к 10 выкинуть одно из
# исключений:
#       ● KillError,
#       ● DrunkError,
#       ● CarCrashError,
#       ● GluttonyError,
#       ● DepressionError.
# (Исключения нужно создать самостоятельно, при помощи наследования от Exception.)
# Напишите такую программу. Функцию оберните в бесконечный цикл, выход из
# которого возможен только при накоплении кармы до уровня константы.
# Исключения обработайте и запишите в отдельный лог karma.log.
# По итогу у вас может быть примерно такая структура программы:
#   открываем файл
#   цикл по набору кармы
#   try
#       карма += one_day()
#   except(ы) с указанием классов исключений, которые нужно поймать
#       добавляем запись в файл
#   закрываем файл
# Подсказка № 1
#   Создайте пользовательские исключения с помощью наследования от Exception.
#   Создайте классы для каждого типа исключения, унаследовав их от базового класса
#   Exception, и определите их сообщения в конструкторе.
# Подсказка № 2
#   Используйте модуль random для генерации случайных чисел. Модуль random поможет
#   вам как для генерации случайных чисел для кармы, так и для случайного выбора исключений.
# Подсказка № 3
#   Обработайте исключения внутри блока try-except и запишите их в файл. Используйте
#   конструкцию try-except для перехвата исключений и записи их сообщений в файл karma.log.
# Подсказка № 4
#   Откройте файл в режиме записи с помощью with для автоматического управления
#   ресурсами. Использование конструкции with open(...) обеспечит автоматическое
#   закрытие файла после завершения работы с ним.

import logging
from random import randint, choice


class LifeException(Exception):
    pass


class KillError(LifeException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Убийство. Уровень кармы {self.value}'


class DrunkError(LifeException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Пьянство. Уровень кармы {self.value}'


class CarCrashError(LifeException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Автомобильная авария. Уровень кармы {self.value}'


class GluttonyError(LifeException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Обжорство. Уровень кармы {self.value}'


class DepressionError(LifeException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Депрессия. Уровень кармы {self.value}'


MIN_VALUE = 1
MAX_VALUE = 7
KARMA_MAX = 500
gen = [i for i in range(1, 11)]


def one_day():
    lst_err = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]
    num = choice(gen)
    match num:
        case 1:
            e = choice(lst_err)
            raise e(karma)
        case _:
            k = randint(MIN_VALUE, MAX_VALUE + 1)
            return k


karma = 0
logging.basicConfig(filename='karma.log', filemode='w', level=logging.INFO, encoding='utf-8')
while True:
    if karma < KARMA_MAX:
        try:
            cnt = one_day()
            karma += cnt
            # logging.info(f'Уровень кармы увеличился на {cnt} и составляет {karma}')
        except KillError:
            logging.error('KillError', exc_info=True)
        except DrunkError:
            logging.error('DrunkError', exc_info=True)
        except CarCrashError:
            logging.error('CarCrashError', exc_info=True)
        except GluttonyError:
            logging.error('GluttonyError', exc_info=True)
        except DepressionError:
            logging.error('DepressionError', exc_info=True)
    else:
        break


# PERFECT SOLUTION
# import random
#
# # Константа для достижения просветления
# NIRVANA_KARMA = 500
#
#
# # Определение пользовательских исключений
# class KillError(Exception):
#     def __init__(self):
#         super().__init__("Убийство. Вы и убили-с!")
#
#
# class DrunkError(Exception):
#     def __init__(self):
#         super().__init__("Пьянство. Пьянству бой!")
#
#
# class CarCrashError(Exception):
#     def __init__(self):
#         super().__init__("Вы попали в аварию. Стоит следить за дорогой.")
#
#
# class GluttonyError(Exception):
#     def __init__(self):
#         super().__init__("Вы обожрались. Следует сократить порции.")
#
#
# class DepressionError(Exception):
#     def __init__(self):
#         super().__init__("На вас напала хандра. Уныние - грех.")
#
#
# # Функция, моделирующая один день жизни
# def one_day():
#     # Случайное количество кармы от 1 до 7
#     day_karma = random.randint(1, 7)
#     # Случайная вероятность выброса исключения
#     if random.randint(1, 10) == 5:
#         # Случайный выбор исключения
#         exception = random.choice([KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()])
#         raise exception
#     return day_karma
#
#
# # Основная функция симулятора
# def main():
#     karma = 0
#
#     # Открываем файл для записи логов
#     with open('karma.log', 'w', encoding='utf-8') as fl_logger:
#         while True:
#             try:
#                 # Прибавляем карму за один день
#                 karma += one_day()
#             except Exception as ex:
#                 # Записываем информацию об исключении в файл
#                 fl_logger.write(f'{ex}\n')
#             # Проверяем, достигнуто ли необходимое количество кармы
#             if karma >= NIRVANA_KARMA:
#                 break
#     # Сообщаем о достижении цели
#     print('Вы достигли Нирваны! ')
#     print('Омм ')
#
#
# # Запуск основной функции
# if __name__ == "__main__":
#     main()
