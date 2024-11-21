# Задача 3. Класс Rectangle - работа с прямоугольниками
# Разработайте программу для работы с прямоугольниками. Необходимо создать класс
# Rectangle, который будет представлять прямоугольник с заданными шириной и высотой.
# Атрибуты класса:
# width (int): Ширина прямоугольника. height (int): Высота прямоугольника.
# Методы класса:
# __init__(self, width, height=None): Конструктор класса. Принимает ширину и
#       высоту прямоугольника. Если высота не указана (по умолчанию None), то считается, что
#       прямоугольник является квадратом, и высота устанавливается равной ширине.
# perimeter(self): Метод для вычисления периметра прямоугольника. Возвращает целое
#       число - значение периметра.
# area(self): Метод для вычисления площади прямоугольника. Возвращает целое число -
#       значение площади.
# __add__(self, other): Магический метод, который определяет операцию сложения (+)
#       для двух прямоугольников. Принимает другой прямоугольник other. Создает новый
#       прямоугольник, который представляет собой объединение исходных прямоугольников по
#       периметру. Новая ширина и высота вычисляются также на основе объединения.
#       Возвращает новый прямоугольник.
# __sub__(self, other): Магический метод, который определяет операцию вычитания (-)
#       одного прямоугольника из другого. Принимает вычитаемый прямоугольник other. Создает
#       новый прямоугольник, представляющий разницу периметров исходных прямоугольников, и
#       вычисляет высоту на основе этой разницы. Новая ширина вычисляется также на основе
#       разницы. Возвращает новый прямоугольник.
# __lt__(self, other): Магический метод, который определяет операцию "меньше" (<)
#       для двух прямоугольников. Принимает другой прямоугольник other. Возвращает True, если
#       площадь первого прямоугольника меньше площади второго, иначе False.
# __eq__(self, other): Магический метод, который определяет операцию "равно" (==)
#       для двух прямоугольников. Принимает другой прямоугольник other. Возвращает True, если
#       площади равны, иначе False.
# __le__(self, other): Магический метод, который определяет операцию "меньше или
#       равно" (<=) для двух прямоугольников. Принимает другой прямоугольник other. Возвращает
#       True, если площадь первого прямоугольника меньше или равна площади второго, иначе False.
# __str__(self): Магический метод, возвращающий строковое представление
#       прямоугольника. Возвращает строку, описывающую ширину и высоту прямоугольника в виде:
#               Прямоугольник со сторонами 2 и 3, где первое число - это ширина, а второе - высота.
# __repr__(self): Магический метод, возвращающий строковое представление
#       прямоугольника, которое может быть использовано для создания нового объекта такого же
#       класса с теми же атрибутами.
# Подсказка № 1
#       Используйте проверку условия в конструкторе для создания квадрата. В конструкторе
#       класса Rectangle используйте тернарный оператор для установки значения высоты
#       (height) равным ширине (width), если высота не указана.
# Подсказка № 2
#       Применяйте метод abs для вычитания периметров. В методе __sub__, для
#       корректного расчета разницы между периметрами двух прямоугольников, используйте
#       функцию abs, чтобы избежать отрицательных значений.
# Подсказка № 3
#       Разделяйте ответственность методов. Создайте отдельные методы для вычисления
#       периметра и площади, чтобы они могли быть переиспользованы в магических методах
#       __add__, __sub__ и методах сравнения.
# Подсказка № 4
#       Используйте обратный расчет сторон для новых прямоугольников. При объединении
#       или вычитании прямоугольников, рассчитывайте стороны нового прямоугольника
#       исходя из вычисленного периметра, разделяя его на 4, чтобы получить ширину и высоту.
# Подсказка № 5
#       Обрабатывайте случай, когда площади прямоугольников равны в методе сравнения
#       __le__, возвращая True, если площади равны или первая меньше второй.

class Rectangle():
    def __init__(self, width, height=None):
        self.width = width
        self.height = height if height is not None else width

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) * 2

    def __add__(self, other):
        new_perimetr = self.get_perimeter() + other.get_perimeter()
        width = new_perimetr // 4
        height = int((new_perimetr - width * 2) / 2)
        return Rectangle(width, height)

    def __sub__(self, other):
        new_perimetr = abs(self.get_perimeter() - other.get_perimeter())
        width = new_perimetr // 4
        height = int((new_perimetr - width * 2) // 2)
        return Rectangle(width, height)

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()

    def __str__(self):
        return f'Прямоугольник со сторонами {self.width} и {self.height}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.width}, {self.height})'


def main():
    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(3, 7)

    print(f"Периметр rect1: {rect1.get_perimeter()}")
    print(f"Периметр rect2: {rect2.get_perimeter()}")
    print(f"Площадь rect1: {rect1.get_area()}")
    print(f"Площадь rect2: {rect2.get_area()}")

    print(f"rect1 < rect2: {rect1 < rect2}")
    print(f"rect1 == rect2: {rect1 == rect2}")
    print(f"rect1 <= rect2: {rect1 <= rect2}")

    rect3 = rect1 + rect2
    rect4 = rect1 - rect2

    print(f"Периметр rect3: {rect3.get_perimeter()}")
    print(f"Периметр rect4: {rect4.get_perimeter()}")
    print(f"Площадь rect3: {rect3.get_area()}")
    print(f"Площадь rect4: {rect4.get_area()}")

    print(rect3)
    print(f'{rect4}')

    print(f'{rect3=}')
    print(repr(rect4))


if __name__ == '__main__':
    main()


# # PERFECT SOLUTION
# class Rectangle:
#     def __init__(self, width, height=None):
#         self.width = width
#         self.height = height if height is not None else width
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#     def area(self):
#         return self.width * self.height
#
#     def __add__(self, other):
#         new_perimeter = self.perimeter() + other.perimeter()
#         new_width = new_perimeter // 4
#         new_height = new_width
#         return Rectangle(new_width, new_height)
#
#     def __sub__(self, other):
#         new_perimeter = abs(self.perimeter() - other.perimeter())
#         new_width = new_perimeter // 4
#         new_height = new_width
#         return Rectangle(new_width, new_height)
#
#     def __lt__(self, other):
#         return self.area() < other.area()
#
#     def __eq__(self, other):
#         return self.area() == other.area()
#
#     def __le__(self, other):
#         return self.area() <= other.area()
#
#     def __str__(self):
#         return f"Прямоугольник со сторонами {self.width} и {self.height}"
#
#     def __repr__(self):
#         return f"Rectangle({self.width}, {self.height})"
#
#
# # Примеры работы с классом Rectangle
# rect1 = Rectangle(5, 10)
# rect2 = Rectangle(3, 7)
#
# # Вывод периметра и площади
# print(f"Периметр rect1: {rect1.perimeter()}")  # Вывод: 30
# print(f"Площадь rect2: {rect2.area()}")  # Вывод: 21
#
# # Сравнение прямоугольников по площади
# print(f"rect1 < rect2: {rect1 < rect2}")  # Вывод: False
# print(f"rect1 == rect2: {rect1 == rect2}")  # Вывод: False
# print(f"rect1 <= rect2: {rect1 <= rect2}")  # Вывод: False
#
# # Сложение и вычитание прямоугольников
# rect3 = rect1 + rect2
# print(f"Периметр rect3: {rect3.perimeter()}")  # Вывод: 50
# rect4 = rect1 - rect2
# print(f"Ширина rect4: {rect4.width}")  # Вывод: 2
#
# # Дополнительный тест для repr и str
# print(rect3)  # Вывод: Прямоугольник со сторонами 12 и 12
# print(repr(rect4))  # Вывод: Rectangle(2, 2)