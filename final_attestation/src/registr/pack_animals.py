from animals import Animal

__all__ = ['PackAnimal', 'Horse', 'Donkey', 'Camel']


class PackAnimal(Animal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Horse(PackAnimal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Donkey(PackAnimal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Camel(PackAnimal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
