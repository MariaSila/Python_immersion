from animals import Animal
from exceptions import ClassNotFoundError
from subclasses_ import get_subclass
from pets import Dog, Cat, Hamster
from pack_animals import Horse, Camel, Donkey

__all__ = ['Factory', 'get']


parent = Animal


class Factory:
    def create(self, type_animal, *args, **kwargs):
        creator = get(type_animal)
        return creator(*args, **kwargs)


def get(class_name: str) -> object:
    if type(class_name) != str:
        raise ClassNotFoundError(class_name)

    classes_ = get_subclass(parent)
    class_ = classes_.get(class_name, None)
    if class_ is not None:
        return class_

    raise ClassNotFoundError(class_name)
