__all__ = ['UserException', 'ClassNotFoundError', 'NameNotFoundError', 'NameError', 'DataError', 'InputError']


class UserException(Exception):
    pass


class ClassNotFoundError(UserException):
    def __init__(self, cls_name):
        self.cls_name = cls_name

    def __str__(self):
        return f'Класс {self.cls_name} не найден'


class NameNotFoundError(UserException):
    def __init__(self, cls_name, name):
        self.cls_name = cls_name
        self.name = name

    def __str__(self):
        return f'{self.cls_name} с именем {self.name} не найден'


class NameError(UserException):
    def __str__(self):
        return 'Имя не соответствует формату. Имя должно состоять из букв и начинается с заглавной буквы'


class DataError(UserException):
    def __str__(self):
        return 'Некорректная дата. Проверьте дату и формат гггг-мм-дд'


class InputError(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Неккоретный ввод данных. Ожидается диапазон от 1 до {self.value} включительно'
