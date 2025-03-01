from subclasses_ import Subclasses_
from animals import Animal
from pets import Dog, Cat, Hamster
from pack_animals import Horse, Camel, Donkey

__all__ = ['Factory']


class Factory:
    def create(self, type_animal, *args, **kwargs):
        creator = Subclasses_.get_dict_sub(type_animal)
        return creator(*args, **kwargs)
