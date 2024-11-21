# Задание 1. Матрицы
# Вы стажируетесь в лаборатории искусственного интеллекта, в ней вам
# поручили разработать класс Matrix для обработки и анализа данных. Ваш класс
# должен предоставлять функциональность для выполнения основных операций
# с матрицами, таких как сложение, вычитание, умножение и транспонирование.
# Это будет полезно для обработки и структурирования больших объёмов
# данных, которые используются в обучении нейронных сетей.
# Задача
# 1. Создайте класс Matrix для работы с матрицами.
#   Реализуйте методы:
#       ○ сложения,
#       ○ вычитания,
#       ○ умножения,
#       ○ транспонирования матрицы.
# 2. Создайте несколько экземпляров класса Matrix и протестируйте реализованные операции.
# Советы
#       ● Методы сложения/вычитания/умножения должны получать параметром
#         другую матрицу (объект класса Matrix) и выполнять указанное действие
#         над своей и этой другой матрицей. Например, метод сложения должен
#         получить параметром новую матрицу и сложить её со своей текущей.
#       ● Метод транспонирования не должен ничего получать, он должен
#         работать исключительно со своей матрицей.
#       ● Транспонирование — это алгоритм, при котором строки матрицы
#         меняются местами с её столбцами:
#       ● Алгоритм транспонирования матрицы можно расписать следующим
#         образом:
#               1. Создать новую матрицу result с размерами, обратными размерам
#                   исходной матрицы. Количество строк новой матрицы равно
#                   количеству столбцов исходной, а количество столбцов новой
#                   матрицы равно количеству строк исходной.
#               2. Пройтись по каждому элементу исходной матрицы. Для каждого
#                   элемента с индексами (i, j):
#                           1. Поместить значение этого элемента (i, j) в ячейку с
#                               индексами (j, i) новой матрицы. То есть транспонирование
#                               происходит с помощью обмена индексов местами.
#                           2. После завершения цикла новая матрица result будет
#                               содержать транспонированную матрицу, которую можно вернуть.
# Подсказка № 1
#   Используйте вложенные циклы для инициализации матрицы. Для создания двумерного
#   массива (матрицы) размером rows на cols используйте вложенные списковые
#   включения (list comprehensions). Это создаст матрицу, заполненную нулями.
# Подсказка № 2
#   Добавьте проверку размеров матриц перед операциями. Перед выполнением
#   операций сложения, вычитания или умножения убедитесь, что размеры матриц
#   совместимы. Например, для сложения и вычитания матрицы должны иметь
#   одинаковые размеры, а для умножения количество столбцов первой матрицы должно
#   совпадать с количеством строк второй.
# Подсказка № 3
#   Используйте двойные циклы для операций сложения и вычитания. Для выполнения
#   операций сложения или вычитания матриц используйте двойные циклы, чтобы
#   пройтись по каждому элементу матрицы и выполнить соответствующую
#   арифметическую операцию.
# Подсказка № 4
#   Убедитесь, что метод умножения учитывает правила умножения матриц. Для
#   умножения матриц используйте тройной цикл: первый цикл по строкам первой
#   матрицы, второй по столбцам второй матрицы, и третий по элементам строки и
#   столбца для выполнения суммирования произведений.
# Подсказка № 5
#   Реализуйте метод __str__ для удобного вывода матрицы. Реализуйте метод __str__,
#   чтобы матрицы можно было легко выводить на экран. Используйте join() для
#   форматирования строк матрицы, а затем объедините их в одну строку с разделителем
#   новой строки

class Matrix:
    """ Создание матриц и математические действия над ними"""
    def __init__(self, rows, cols, data=None):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for j in range(cols)] for i in range(rows)] if data is None else data

    def __eq__(self, other):
        """ Сравнение размеров матриц """
        first = (self.rows, self.cols)
        second = (other.rows, other.cols)
        return first == second

    def add(self, other):
        """ Суммирование матриц через вызов метода"""
        if self != other:
            raise AttributeError('Сложение не возможно. Матрицы имеют разный размер.')
        result = [[self.data[row][col] + other.data[row][col] for col in range(self.cols)] for row in range(self.rows)]
        return Matrix(self.rows, self.cols, data=result)

    def __add__(self, other):
        """ Суммирование матриц через знак '+'"""
        if self != other:
            raise AttributeError('Сложение не возможно. Матрицы имеют разный размер.')
        result = [[self.data[row][col] + other.data[row][col] for col in range(self.cols)] for row in range(self.rows)]
        return Matrix(self.rows, self.cols, data=result)

    def subtract(self, other):
        """Вычитание матриц через вызов метода"""
        if self != other:
            raise AttributeError('Вычитание не возможно. Матрицы имеют разный размер.')
        result = [[self.data[row][col] - other.data[row][col] for col in range(self.cols)] for row in range(self.rows)]
        return Matrix(self.rows, self.cols, data=result)

    def __sub__(self, other):
        """ Вычитание матриц через знак '-'"""
        if self != other:
            raise AttributeError('Вычитание не возможно. Матрицы имеют разный размер.')
        result = [[self.data[row][col] - other.data[row][col] for col in range(self.cols)] for row in range(self.rows)]
        return Matrix(self.rows, self.cols, data=result)

    def multiply(self, other):
        """Умножение матриц через вызов метода"""
        if self.cols != other.rows:
            raise AttributeError('Умножение не возможно. Количество столбцов первой матрицы должно'
                                 ' совпадать с количество строк второй')
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    def __mul__(self, other):
        """Умножение матриц через знак '*'"""
        if self.cols != other.rows:
            raise AttributeError('Умножение не возможно. Количество столбцов первой матрицы должно'
                                 ' совпадать с количество строк второй')
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    def transpose(self):
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[j][i] = self.data[i][j]
        return result

    def __str__(self):
        return f'{'\n'.join('\t'.join(str(col) for col in row) for row in self.data)} \n'


