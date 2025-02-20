from animals import Animal

__all__ = ['Pet', 'Cat', 'Dog', 'Hamster']


class Pet(Animal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Cat(Pet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'{__class__.__name__}({self.name})'

    def __str__(self):
        return f'{__class__.__name__}: {self.name}, birthday:{self.birthday}, {self.skills}'


class Dog(Pet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'{__class__.__name__}({self.name})'

    def __str__(self):
        return f'{__class__.__name__}: {self.name}, birthday:{self.birthday}, {self.skills}'


class Hamster(Pet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'{__class__.__name__}({self.name})'

    def __str__(self):
        return f'{__class__.__name__}: {self.name}, birthday:{self.birthday}, {self.skills}'
