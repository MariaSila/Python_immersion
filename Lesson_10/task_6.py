# Задание №6
# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс
# Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

class Animal:
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color


class Bird(Animal):
    def __init__(self, name, weight, wingspan, color):
        super().__init__(name, weight, color)
        self.wingspan = wingspan

    def get_wing_length(self):
        return self.wingspan / 2


class Fish(Animal):
    def __init__(self, name, weight, max_depth, color):
        super().__init__(name, weight, color)
        self.max_depth = max_depth

    def get_depth(self):
        if self.max_depth < 10:
            return 'Мелководная'
        elif self.max_depth > 100:
            return 'Глубоководная'
        return 'Средневодная'


class Mammal(Animal):
    def __init__(self, name, weight, height, color):
        super().__init__(name, weight, color)
        self.height = height

    def get_category(self):
        if self.height < 10:
            return 'Карликовый'
        elif self.height > 80:
            return 'Гигантский'
        return 'Средний'


if __name__ == '__main__':
    penguin = Bird('Ковальски', 20, 60, 'black')
    clown = Fish('Немо', 1, 20, 'orange')
    zebra = Mammal('Мартин', 150, 120, 'white')

    print(f' Длина крыла {penguin.name} = {penguin.get_wing_length()}')
    print(f'{clown.get_depth()=}')
    print(f'{zebra.get_category()=}')
