from animals import Animal

__all__ = ['PackAnimal', 'Horse', 'Donkey', 'Camel']


class PackAnimal(Animal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Horse(PackAnimal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'{__class__.__name__}({self.name})'

    def __str__(self):
        return f'{__class__.__name__}: {self.name}, birthday:{self.birthday}, {self.skills}'


class Donkey(PackAnimal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'{__class__.__name__}({self.name})'

    def __str__(self):
        return f'{__class__.__name__}: {self.name}, birthday:{self.birthday}, {self.skills}'


class Camel(PackAnimal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'{__class__.__name__}({self.name})'

    def __str__(self):
        return f'{__class__.__name__}: {self.name}, birthday:{self.birthday}, {self.skills}'
