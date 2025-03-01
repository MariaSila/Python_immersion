from typing import Callable
from animals import Animal
from pets import Dog, Cat, Hamster, Pet
from pack_animals import Horse, Camel, Donkey, PackAnimal


__all__ = ['get_subclass', 'lst_subclasses']


def get_subclass(class_name):
    classes_: dict[str, Callable[..., object]] = {}
    for key in class_name.__subclasses__():
        sub = key.__subclasses__()
        cls_: dict[str, Callable[..., object]] = {c.__name__: c for c in sub}
        classes_.update(cls_)
    return classes_


def lst_subclasses(cls_name):
    return cls_name.__subclasses__()
