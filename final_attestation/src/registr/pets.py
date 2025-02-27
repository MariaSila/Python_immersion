from animals import Animal

__all__ = ['Pet', 'Cat', 'Dog', 'Hamster']


class Pet(Animal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Cat(Pet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Dog(Pet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Hamster(Pet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