if __name__ == '__main__':
    # Создание объектов
    m1 = Matrix(2, 3)
    m1.data = [[1, 2, 3], [4, 5, 6]]

    m2 = Matrix(2, 3)
    m2.data = [[7, 8, 9], [10, 11, 12]]

    m3 = Matrix(3, 2)
    m3.data = [[1, 2], [3, 4], [5, 6]]

    # Тестирование операций
    print(f'Матрица 1: \n{m1}')
    print(f'Матрица 2: \n{m2}')
    print(f'Матрица 3: \n{m3}')

    print(f'Сравнение размеров матриц m1 и m2 = {m1 == m2}')

    print(f'Сложение матриц дандер метод __add__: \n{m1 + m2}')
    print(f'Сложение матриц метод add: \n{m1.add(m2)}')

    print(f'Вычитание матриц дандер метод __sub__: \n{m1 - m2}')
    print(f'Вычитание матриц метод subtract: \n{m1.subtract(m2)}')

    print(f'Умножение матриц дандер метод __mul__: \n{m1 * m3}')
    print(f'Умножение матриц метод multiply: \n{m1.multiply(m3)}')

    print(f'Транспонированная матрица m1: \n{m1.transpose()}')


# # PERFECT SOLUTION
# # Класс Matrix для работы с матрицами
# class Matrix:
#     def __init__(self, rows, cols):
#         self.rows = rows
#         self.cols = cols
#         self.data = [[0 for _ in range(cols)] for _ in range(rows)]
#
#     def add(self, other):
#         if self.rows != other.rows or self.cols != other.cols:
#             raise ValueError("Размеры матриц не совпадают для сложения")
#         result = Matrix(self.rows, self.cols)
#         for i in range(self.rows):
#             for j in range(self.cols):
#                 result.data[i][j] = self.data[i][j] + other.data[i][j]
#         return result
#
#     def subtract(self, other):
#         if self.rows != other.rows or self.cols != other.cols:
#             raise ValueError("Размеры матриц не совпадают для вычитания")
#         result = Matrix(self.rows, self.cols)
#         for i in range(self.rows):
#             for j in range(self.cols):
#                 result.data[i][j] = self.data[i][j] - other.data[i][j]
#         return result
#
#     def multiply(self, other):
#         if self.cols != other.rows:
#             raise ValueError("Количество столбцов первой матрицы должно совпадать с количеством строк второй матрицы")
#         result = Matrix(self.rows, other.cols)
#         for i in range(self.rows):
#             for j in range(other.cols):
#                 for k in range(self.cols):
#                     result.data[i][j] += self.data[i][k] * other.data[k][j]
#         return result
#
#     def transpose(self):
#         result = Matrix(self.cols, self.rows)
#         for i in range(self.rows):
#             for j in range(self.cols):
#                 result.data[j][i] = self.data[i][j]
#         return result
#
#     def __str__(self):
#         res = "\n".join(["\t".join(map(str, row)) for row in self.data])
#         return res
#
#
# # Примеры работы с классом:
# # Создание экземпляров класса Matrix
# m1 = Matrix(2, 3)
# m1.data = [[1, 2, 3], [4, 5, 6]]
#
# m2 = Matrix(2, 3)
# m2.data = [[7, 8, 9], [10, 11, 12]]
#
# # Тестирование операций
# print("Матрица 1:")
# print(m1)
# print("Матрица 2:")
# print(m2)
# print("Сложение матриц:")
# print(m1.add(m2))
# print("Вычитание матриц:")
# print(m1.subtract(m2))
#
# m3 = Matrix(3, 2)
# m3.data = [[1, 2], [3, 4], [5, 6]]
#
# print("Умножение матриц:")
# print(m1.multiply(m3))
# print("Транспонирование матрицы 1:")
# print(m1.transpose())





