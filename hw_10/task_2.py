# Задача 2. Совместное проживание
# Чтобы понять, стоит ли ему жить с кем-то или лучше остаться в гордом
# одиночестве, Артём решил провести необычное исследование. Для этого он
# реализовал модель человека и модель дома.

# Человек может (должны быть такие методы):
#   ● есть (+ сытость, − еда);
#   ● работать (− сытость, + деньги);
#   ● играть (− сытость);
#   ● ходить в магазин за едой (+ еда, − деньги);
#   ● прожить один день (выбирает одно действие согласно описанному ниже приоритету и выполняет его).

# У человека есть (должны быть такие атрибуты):
#   ● имя,
#   ● степень сытости (изначально 50),
#   ● дом.

# В доме есть:
#   ● холодильник с едой (изначально 50 еды),
#   ● тумбочка с деньгами (изначально 0 денег).

# Если сытость человека становится меньше нуля, человек умирает.
# Логика действий человека определяется следующим образом:
#   1. Генерируется число кубика от 1 до 6.
#   2. Если сытость < 20, то нужно поесть.
#   3. Иначе, если еды в доме < 10, то сходить в магазин.
#   4. Иначе, если денег в доме < 50, то работать.
#   5. Иначе, если кубик равен 1, то работать.
#   6. Иначе, если кубик равен 2, то поесть.
#   7. Иначе играть.

# По такой логике эксперимента человеку надо прожить 365 дней.
# Реализуйте такую программу и создайте двух людей, живущих в одном доме.
# Проверьте работу программы несколько раз.

# Подсказка № 1
# Используйте функцию random.randint(1, 6) для моделирования броска кубика. Это
# поможет определить случайное действие, которое будет выполнять человек в течение дня.
# Подсказка № 2
# Определите методы для каждого действия человека (например, eat, work, play,
# shop_for_food), чтобы каждый метод изменял соответствующие атрибуты человека
# и дома (сытость, еда, деньги).
# Подсказка № 3
# Создайте класс House, в котором будут храниться ресурсы (еда и деньги). Это поможет
# легко управлять ресурсами и отслеживать их изменения в течение времени.
# Подсказка № 4
# Проверьте, не достигла ли сытость человека нуля, в методе live_day. Если сытость
# упала ниже нуля, программа должна завершиться, чтобы указать на смерть
# персонажа.
# Подсказка № 5
# Используйте цикл для моделирования жизни человека в течение 365 дней. Этот цикл
# должен вызывать метод live_day каждый день и проверять, выжил ли человек
from random import randint


class Human():
    MAX_SATIETY = 100
    ONE_MEAL = 20
    GET_HUNGRY = 20
    SALARY = 50
    MIN_ACTION = 1
    MAX_ACTION = 6

    def __init__(self, name, house, satiety=50):
        self.name = name
        self.house = house
        self.satiety = satiety

    def eat(self):
        if self.house.food >= self.ONE_MEAL:
            self.house.food -= self.ONE_MEAL
            self.satiety += self.ONE_MEAL
            self.satiety = min(self.satiety, self.MAX_SATIETY)
        elif 0 > self.house.food < self.ONE_MEAL:
            self.satiety += self.house.food
            print(f'Ты съел {self.house.food} еды, это все что было...')
        else:
            print('Холодильник пуст, еда закончилась!')

    def work(self):
        self.satiety -= self.GET_HUNGRY
        self.house.money += self.SALARY

    def play(self):
        self.satiety -= self.GET_HUNGRY

    def shop_for_food(self, quantity=50):
        self.house.add_food(quantity)

    def is_alive(self):
        if self.satiety <= 0:
            # print(f'R.I.P. {self.name} из дома {self.house} умер.')
            return False
        return True

    def live_day(self):
        if self.is_alive():
            action = randint(self.MIN_ACTION, self.MAX_ACTION)
            if self.satiety < 20:
                self.eat()
            elif self.house.food <= 10:
                self.shop_for_food()
            elif self.house.money <= 50:
                self.work()
            elif action == 1:
                self.work()
            elif action == 2:
                self.eat()

    def game(self, days):
        for i in range(1, days + 1):
            if not self.is_alive():
                print(f'Человек {self} умер от голода на {i} день')
                break
            else:
                self.live_day()
        else:
            print(f'Поздравляю! Человек {self} смог прожить {days} дней')

    def __repr__(self):
        return f'{self.name} из {self.house}'


