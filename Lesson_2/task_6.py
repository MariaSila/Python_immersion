# Задание №6 Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

import decimal

CMD_WITHDRAW = "с"
CMD_DEPOSIT = "п"
CMD_EXIT = "в"
MULTIPLICITY = 50
NUMBER_OPERATION = 3
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(5_000_000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_BONUS = decimal.Decimal(3) / decimal.Decimal(100)

balance = decimal.Decimal(60_000_000)
count = 0

while True:
    action = input(f"Пополнить - '{CMD_DEPOSIT}', снять - '{CMD_WITHDRAW}', выйти - '{CMD_EXIT}' ")
    if action == CMD_EXIT:
        print(f"Заберите карту. баланс:{balance}у.е")
        break
    if balance > RICHNESS_SUM:
        percent = balance * RICHNESS_PERCENT
        balance -= percent
        print(f"Вычтен налог на богатство {RICHNESS_PERCENT * 100}%. "
              f"Сумма процента - {percent}. Баланс карты - {balance}")

    if action in (CMD_DEPOSIT, CMD_WITHDRAW):
        amount = 1
        while amount % MULTIPLICITY != 0:
            amount = decimal.Decimal(input(f"Введите сумму кратнную {MULTIPLICITY}: "))

        if action == CMD_DEPOSIT:
            count += 1
            balance += amount
            print(f"Пополнение карты на {amount}. Баланс карты: {balance}")
        elif action == CMD_WITHDRAW:
            percent = amount * PERCENT_REMOVAL
            percent = MIN_REMOVAL if percent < MIN_REMOVAL else MAX_REMOVAL if percent > MAX_REMOVAL else percent
            sub = amount + percent
            if balance > sub:
                balance -= sub
                count += 1
                print(f"Снятие с карты {amount}у.е. Сумма процента за снятие {percent}. "
                      f"Баланс карты {balance}")
            else:
                print(f"Недостаточно средств. Сумма снятия {amount}. Сумма процента за снятие {percent}."
                      f"Баланс карты {balance}")

        if count % NUMBER_OPERATION == 0:
            bonus = balance * PERCENT_BONUS
            balance += bonus
            print(f"Начислен бонус: {bonus} за каждую {NUMBER_OPERATION}. Баланс карты {balance}")
