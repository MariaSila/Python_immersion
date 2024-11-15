# Задача 4. Создание класса-фабрики для животных
# Создайте базовый класс Animal, который имеет атрибут name, представляющий имя
# животного.
# Создайте классы Bird, Fish и Mammal, которые наследуются от базового класса Animal и
# добавляют дополнительные атрибуты и методы:
# Bird имеет атрибут wingspan (размах крыльев) и метод wing_length, который
# возвращает длину крыла птицы.
# Fish имеет атрибут max_depth (максимальная глубина обитания) и метод depth, который
# возвращает категорию глубины рыбы (мелководная, средневодная, глубоководная) в
# зависимости от значения max_depth.
# Если максимальная глубина обитания рыбы (max_depth) меньше 10, то она относится к
# категории "Мелководная рыба".
# Если максимальная глубина обитания рыбы больше 100, то она относится к категории
# "Глубоководная рыба".
# В противном случае, рыба относится к категории "Средневодная рыба".
# Mammal имеет атрибут weight (вес) и метод category, который возвращает категорию
# млекопитающего (Малявка, Обычный, Гигант) в зависимости от веса. Если вес объекта
# меньше 1, то он относится к категории "Малявка".
# Если вес объекта больше 200, то он относится к категории "Гигант".
# В противном случае, объект относится к категории "Обычный".
# Создайте класс-фабрику AnimalFactory, который будет создавать экземпляры животных
# разных типов на основе переданного типа и параметров. Класс-фабрика должен иметь
# метод create_animal, который принимает следующие аргументы:
# animal_type (строка) - тип животного (один из: 'Bird', 'Fish', 'Mammal').
# *args - переменное количество аргументов, представляющих параметры для конкретного
# типа животного. Количество и типы аргументов могут различаться в зависимости от типа
# животного.
# Метод create_animal должен создавать и возвращать экземпляр животного заданного
# типа с переданными параметрами.
# Если animal_type не соответствует 'Bird', 'Fish' или 'Mammal', функция вызовет ValueError с
# сообщением 'Недопустимый тип животного'.
# Подсказка № 1
# Начните с создания базового класса Animal, который содержит атрибут name. Этот
# класс будет родительским для других классов животных. Атрибут name будет
# передаваться через конструктор __init__.
# Подсказка № 2
# Создайте классы-наследники Bird, Fish и Mammal. Каждый из этих классов должен
# наследоваться от класса Animal и добавлять свои уникальные атрибуты. Например, у
# Bird будет атрибут wingspan, у Fish — max_depth, а у Mammal — weight.
# Подсказка № 3
# В классе Bird создайте метод wing_length, который будет возвращать длину крыла.
# Допустим, длина крыла равна половине размаха крыльев (wingspan).
# Подсказка № 4
# В классе Fish создайте метод depth, который будет возвращать категорию глубины
# на основе значения max_depth. Используйте условные конструкции if для проверки
# диапазонов глубин.

class Animal:
    def __init__(self, name):
        self.name = name


class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def get_wing_length(self):
        return self.wingspan / 2

    def __repr__(self):
        return f'Птица {self.name}, размах крыла: {self.wingspan}'


class Fish(Animal):
    def __init__(self, name, max_depth):
        super().__init__(name)
        self.max_depth = max_depth

    def get_depth(self):
        if self.max_depth < 10:
            return 'Мелководная'
        elif self.max_depth > 100:
            return 'Глубоководная'
        return 'Средневодная'

    def __repr__(self):
        return f'Рыба {self.name}, максимальная глубина {self.max_depth}'


class Mammal(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def get_category(self):
        if self.weight < 1:
            return 'Малявка'
        elif self.weight > 80:
            return 'Гигант'
        return 'Обычный'

    def __repr__(self):
        return f'Млекопитающий {self.name}, вес: {self.weight}'


class AnimalFactory():
    @staticmethod
    def create_animal(animal_type, *args):
        try:
            if animal_type.lower() == 'bird':
                return Bird(*args)
            elif animal_type.lower() == 'fish':
                return Fish(*args)
            elif animal_type.lower() == 'mammal':
                return Mammal(*args)
            else:
                raise ValueError
        except ValueError:
            print(f'Недопустимый тип животного {animal_type}')


if __name__ == '__main__':
    dori = AnimalFactory.create_animal('Fish', 'Dori', 10)
    marty = AnimalFactory.create_animal('Mammal', 'Martyn', 150)
    coco = AnimalFactory.create_animal('Bird','Coco', 9)
    print(dori)
    print(marty)
    print(coco)


# # PERFECT SOLUTION
# class Animal:
#     def __init__(self, name: str):
#         self.name = name
#
#     def speak(self):
#         raise NotImplementedError("Subclasses should implement this method")
#
#     def __str__(self):
#         return f"{self.__class__.__name__} named {self.name}"
#
# class Dog(Animal):
#     def __init__(self, name: str, breed: str):
#         super().__init__(name)
#         self.breed = breed
#
#     def speak(self):
#         return "Woof!"
#
#     def __str__(self):
#         return f"{super().__str__()} of breed {self.breed}"
#
#
# class Cat(Animal):
#     def __init__(self, name: str, color: str):
#         super().__init__(name)
#         self.color = color
#
#     def speak(self):
#         return "Meow!"
#
#     def __str__(self):
#         return f"{super().__str__()} with color {self.color}"
#
#
# class AnimalFactory:
#     @staticmethod
#     def create_animal(animal_type: str, *args) -> Animal:
#         """ Создает экземпляр животного на основе переданного типа и
#         параметров.
#         :param animal_type: Название типа животного (например, 'Dog'
#         или 'Cat')
#         :param args: Параметры для конструктора животного
#         :return: Экземпляр соответствующего класса животного
#         """
#         animal_classes = {'Dog': Dog, 'Cat': Cat}
#         if animal_type in animal_classes:
#             return animal_classes[animal_type](*args)
#         else:
#             raise ValueError(f"Unknown animal type: {animal_type}")
#
#
# # Создаем экземпляры животных с использованием фабрики
# dog = AnimalFactory.create_animal('Dog', 'Buddy', 'Golden Retriever')
# cat = AnimalFactory.create_animal('Cat', 'Whiskers', 'Black')
#
# print(dog)  # Вывод: Dog named Buddy of breed Golden Retriever
# print(cat)  # Вывод: Cat named Whiskers with color Black
# print(dog.speak())  # Вывод: Woof!
# print(cat.speak())  # Вывод: Meow!