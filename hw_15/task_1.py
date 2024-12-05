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
