# Задача 5. Абстрактный класс
# Вы работаете в компании, занимающейся разработкой программного обеспечения
# для архитектурных проектов. Вам необходимо разработать программу для расчёта
# площади различных геометрических фигур, таких как круги, прямоугольники и
# треугольники.
# Задача
# Создайте:
#   ● класс Shape, который будет базовым классом для всех фигур и будет
#       хранить пустой метод area, который наследники должны переопределить;
#   ● класс Circle;
#   ● класс Rectangle;
#   ● класс Triangle.
# Классы Circle, Rectangle и Triangle наследуют от класса Shape и реализуют метод
# для вычисления площади фигуры.
# Дополнительно: изучите информацию о работе с абстрактными классами.
# На основе этой информации сделайте так, чтобы:
#       1. Нельзя было создавать объекты класса Shape.
#       2. Наследники класса Shape переопределяли его метод area, чтобы объекты
#           этих классов можно было использовать.
# Подсказка № 1
#   Используйте модуль abc для создания абстрактных классов. Импортируйте класс ABC
#   и декоратор abstractmethod из модуля abc, чтобы сделать ваш базовый класс
#   абстрактным и определить абстрактные методы, которые должны быть реализованы в
#   дочерних классах.
# Подсказка № 2
#   Переопределите метод area в дочерних классах. Убедитесь, что каждый из
#   классов-наследников (Circle, Rectangle, Triangle) реализует метод area, который
#   рассчитывает площадь фигуры в соответствии с её формулой.
# Подсказка № 3
#   Не создавайте экземпляры абстрактного класса. Попробуйте создать экземпляр класса
#   Shape, чтобы убедиться, что это невозможно из-за его абстрактности.
from math import pi
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def area(self):
        return (self.length * self.height) / 2


if __name__ == '__main__':
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 8)

    # Вычисление площади фигур
    circle_area = circle.area()
    rectangle_area = rectangle.area()
    triangle_area = triangle.area()

    # Вывод результатов
    print("Площадь круга:", circle_area)
    print("Площадь прямоугольника:", rectangle_area)
    print("Площадь треугольника:", triangle_area)


# # PERFECT SOLUTION
# import math
# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#
# class Circle(Shape):
#     """Класс для представления круга, наследует от Shape."""
#
#     def __init__(self, radius):
#         """Инициализация круга с заданным радиусом."""
#         self.radius = radius
#
#     def area(self):
#         """Вычисление площади круга.Формула: π * радиус^2"""
#         return math.pi * self.radius ** 2
#
#
# class Rectangle(Shape):
#     """Класс для представления прямоугольника, наследует от Shape."""
#
#     def __init__(self, width, height):
#         """Инициализация прямоугольника с заданной шириной и высотой."""
#         self.width = width
#         self.height = height
#
#     def area(self):
#         """Вычисление площади прямоугольника. Формула: ширина * высота"""
#         return self.width * self.height
#
#
# class Triangle(Shape):
#     """Класс для представления треугольника, наследует от Shape."""
#     def __init__(self, base, height):
#         """Инициализация треугольника с заданной основой и высотой."""
#         self.base = base
#         self.height = height
#
#     def area(self):
#         """Вычисление площади треугольника. Формула: 0.5 * основа * высота"""
#         return 0.5 * self.base * self.height
#
#
# # Создание экземпляров классов
# circle = Circle(5)
# rectangle = Rectangle(4, 6)
# triangle = Triangle(3, 8)
#
# # Вычисление площади фигур
# circle_area = circle.area()
# rectangle_area = rectangle.area()
# triangle_area = triangle.area()
#
# # Вывод результатов
# print("Площадь круга:", circle_area)
# print("Площадь прямоугольника:", rectangle_area)
# print("Площадь треугольника:", triangle_area)
#
# # Попытка создания экземпляра абстрактного класса Shape (должно вызвать ошибку)
# try:
#     shape = Shape()  # Ожидается ошибка
# except TypeError as e:
#     print(f"Ошибка: {e}")
