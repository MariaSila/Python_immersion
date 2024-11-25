# Задача 4. Класс с контролем цены и количества
# Создайте класс Product с атрибутами name, price, и quantity. price должен
# быть положительным числом, а quantity неотрицательным целым числом. При
# попытке установить price или quantity, должен производиться контроль значений.
# Подсказка № 1
# Используйте метод __setattr__ для контроля значений атрибутов. Переопределите
# метод __setattr__, чтобы проверять, что price является положительным числом, а
# quantity — неотрицательным целым числом, прежде чем устанавливать значение
# атрибутов.
# Подсказка № 2
# Проверьте тип и значение для price. Убедитесь, что price является либо целым
# числом, либо числом с плавающей точкой, и что оно больше нуля.
# Подсказка № 3
# Проверьте тип и значение для quantity. Убедитесь, что quantity является целым
# числом и не отрицательным.
# Подсказка № 4
# Используйте метод super().__setattr__ для установки атрибутов после проверки.
# Вызовите метод super().__setattr__ для фактического присвоения значений
# атрибутам после проверки.

class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __setattr__(self, key, value):
        if key == 'price':
            if not (isinstance(value, int) or isinstance(value, float) and value > 0):
                print('Цена должна быть положительным числом')
        elif key == 'quantity':
            if not (isinstance(value, int) and value > 0):
                print('Количество должно быть целым положительным числом')
        return super().__setattr__(key, value)

    def __str__(self):
        return f'{self.name}, цена: {self.price}, количество: {self.quantity}'


if __name__ == '__main__':
    p1 = Product('Книга', 25, 6)
    p2 = Product('Тетрадь', 2.5, 100)
    p3 = Product('Тетрадь', 2, 2)
    print(p1)
    print(p2)
    print(p3)


# PERFECT SOLUTION
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def __setattr__(self, name, value):
#         if name == 'price':
#             if not (isinstance(value, (int, float)) and value > 0):
#                 raise ValueError("Цена должна быть положительным числом")
#         elif name == 'quantity':
#             if not (isinstance(value, int) and value >= 0):
#                 raise ValueError("Количество должно быть неотрицательным целым числом")
#         super().__setattr__(name, value)
#
#     def __str__(self):
#         return f"Product(name={self.name}, price={self.price}, quantity = {self.quantity})"
#
#
# # Пример использования
# try:
#     prod = Product("Laptop", 1000, 10)
#     prod.price = 1200
#     prod.quantity = 5
#     print(prod)
# except ValueError as e:
#     print(e)