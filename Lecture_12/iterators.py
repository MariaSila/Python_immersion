# Создаём итераторы


# --------------------------------------------------------------
# STEP 1. Если экземпляр класса должен итерироваться, необходимо
# реализовать пару дандер методов.
# Создадим класс экземпляр которого будет выдавать числа Фибоначчи в диапазоне
# начиная с числа больше или равного start и заканчивая числом меньше stop.
# Внутри дандер __init__ запомнили границы start и stop и определили нулевое и
# первое число Фибоначчи в свойствах first и second соответственно.
# Создание экземпляра не вызывает проблем. А попытка получить числа в цикле
# увенчалась ошибкой. Python сообщил, что объект не итерируемый.

# class Fibonacci:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#         self.first = 0
#         self.second = 1
#
#
# fib = Fibonacci(20, 100)
# for num in fib:  # TypeError: 'Fibonacci' object is not iterable
#     print(num)


# --------------------------------------------------------------------------------------
# STEP 2. Возврат итератора, __iter__
# Для того, чтобы объект стал итерируемым, ему необходимо вернуть
# объект-итератор. В нашем случае экземпляр класса и есть объект-итератор.
# Следовательно он должен вернуть сам себя. Для возврата итератора нужно создать
# дандер метод __iter__.
# Две строки метода вернули ссылку на самого себя. В результате получаем новую
# ошибку. Вернулся не итерируемый объект.

# class Fibonacci:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#         self.first = 0
#         self.second = 1
#
#     def __iter__(self):
#         return self
#
#
# fib = Fibonacci(20, 100)
# for num in fib: # TypeError: iter() returned non-iterator of type 'Fibonacci'
#     print(num)


# --------------------------------------------------------------------------------------
# STEP 3. Возврат очередного значения, __next__
# Как вы помните из лекции об итераторах и генераторах, любая итерация
# представляет из себя последовательный вызов функции next() с итератором в
# качестве аргумента.
# Для возврата такого значения необходимо определить дандер метод __next__.
# Итератор отработал как и ожидалось.
#   ➢ дандер __next__ создаёт цикл пока число в first не превысит значение stop
#   ➢ получаем следующую пару Фибоначчи в first и second
#   ➢ если first оказывается внутри диапазона [start, stop), возвращаем очередной элемент
#   ➢ обязательным условием для завершения итерации является вызов ошибки
#       StopIteration. Python обрабатывает её как сигнал для завершения итерации и
#       перехода к следующему за циклом коду. Остановки кода по ошибке не будет.

# class Fibonacci:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#         self.first = 0
#         self.second = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.first < self.stop:
#             self.first, self.second = self.second, self.first + self.second
#             if self.start <= self.first < self.stop:
#                 return self.first
#         raise StopIteration
#
#
# fib = Fibonacci(20, 100)
# for num in fib:
#     print(num)


# ------------------------------------------------------------------------------------
# class Iter:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#     def __iter__(self):
#         return self
#     def __next__(self):
#         for i in range(self.start, self.stop):
#             return chr(i)
#         raise StopIteration
#
#
# chars = Iter(65, 91)
# for c in chars:
#     print(c)