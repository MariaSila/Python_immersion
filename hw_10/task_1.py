# Задание 1. Отцы, матери и дети.
# Вася совсем заскучал на работе и решил побаловаться с кодом проекта. Он
# Реализуйте два класса: «Родитель» и «Ребёнок». У родителя есть: ● имя, ● возраст, ● список детей.
# И он может: ● сообщить информацию о себе, ● успокоить ребёнка, ● покормить ребёнка.
# У ребёнка есть: ● имя, ● возраст (должен быть меньше возраста родителя хотя бы на 16 лет),
#                   ● состояние спокойствия, ● состояние голода.
# Реализация состояний — на ваше усмотрение. Это может быть и простой «флаг»,
# и словарь состояний, и что-то поинтереснее.
# Подсказка № 1
# Используйте проверку на разницу в возрасте при добавлении ребёнка в список детей.
# Это поможет убедиться, что разница в возрасте между родителем и ребёнком
# составляет хотя бы 16 лет.
# Подсказка № 2
# Реализуйте методы feed() и calm() в классе Parent, чтобы они изменяли
# соответствующие состояния ребёнка. Например, состояние голода можно представить
# как логическое значение (True/False) или строку («голоден»/«сыт»).
# Подсказка № 3
# Используйте методы __str__() или __repr__() в классах Parent и Child, чтобы
# предоставить более удобный вывод информации о них. Это улучшит читаемость кода,
# когда объекты классов будут выводиться в консоль.
# Подсказка № 4
# Добавьте метод для вывода информации о детях родителя. Это позволит родителю
# предоставить информацию о всех своих детях в одном месте, что упростит управление объектами

from random import choice


class Parent():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.list_children = []

    def add_child(self, child):
        if self.age - child.age >= 16:
            if child.name not in self.list_children:
                self.list_children.append(child.name)
                print(f'Ребенок {child.name} добавлен родителю {self.name}')
            else:
                print(f'Ребенок {child.name} не добавлен. '
                      f'{child.name} уже есть в списке детей {self.name}')
        else:
            print(f'Ребенок {child.name} не добавлен. '
                  f'Разница в возрасте = {self.age - child.age}, что меньше 16')
        return self.list_children

    def get_child(self):
        return f'Список детей: {self.list_children}' if self.list_children else f'Нет детей'

    def do_calm(self, child):
        if not child.calm:
            child.calm = True
            print(f'Ребенок {child.name} успокоен')
        else:
            print(f'Ребенок {child.name} уже спокоен')

    def do_feed(self, child):
        if not child.hunger:
            child.hunger = True
            print(f'Ребенок {child.name} накормлен')
        else:
            print(f'Ребенок {child.name} уже сыт')

    def __repr__(self):
        return f'Родитель: {self.name}; Возраст: {self.age}; {self.get_child()}'


class Child():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.calm = choice([True, False])
        self.hunger = choice([True, False])

    def get_calm(self):
        if self.calm:
            return f'Спокоен'
        else:
            return f'Беспокоен'

    def get_hunger(self):
        if self.hunger:
            return f'Сыт'
        else:
            return f'Голоден'

    def set_age(self, age):
        last_age = self.age
        self.age = age
        print(f'Изменен возраст {self.name} с {last_age} на {self.age}')

    def __repr__(self):
        return f'Ребенок: {self.name}; Возраст: {self.age}; Состояние: {self.get_calm()}, {self.get_hunger()}'


# Создание объектов
p_Mark = Parent('Mark', 30)
ch_lena = Child('Lena', 8)
ch_sveta = Child('Sveta', 15)
p_Masha = Parent('Masha', 29)

# Вывод инфо о родителях без детей
print(p_Masha)
print(p_Mark)

# Добавление детей без ошибок
p_Mark.add_child(ch_lena)
p_Masha.add_child(ch_lena)

# Добавление детей на проверку ошибки
p_Mark.add_child(ch_lena)
p_Mark.add_child(ch_sveta)

# Изменяем возраст ребенка
ch_sveta.set_age(12)

# Добавляем детей после исправления возраста
p_Mark.add_child(ch_sveta)

# Получаем список детей родителей
print(p_Mark.get_child())
print(p_Masha.get_child())

# Вывод инфо о родителях
print(p_Masha)
print(p_Mark)

# Вывод инфо о детях
print(ch_sveta)
print(ch_lena)

# Покормить и успокоить детей
p_Mark.do_calm(ch_sveta)
p_Mark.do_feed(ch_sveta)
p_Masha.do_calm(ch_lena)
p_Masha.do_feed(ch_lena)

# Вывод инфо о детях
print(ch_sveta)
print(ch_lena)


# # perfect solution
# class Parent:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#         self.children = []
#
#     def info(self):
#         """Сообщает информацию о родителе"""
#         print(f"Меня зовут {self.name}, мне {self.age} лет")
#
#     def add_child(self, child):
#         """Добавляет ребёнка в список детей, если разница в возрасте больше 16 лет"""
#         if self.age - child.age >= 16:
#             self.children.append(child)
#             print(f"Ребёнок {child.name} добавлен к {self.name}.")
#         else:
#             print(f"Ребёнок {child.name} не добавлен к {self.name}, так как разница в возрасте слишком мала.")
#
#     def feed(self, child):
#         """Кормит ребёнка, изменяя его состояние голода"""
#         if child in self.children:
#             child.hungry = False
#             print(f"{self.name} покормил(а) {child.name}.")
#         else:
#             print(f"{child.name} не является ребёнком {self.name}.")
#
#     def calm(self, child):
#         """Успокаивает ребёнка, изменяя его состояние спокойствия"""
#         if child in self.children:
#             child.calm = True
#             print(f"{self.name} успокоил(а) {child.name}.")
#         else:
#             print(f"{child.name} не является ребёнком {self.name}.")
#
#     def list_children(self):
#         """Выводит информацию обо всех детях родителя"""
#         if self.children:
#             print(f"У {self.name} есть следующие дети:")
#             for child in self.children:
#                 print(f" - {child}")
#         else:
#             print(f"У {self.name} нет детей.")
#
#
# class Child:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#         self.calm = False  # Ребёнок по умолчанию не спокоен
#         self.hungry = True  # Ребёнок по умолчанию голоден
#
#     def get_status(self):
#         """Сообщает текущее состояние ребёнка"""
#         calm_status = "спокоен" if self.calm else "не спокоен"
#         hungry_status = "сыт" if not self.hungry else "голоден"
#         print(f"Ребёнок {self.name} {calm_status} и {hungry_status}.")
#
#     def __str__(self):
#         """Представление объекта ребёнка в виде строки"""
#         return f"Ребёнок {self.name}, {self.age} лет"
#
#
# # Создание объектов
# parent = Parent("Иван", 40)
# child1 = Child("Анна", 20)
# child2 = Child("Петя", 10)
# child3 = Child("Маша", 3)
#
# # Добавление детей к родителю
# for child in [child1, child2, child3]:
#     parent.add_child(child)
#
# # Вывод информации о родителе и его детях
# parent.info()
# parent.list_children()
#
# # Родитель кормит и успокаивает детей
# for child in parent.children:
#     parent.feed(child)
#     parent.calm(child)
#     child.get_status()

