# Задача 3. Тестирование класса с использованием doctest
# Напишите класс Rectangle, который управляет прямоугольником. Класс должен
# поддерживать следующие методы:
#       ● set_dimensions(width, height): устанавливает ширину и высоту
#           прямоугольника.
#       ● get_area(): возвращает площадь прямоугольника.
#       ● get_perimeter(): возвращает периметр прямоугольника.
# Напишите 3 теста с помощью doctest.
# Подсказка № 1
#   Убедитесь, что при создании объекта Rectangle с заданными шириной и высотой,
#   методы get_area и get_perimeter возвращают правильные значения.
# Подсказка № 2
#   После установки новых размеров с помощью set_dimensions, убедитесь, что методы
#   get_area и get_perimeter обновляются корректно.
# Подсказка № 3
#   Убедитесь, что метод set_dimensions выбрасывает исключение ValueError, если
#   переданы отрицательные значения для ширины или высоты.
# Подсказка № 4
#   Убедитесь, что метод set_dimensions правильно обрабатывает нулевые значения.
#   Для нулевых значений площадь и периметр должны быть корректными (площадь
#   будет 0).

class Rectangle:
    """
    >>> rect = Rectangle(2, 4)
    >>> rect.get_perimeter()
    12
    >>> rect.get_area()
    8
    >>> rect.set_dimensions(4, 8)
    >>> rect.get_perimeter()
    24
    >>> rect.get_area()
    32
    >>> rect_2 = Rectangle('2', 4)
    Traceback (most recent call last):
    ...
    ValueError
    >>> rect_2 = Rectangle(-2, 4)
    Traceback (most recent call last):
    ...
    ValueError
    >>> rect.set_dimensions(-8, 6)
    Traceback (most recent call last):
    ...
    ValueError
    >>> rect.set_dimensions('8', 6)
    Traceback (most recent call last):
    ...
    ValueError
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_dimensions(self, width, height):
        """Устанавливает ширину и высоту прямоугольника"""
        self.width = width
        self.height = height

    def __setattr__(self, key, value):
        if key == 'width' or key == 'height':
            if not (isinstance(value, (int, float)) and value > 0):
                raise ValueError
        super().__setattr__(key, value)

    def get_area(self):
        """Возвращает площадь прямоугольника"""
        return self.width * self.height

    def get_perimeter(self):
        """Возвращает периметр прямоугольника"""
        return (self.width + self.height) * 2

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

    # rect = Rectangle(2, 4)
    # print(rect)
    # print(rect.get_perimeter())
    # print(rect.get_area())
    # rect.set_dimensions(4, 8)
    # print(rect)


# PERFECT SOLUTION
# import doctest
#
#
# class Rectangle:
#     def __init__(self, width=0, height=0):
#         """
#         Инициализация прямоугольника с заданными шириной и высотой.
#         >>> r = Rectangle(3, 4)
#         >>> r.get_area()
#         12
#         >>> r.get_perimeter()
#         14
#         """
#         self.width = width
#         self.height = height
#
#     def set_dimensions(self, width, height):
#         """
#         Устанавливает ширину и высоту прямоугольника.
#         >>> r = Rectangle()
#         >>> r.set_dimensions(6, 7)
#         >>> r.get_area()
#         42
#         >>> r.get_perimeter()
#         26
#         """
#         if width <= 0 or height <= 0:
#             raise ValueError("Ширина и высота должны быть положительными числами.")
#         self.width = width
#         self.height = height
#
#     def get_area(self):
#         """Возвращает площадь прямоугольника."""
#         return self.width * self.height
#
#     def get_perimeter(self):
#         """Возвращает периметр прямоугольника."""
#         return 2 * (self.width + self.height)
#
#
# if __name__ == "__main__":
#     doctest.testmod()
