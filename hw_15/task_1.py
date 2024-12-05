# Задание 1. Логирование с использованием нескольких файлов
# Напишите скрипт, который логирует разные типы сообщений в разные файлы.
# Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня
# WARNING и выше — в warnings_errors.log.
# Подсказка № 1
#   Создайте логгеры с разными уровнями логирования. Используйте
#   logger.setLevel() для установки минимального уровня логирования, который будет
#   обрабатываться логгером.
# Подсказка № 2
#   Используйте logging.FileHandler для записи логов в файлы. Установите FileHandler
#   для записи сообщений в указанные файлы и укажите уровень логирования для
#   каждого обработчика с помощью метода setLevel().
# Подсказка № 3
#   Настройте формат сообщений с помощью logging.Formatter. Создайте объект
#   Formatter для настройки формата сообщений. Примените его к обработчикам с
#   помощью метода setFormatter().
# Подсказка № 4
#   Добавьте обработчики к логгеру с помощью addHandler(). После настройки

import logging

# Создаем регистратор
logger = logging.getLogger('debug_info')
logger_warning = logging.getLogger('warning')

# Устанавливаем минимальный уровень логирования
logger.setLevel('DEBUG')
logger_warning.setLevel('WARNING')

# Настройка обработчика
handler_debug = logging.FileHandler('debug_info.log', mode='w', encoding='utf-8')
handler_warning = logging.FileHandler('warnings_errors.log', mode='w', encoding='utf-8')

# Настройка формата
formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

# Добавление формата к обработчику
handler_debug.setFormatter(formatter)
handler_warning.setFormatter(formatter)

# Добавление обработчика к логгеру
logger.addHandler(handler_debug)
logger_warning.addHandler(handler_warning)


if __name__ == '__main__':
    logger.debug('Очень подробная отладочная информация. Заменяем множество "принтов"')
    logger.info('Немного информации о работе кода')
    logger_warning.warning('Внимание! Надвигается буря!')
    logger_warning.error('Поймали ошибку. Дальше только неизвестность')
    logger_warning.critical('На этом всё')


# PERFECT SOLUTION
# import logging
#
# # Настройка логирования
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
#
# # Форматтер для сообщений
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#
# # Обработчик для сообщений уровня DEBUG и INFO
# debug_info_handler = logging.FileHandler('debug_info.log')
# debug_info_handler.setLevel(logging.DEBUG)
# debug_info_handler.setFormatter(formatter)
# logger.addHandler(debug_info_handler)
#
# # Обработчик для сообщений уровня WARNING и выше
# warnings_errors_handler = logging.FileHandler('warnings_errors.log')
# warnings_errors_handler.setLevel(logging.WARNING)
# warnings_errors_handler.setFormatter(formatter)
# logger.addHandler(warnings_errors_handler)
#
# # Логирование сообщений различных уровней
# logger.debug('Это сообщение уровня DEBUG.')
# logger.info('Это сообщение уровня INFO.')
# logger.warning('Это сообщение уровня WARNING.')
# logger.error('Это сообщение уровня ERROR.')
# logger.critical('Это сообщение уровня CRITICAL.')


