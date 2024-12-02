# Задание 1. Тестирование класса с использованием pytest
# Напишите класс BankAccount, который управляет балансом счета. Он должен
# поддерживать следующие методы:
#   ● deposit(amount): добавляет указанную сумму к балансу.
#   ● withdraw(amount): снимает указанную сумму с баланса, если достаточно
#       средств.
#   ● get_balance(): возвращает текущий баланс счета.
# При попытке снять больше средств, чем доступно на счете, должно
# выбрасываться исключение InsufficientFundsError. Напишите как минимум
# 5 тестов для проверки работы классов и его методов.
# Подсказка № 1
#   Проверьте, что начальный баланс создаваемого объекта BankAccount корректен,
#   используя значение, переданное в конструкторе. Убедитесь, что баланс
#   инициализируется правильно при создании объекта.
# Подсказка № 2
#   Проверьте, что метод deposit корректно добавляет указанную сумму к текущему
#   балансу. Убедитесь, что сумма депозита положительна и увеличивает баланс на
#   ожидаемое значение.
# Подсказка № 3
#   Убедитесь, что метод withdraw корректно уменьшает баланс на указанную сумму,
#   если на счету достаточно средств. Проверьте правильность работы метода при
#   различных значениях суммы.
# Подсказка № 4
#   Убедитесь, что метод withdraw корректно выбрасывает исключение
#   InsufficientFundsError, когда пытаются снять больше средств, чем доступно на
#   счету. Используйте pytest.raises для проверки этого поведения.
# Подсказка № 5
#   Проверьте, что при создании объекта BankAccount без указания начального баланса,
#   баланс инициализируется как 0. Это поможет убедиться в правильности работы
#   конструктора с дефолтными значениями.

class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def __setattr__(self, key, value):
        if key == 'balance':
            if not (isinstance(value, (int, float)) and 0 <= value):
                raise ValueError('Баланс должен быть положительным целым или вещественным числом')
        super().__setattr__(key, value)

    def deposit(self, amount):
        """Добавляет указанную сумму к балансу"""
        if not (isinstance(amount, (int, float)) and 0 < amount):
            raise ValueError('Сумма для пополнения должна быть положительным целым или вещественным числом')
        self.balance += amount

    def withdraw(self, amount):
        """Снимает указанную сумму с баланса, если достаточно средств"""
        if not (isinstance(amount, (int, float)) and 0 < amount):
            raise ValueError('Сумма для снятия должна быть положительным целым или вещественным числом')
        elif amount > self.balance:
            raise InsufficientFundsError('Недостаточно средств на счете')
        self.balance -= amount

    def get_balance(self):
        """Возвращает текущий баланс счета"""
        return f'Сумма на счете {self.balance}'


if __name__ == '__main__':
    account = BankAccount()
    print(account.get_balance())
    try:
        account.deposit(100)
        print(account.get_balance())
        account.deposit(12.5)
        print(account.get_balance())
        account.withdraw(400)
        print(account.get_balance())
    except (ValueError, InsufficientFundsError) as e:
        print(e)


# PERFECT SOLUTION
# class InsufficientFundsError(Exception):
#     def __init__(self):
#         super().__init__("Недостаточно средств на счете.")
#
#
# class BankAccount:
#     def __init__(self, initial_balance=0):
#         self.balance = initial_balance
#
#     def deposit(self, amount):
#         if amount <= 0:
#             raise ValueError("Сумма депозита должна быть положительной.")
#         self.balance += amount
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             raise InsufficientFundsError()
#         self.balance -= amount
#
#     def get_balance(self):
#         return self.balance
#
#
# # КОД ТЕСТИРОВАНИЯ
# import pytest
#
#
# @pytest.fixture
# def bank_account():
#     # Подготовка тестового состояния
#     return BankAccount(100)  # Начальный баланс 100
#
#
# def test_initial_balance(bank_account):
#     # Проверка начального баланса
#     assert bank_account.get_balance() == 100
#
#
# def test_deposit(bank_account):
#     # Проверка депозита
#     bank_account.deposit(50)
#     assert bank_account.get_balance() == 150
#
#
# def test_withdraw(bank_account):
#     # Проверка снятия средств
#     bank_account.withdraw(30)
#     assert bank_account.get_balance() == 70
#
#
# def test_withdraw_insufficient_funds(bank_account):
#     # Проверка снятия больше средств, чем доступно
#     with pytest.raises(InsufficientFundsError):
#         bank_account.withdraw(200)
#
#
# def test_deposit_negative_amount(bank_account):
#     # Проверка депозита отрицательной суммы
#     with pytest.raises(ValueError):
#         bank_account.deposit(-10)
