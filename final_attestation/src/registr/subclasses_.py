from typing import Callable
from exceptions import ClassNotFoundError
from animals import Animal
from pets import Dog, Cat, Hamster, Pet
from pack_animals import Horse, Camel, Donkey, PackAnimal


__all__ = ['Subclasses_']


parent = Animal


class Subclasses_():
    def get_subclass(class_name):
        classes_: dict[str, Callable[..., object]] = {}
        for key in class_name.__subclasses__():
            sub = key.__subclasses__()
            cls_: dict[str, Callable[..., object]] = {c.__name__: c for c in sub}
            classes_.update(cls_)
        return classes_

    def lst_subclasses(cls_name):
        return cls_name.__subclasses__()

    def get_dict_sub(class_name: str) -> object:
        if type(class_name) != str:
            raise ClassNotFoundError(class_name)

        classes_ = Subclasses_.get_subclass(parent)
        class_ = classes_.get(class_name, None)
        if class_ is not None:
            return class_
        raise ClassNotFoundError(class_name)
