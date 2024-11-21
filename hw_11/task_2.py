# Задача 2. Магия
# Для одной игры необходимо реализовать механику магии, где при соединении
# двух элементов получается новый.
#   У нас есть четыре базовых элемента: «Вода», «Воздух», «Огонь», «Земля».
#   Из них получаются новые: «Шторм», «Пар», «Грязь», «Молния», «Пыль», «Лава».
# Таблица преобразований:
#       ● Вода + Воздух = Шторм;
#       ● Вода + Огонь = Пар;
#       ● Вода + Земля = Грязь;
#       ● Воздух + Огонь = Молния;
#       ● Воздух + Земля = Пыль;
#       ● Огонь + Земля = Лава.
# Напишите программу, которая реализует все эти элементы. Каждый элемент
# необходимо организовать как отдельный класс. Если результат не определён,
# то возвращается None.
# Примечание: сложение объектов можно реализовывать через магический
# метод __add__, вот пример использования:
#       class ExampleOne:
#           def __add__(self, other):
#               return ExampleTwo()
#       class ExampleTwo:
#           answer = 'сложили два класса и вывели'
#       first_example = ExampleOne()
#       second_example = ExampleTwo()
#       result = first_example + second_example
#       print(result.answer)
# Дополнительно: придумайте свой элемент (или элементы) и реализуйте его
# взаимодействие с остальными.
# Подсказка № 1
#   Используйте магический метод __add__ для определения взаимодействия двух
#   элементов. Этот метод позволяет определить, что произойдет при сложении двух
#   объектов, и возвращает новый объект, если комбинация определена.
# Подсказка № 2
#   Создайте отдельные классы для каждого базового элемента (Вода, Воздух, Огонь,
#   Земля) и производных элементов (Шторм, Пар, Грязь, Молния, Пыль, Лава). Это
#   поможет разделить логику обработки различных типов взаимодействий.
# Подсказка № 3
#   Используйте проверку типа через isinstance внутри метода __add__ для определения,
#   с каким элементом происходит сложение. Это позволит точно определить результат
#   взаимодействия.
# Подсказка № 4
#   Добавьте метод __str__ или атрибут answer для каждого производного элемента, чтобы
#   можно было легко выводить результат взаимодействия в виде строки.
# Подсказка № 5
#   Перед созданием архива убедитесь, что исходный каталог существует, чтобы избежать
#   ошибок. Используйте os.path.isdir() для проверки существования каталога

class Water():
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Land):
            return Dirt()
        elif isinstance(other, Stone):
            return Sand()
        else:
            print(f'Магия не получилась {self.__class__.__name__} не взаимодействует с {other.__class__.__name__}')

    def __str__(self):
        return 'Вода'


class Air():
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Land):
            return Dust()
        elif isinstance(other, Stone):
            return Sand()
        else:
            print(f'Магия не получилась {self.__class__.__name__} не взаимодействует с {other.__class__.__name__}')

    def __str__(self):
        return 'Воздух'


class Fire():
    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Land):
            return Lava()
        elif isinstance(other, Stone):
            return Metal()
        else:
            print(f'Магия не получилась {self.__class__.__name__} не взаимодействует с {other.__class__.__name__}')

    def __str__(self):
        return 'Огонь'


class Land():
    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Stone):
            return Mountain()
        else:
            print(f'Магия не получилась {self.__class__.__name__} не взаимодействует с {other.__class__.__name__}')

    def __str__(self):
        return 'Земля'


class Stone():
    def __add__(self, other):
        if isinstance(other, Water) or isinstance(other, Air):
            return Sand()
        elif isinstance(other, Fire):
            return Metal()
        elif isinstance(other, Land):
            return Mountain()
        else:
            print(f'Магия не получилась {self.__class__.__name__} не взаимодействует с {other.__class__.__name__}')

    def __str__(self):
        return 'Камень'

class Storm():
    def __str__(self):
        return f'получили Шторм'


class Steam():
    def __str__(self):
        return f'получили Пар'


class Dirt():
    def __str__(self):
        return f'получили Грязь'


class Lightning():
    def __str__(self):
        return f'получили Молнию'


class Dust():
    def __str__(self):
        return f'получили Пыль'


class Lava():
    def __str__(self):
        return f'получили Лаву'


class Mountain():
    def __str__(self):
        return f'получили Гору'


class Metal():
    def __str__(self):
        return f'получили Металл'


class Sand():
    def __str__(self):
        return f'получили Песок'


def main():
    elements = [Water(), Air(), Fire(), Land(), Stone()]
    for el in elements:
        for i in range(len(elements)):
            if not isinstance(el, type(elements[i])):
                print(f'Из элементов {el} и {elements[i]} {el + elements[i]}')


if __name__ == '__main__':
    main()


# # PERFECT SOLUTION
# import random
#
# TRIES = 10
#
#
# class Storm:
#     answer = "Вы сложили Воду и Воздух и получили класс Шторм"
#
#
# class Steam:
#     answer = "Вы сложили Воду и Огонь и получили класс Пар"
#
#
# class Mud:
#     answer = "Вы сложили Воду и Землю и получили класс Грязь"
#
#
# class Bolt:
#     answer = "Вы сложили Воздух и Огонь и получили класс Молния"
#
#
# class Dust:
#     answer = "Вы сложили Воздух и Землю и получили класс Пыль"
#
#
# class Lava:
#     answer = "Вы сложили Огонь и Землю и получили класс Лава"
#
#
# class Fog:
#     answer = "Вы сложили Воду и Пыль и получили класс Туман"
#
#
# class Water:
#     def __add__(self, other):
#         if isinstance(other, Soil):
#             return Mud()
#         elif isinstance(other, Air):
#             return Storm()
#         elif isinstance(other, Fire):
#             return Steam()
#         elif isinstance(other, Dust):
#             return Fog()
#
#
# class Fire:
#     def __add__(self, other):
#         if isinstance(other, Air):
#             return Bolt()
#         elif isinstance(other, Soil):
#             return Lava()
#
#
# class Air:
#     def __add__(self, other):
#         if isinstance(other, Fire):
#             return Bolt()
#         elif isinstance(other, Soil):
#             return Dust()
#
#
# class Soil:
#     def __add__(self, other):
#         if isinstance(other, Water):
#             return Mud()
#         elif isinstance(other, Air):
#             return Dust()
#         elif isinstance(other, Fire):
#             return Lava()
#
#
# def main():
#     elements = [Water(), Fire(), Air(), Soil(), Dust()]
#     try_count = 0
#     while try_count < TRIES:
#         element_a = random.choice(elements)
#         element_b = random.choice(elements)
#         result = element_a + element_b
#         if result is None:
#             continue
#         try_count += 1
#         print(result.answer)
#         print()
#
#
# main()
