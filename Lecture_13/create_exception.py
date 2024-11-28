# Создание собственных исключений

# ----------------------------------------------------------------------------
# В финале пару примеров создания собственных исключений. Попробуем для класса
# User из прошлого примера создать свои исключения.
# Писать код исключений будем в отдельном файле error.py Начнём с того, что
# создадим своё собственное базовое исключение. От него будут наследоваться
# остальные наши исключения. Родительское исключение займёт пару строк кода

# # А теперь добавим исключения для ошибок имени и возраста пользователя. Пока это
# # будут исключения на минималках

# Теперь внесём правки в код инициализации пользователя. Заодно избавимся от
# магических чисел для минимальной и максимальной длины имени.
# Подобный код отлично справляется с поставленной задачей. Но стал менее
# информативен в случае возникновения ошибок.

# from error import UserNameError, UserAgeError
#
#
# class User:
#     MIN_LEN = 6
#     MAX_LEN = 30
#
#     def __init__(self, name, age):
#         if self.MIN_LEN < len(name) < self.MAX_LEN:
#             self.name = name
#         else:
#             raise UserNameError
#         if not isinstance(age, (int, float)) or age < 0:
#             raise UserAgeError
#         else:
#             self.age = age
#
#
# user = User('Яков', '-12')


# -----------------------------------------------------------------------
# Понятно, что ошибка в имени. Но не очень информативно. Исправим ситуацию.
# Методы __init__ и __str__ в классах своих исключений
# Чтобы исключение давало подробную информацию об ошибке, будем передавать
# ему проблемную переменную. Класс User доработаем в строках подъёма ошибок.
# Уже лучше. Но без пары дандер методов в классах ошибок пока не идеально.
# Дорабатываем код в файле error2.

# from error import UserNameError, UserAgeError
#
#
# class User:
#     def __init__(self, name, age):
#         if 6 < len(name) < 30:
#             self.name = name
#         else:
#             raise UserNameError(name)
#         if not isinstance(age, (int, float)) or age < 0:
#             raise UserAgeError(age)
#         else:
#             self.age = age
#
#
# user = User('Яков', '-12')


# ----------------------------------------------------------------------------
# from error2 import UserNameError, UserAgeError
#
#
# class User:
#     MIN_LEN = 6
#     MAX_LEN = 30
#
#     def __init__(self, name, age):
#         if self.MIN_LEN < len(name) < self.MAX_LEN:
#             self.name = name
#         else:
#             raise UserNameError(name, self.MIN_LEN, self.MAX_LEN)
#         if not isinstance(age, (int, float)) or age < 0:
#             raise UserAgeError(age)
#         else:
#             self.age = age
#
#
# user = User('Яков', '12')