# Задача 5. Валидатор Пользовательских Данных
# Создайте класс User, который содержит атрибуты name, email, и age.
# Необходимо убедиться, что:
#       ● Имя состоит из хотя бы двух слов, каждое из которых начинается с
#       заглавной буквы.
#       ● Электронная почта содержит символ @ и точку . после @.
#       ● Возраст — это положительное целое число, не меньше 0 и не больше 120.
# Создайте пользовательские исключения для каждой из этих проверок:
#       ● NameError: Если имя не соответствует формату.
#       ● EmailError: Если электронная почта не соответствует формату.
#       ● AgeError: Если возраст вне допустимого диапазона.
# Подсказка № 1
#   Создайте пользовательские исключения. Определите три класса исключений
#   (NameError, EmailError, AgeError), наследующие от базового класса Exception.
#   Установите сообщения об ошибках в конструкторах этих классов, чтобы указать, какие
#   именно ошибки произошли.
# Подсказка № 2
#   Используйте свойства (геттеры и сеттеры) в классе User для контроля установки
#   значений атрибутов name, email, и age. Это позволяет выполнять проверки перед
#   присваиванием значений.
# Подсказка № 3
#   Убедитесь, что имя состоит из хотя бы двух слов, каждое из которых начинается с
#   заглавной буквы. Используйте метод split() для разделения имени на слова и
#   проверьте первый символ каждого слова с помощью isupper().
# Подсказка № 4
#   Убедитесь, что электронная почта содержит символ @ и точку . после символа @.
#   Используйте метод split('@') для разделения строки и проверяйте наличие точки в
#   части после @.
# Подсказка № 5
#   Убедитесь, что возраст является целым числом в пределах от 0 до 120. Используйте
#   функцию isinstance() для проверки типа данных и операторы сравнения для
#   проверки диапазона.
class UserException(Exception):
    pass


class NameError(UserException):
    def __str__(self):
        return ('Имя не соответствует формату. Имя должно состоять хотя бы из двух слов, '
                'каждое из которых начинается с заглавной буквы')


class EmailError(UserException):
    def __str__(self):
        return 'Email не соответствует формату. Электронная почта должна содержать символ @ и точку после @'


class AgeError(UserException):
    def __str__(self):
        return ('Возраст вне допустимого диапазона. Возраст должен быть '
                'положительным целым числом, не меньше 0 и не больше 120')


class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def __setattr__(self, key, value):
        if key == 'name':
            if not (len(value.split()) >= 2 and value.istitle()):
                raise NameError
        if key == 'email':
            if not ('@' in value and '.' in value[value.find('@') + 1:]):
                raise EmailError
        if key == 'age':
            if not (isinstance(value, int) and 0 <= value <= 120):
                raise AgeError
        super().__setattr__(key, value)


if __name__ == '__main__':
    try:
        p_1 = User('Vova Lada', 'dmn02@mail.ru', 12)
    except UserException as e:
        print(e)


# PERFECT SOLUTION
# class NameError(Exception):
#     def __init__(self):
#         super().__init__("Имя должно состоять из хотя бы двух слов, каждое из которых начинается с заглавной буквы.")
#
#
# class EmailError(Exception):
#     def __init__(self):
#         super().__init__("Электронная почта должна содержать символ '@' и точку '.' после '@'.")
#
#
# class AgeError(Exception):
#     def __init__(self):
#         super().__init__("Возраст должен быть целым числом от 0 до 120.")
#
#
# class User:
#     def __init__(self, name, email, age):
#         self.name = name
#         self.email = email
#         self.age = age
#     @property
#     def name(self):
#         return self._name
#     @name.setter
#     def name(self, value):
#         if not (len(value.split()) >= 2 and all(word[0].isupper() for word in value.split())):
#             raise NameError()
#         self._name = value
#     @property
#     def email(self):
#         return self._email
#
#     @email.setter
#     def email(self, value):
#         if '@' not in value or '.' not in value.split('@')[1]:
#             raise EmailError()
#         self._email = value
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, value):
#         if not (isinstance(value, int) and 0 <= value <= 120):
#             raise AgeError()
#         self._age = value
#
#
# # Пример использования:
# try:
#     user = User(name="John Doe", email="john.doe@example.com", age=25)
#     print(f"User created: {user.name}, {user.email}, {user.age}")
# except (NameError, EmailError, AgeError) as e:
#     print(e)






