# Строка документации, Хранение документации в __doc__


# -------------------------------------------------------------------------------------
# STEP 1. Как и при создании функции, при создании классов принято оставлять
# документацию к нему. Для этого достаточно использовать многострочный
# комментарий сразу после определения класса — строки class ClassName
# После заголовка класса оставили пару строк описания. Также добавлена строка
# документации для метода __init__. Далее вызываем справку для класс User и для
# его экземпляра. С первого взгляда они похожи и выводят куда больше информации.
# Помимо оставленной документации help собирает информацию о методах класса.
# Выводит первую строку метода и строку документации метода, если она задана
# многострочным комментарием.
# Отличие справки для класса и экземпляра лишь в первой строке. Сравните:
# Help on class User in module __main__:
# 10
# Help on User in module __main__ object:

# class User:
#     """A User training class for demonstrating class
#     documentation.
#     Shows the operation of the help(cls) and the dander method
#     __doc__"""
#     def __init__(self, name: str):
#         """Added the name parameter."""
#         self.name = name
#
#     def simple_method(self):
#         """Example of a simple method."""
#         self.name.capitalize()
#
#
# u_1 = User('Спенглер')
# print('Справка класса User ниже', '*' * 50)
# help(User)
# print('Справка экземпляра u_1 ниже', '*' * 50)
# help(u_1)


#  => Справка класса User ниже **************************************************
# Help on class User in module __main__:
#
# class User(builtins.object)
#  |  User(name: str)
#  |
#  |  A User training class for demonstrating class
#  |  documentation.
#  |  Shows the operation of the help(cls) and the dander method
#  |  __doc__
#  |
#  |  Methods defined here:
#  |
#  |  __init__(self, name: str)
#  |      Added the name parameter.
#  |
#  |  simple_method(self)
#  |      Example of a simple method.
#  |
#  |  --------------------------------
#  |  Data descriptors defined here:
#  |
#  |  __dict__
#  |      dictionary for instance variables
#  |
#  |  __weakref__
#  |      list of weak references to the object
#
#  => Справка экземпляра u_1 ниже **************************************************
# Help on User in module __main__ object:
#
# class User(builtins.object)
#  |  User(name: str)
#  |
#  |  A User training class for demonstrating class
#  |  documentation.
#  |  Shows the operation of the help(cls) and the dander method
#  |  __doc__
#  |
#  |  Methods defined here:
#  |
#  |  __init__(self, name: str)
#  |      Added the name parameter.
#  |
#  |  simple_method(self)
#  |      Example of a simple method.
#  |
#  |  ------------------------------
#  |  Data descriptors defined here:
#  |
#  |  __dict__
#  |      dictionary for instance variables
#  |
#  |  __weakref__
#  |      list of weak references to the object


# STEP 2. Хранение документации в __doc__
# Любая многострочная строка после заголовка класса и метода автоматичские
# сохраняется в дандер переменную __doc__. Помимо вызова справки через
# функцию help можно прочитать отдельный мнострочник напрямую обратившись к переменной.
# Как и в случае с help обращение через класс или через экземпляр не даёт разницы.

# class User:
#     """A User training class for demonstrating class
#     documentation.
#     Shows the operation of the help(cls) and the dander method
#     __doc__"""
#     def __init__(self, name: str):
#         """Added the name parameter."""
#         self.name = name
#         print(f'Создал {self.name = }')
#
#     def simple_method(self):
#         """Example of a simple method."""
#         self.name.capitalize()
#
#
# u_1 = User('Спенглер')
# print(f'Документация класса: {User.__doc__=}')
# print(f'Документация экземпляра: {u_1.__doc__=}')
# print(f'Документация метода: {u_1.simple_method.__doc__}')


# => Создал self.name = 'Спенглер'
# => Документация класса: User.__doc__='A User training class for demonstrating class\n
#       documentation.\n    Shows the operation of the help(cls) and the dander method\n    __doc__'
# => Документация экземпляра: u_1.__doc__='A User training class for demonstrating class\n
#       documentation.\n    Shows the operation of the help(cls) and the dander method\n    __doc__'
# => Документация метода: Example of a simple method.


# ---------------------------------------------------------------------------------------------
# class MyClass:
#     A = 42
#
#     """About class"""
#     def __init__(self, a, b):
#         """self.__doc__ = None"""
#         self.a = a
#         self.b = b
#
#     def method(self):
#         """Documentation"""
#         self.__doc__ = None
#
#
# help(MyClass)