class House():
    REFRIGERATOR = 200
    COST_ONE_FOOD = 2

    def __init__(self,  name, money=0, food=50):
        self.name = name
        self.money = money
        self.food = food

    def add_food(self, quantity=50):
        if self.money >= quantity * self.COST_ONE_FOOD:
            self.food += quantity
            self.money -= quantity * self.COST_ONE_FOOD
            self.food = min(self.food, self.REFRIGERATOR)
        else:
            quantity = self.money // self.COST_ONE_FOOD
            self.money -= quantity
            self.food += quantity

    def __repr__(self):
        return f'Дом: {self.name} количество денег: {self.money}, продуктов {self.food}'


def main():
    PLAY_DAYS = 365

    home_1 = House('DarkHouse')
    player_1 = Human('Zak', home_1)
    player_2 = Human('Pol', home_1)

    player_1.game(PLAY_DAYS)
    player_2.game(PLAY_DAYS)


if __name__ == '__main__':
    main()


# # perfect solution
# import random
#
#
# class House:
#     def __init__(self, food=50, money=0):
#         self.food = food  # Количество еды в доме
#         self.money = money  # Количество денег в доме
#
#     def buy_food(self, quantity, price):
#         """Покупка еды: увеличивает количество еды и уменьшает
#         количество денег."""
#         if self.money >= price:
#             self.food += quantity
#             self.money -= price
#             print(f"Купили {quantity} единиц еды за {price} денег.")
#         else:
#             print("Недостаточно денег для покупки еды!")
#
#     def earn_money(self, salary):
#         """Заработок денег: увеличивает количество денег в доме."""
#         self.money += salary
#         print(f"Заработали {salary} денег.")
#
#
# class Human:
#     def __init__(self, name, house):
#         self.name = name  # Имя человека
#         self.hunger = 50  # Сытость человека (начальная = 50)
#         self.house = house  # Дом, в котором живет человек
#
#     def eat(self):
#         """Метод, который увеличивает сытость человека и уменьшает
#         количество еды в доме."""
#         if self.house.food >= 10:
#             self.hunger += 10
#             self.house.food -= 10
#             print(f"{self.name} поел. Сытость увеличилась до {self.hunger}, еда уменьшилась до {self.house.food}.")
#         else:
#             print(f"{self.name} хотел поесть, но в доме недостаточно еды!")
#
#     def work(self):
#         """Метод, который уменьшает сытость человека и увеличивает
#         количество денег в доме."""
#         self.hunger -= 10
#         self.house.earn_money(50)
#         print(f"{self.name} поработал. Сытость уменьшилась до {self.hunger}.")
#
#     def play(self):
#         """Метод, который уменьшает сытость человека."""
#         self.hunger -= 5
#         print(f"{self.name} поиграл. Сытость уменьшилась до {self.hunger}.")
#
#     def shop_for_food(self):
#         """Метод, который покупает еду за деньги."""
#         self.house.buy_food(15, 50)
#
#     def live_day(self):
#         """Метод, который моделирует один день жизни человека."""
#         cube = random.randint(1, 6)
#         print(f"\nСегодняшний кубик: {cube}")
#         if self.hunger < 20:
#             self.eat()
#         elif self.house.food < 10:
#             self.shop_for_food()
#         elif self.house.money < 50:
#             self.work()
#         elif cube == 1:
#             self.work()
#         elif cube == 2:
#             self.eat()
#         else:
#             self.play()
#
#         if self.hunger <= 0:
#             print(f"{self.name} умер от голода.")
#             return False
#         return True
#
#
# # Создаем объекты дома и людей
# house1 = House()
# human1 = Human("Артем", house1)
# human2 = Human("Даша", house1)
# house2 = House()
# human3 = Human("Филипп", house2)
#
# try:
#     for day in range(1, 366): # Моделируем 365 дней
#         print(f"\nДень {day}")
#         if not human1.live_day() or not human2.live_day() or not human3.live_day():
#             print(f"Человек умер на {day} день.")
#             break
# finally:
#     # Выводим конечные результаты
#     print("\nСостояние пары:")
#     print(f"Еда в холодильнике - {house1.food}, Деньги - {house1.money}")
#     print(f"Состояние {human1.name}: Сытость - {human1.hunger}")
#     print(f"Состояние {human2.name}: Сытость - {human2.hunger}\n")
#     print("Состояние одиночки:")
#     print(f"Еда в холодильнике - {house2.food}, Деньги - {house2.money}")
#     print(f"Состояние {human3.name}: Сытость - {human3.hunger}")


