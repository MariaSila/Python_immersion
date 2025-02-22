from typing import Callable
from animals import Animal
from exceptions import ClassNotFoundError

__all__ = ['get_subclass']


parent = Animal


class Factory:
    def create(self, type_animal, *args, **kwargs):
        creator = get(type_animal)
        return creator(*args, **kwargs)


def get_subclass(class_name):
    classes_: dict[str, Callable[..., object]] = {}
    for key in class_name.__subclasses__():
        sub = key.__subclasses__()
        cls_: dict[str, Callable[..., object]] = {c.__name__: c for c in sub}
        classes_.update(cls_)
    return classes_


def get(class_name: str) -> object:
    if type(class_name) != str:
        raise ValueError("class_name must be a string!")

    classes_ = get_subclass(parent)
    class_ = classes_.get(class_name, None)
    if class_ is not None:
        return class_

    raise ClassNotFoundError



# первый вариант (без пород)
# classes: dict[str, Callable[..., object]] = {}
# for key in Animal.__subclasses__():
#     sub = key.__subclasses__()
#     cls: dict[str, Callable[..., object]] = {c.__name__: c for c in sub}
#     classes.update(cls)
# print(classes)
#{'Cat': <class 'pets.Cat'>, 'Dog': <class 'pets.Dog'>, 'Hamster': <class 'pets.Hamster'>,
#'Horse': <class 'pack_animals.Horse'>, 'Donkey': <class 'pack_animals.Donkey'>,
#'Camel': <class 'pack_animals.Camel'>}


# # второй вариант (без пород)
# def get_subclass(class_name):
#     classes_: dict[str, Callable[..., object]] = {}
#     for key in class_name.__subclasses__():
#         sub = key.__subclasses__()
#         cls_: dict[str, Callable[..., object]] = {c.__name__: c for c in sub}
#         classes_.update(cls_)
#     return classes_
#
# classes = get_subclass(Animal)
# print(classes)
#
# # {'Cat': <class 'pets.Cat'>, 'Dog': <class 'pets.Dog'>, 'Hamster': <class 'pets.Hamster'>,
# # 'Horse': <class 'pack_animals.Horse'>, 'Donkey': <class 'pack_animals.Donkey'>,
# # 'Camel': <class 'pack_animals.Camel'>}


# # третий вариант (с пародами)
# def get_sub(lst):
#     cls_: dict[str, Callable[..., object]] = {}
#     for name in lst:
#         sub = name.__subclasses__()
#         cls_.update({c.__name__: c for c in sub})
#     return cls_
#
# def get_subclass(class_name):
#     classes_: dict[str, Callable[..., object]] = {}
#     classes_.update(get_sub(class_name.__subclasses__()))
#     classes_.update(get_sub(classes_.values()))
#     return classes_
#
# classes = get_subclass(Animal)
# print(classes)
#
# # {'Cat': <class 'pets.Cat'>, 'Dog': <class 'pets.Dog'>, 'Hamster': <class 'pets.Hamster'>,
# # 'Horse': <class 'pack_animals.Horse'>, 'Donkey': <class 'pack_animals.Donkey'>,
# # 'Camel': <class 'pack_animals.Camel'>, 'Bulldog': <class 'pets.Bulldog'>}


# # четвертый вариант (с пародами)
# def get_subclass(class_name):
#     classes_: dict[str, Callable[..., object]] = {}
#     for sub_one in class_name.__subclasses__():
#         sub = sub_one.__subclasses__()
#         cls_: dict[str, Callable[..., object]] = {c.__name__: c for c in sub}
#         classes_.update(cls_)
#         for sub_two in sub:
#             sub = sub_two.__subclasses__()
#             cls_: dict[str, Callable[..., object]] = {c.__name__: c for c in sub}
#             classes_.update(cls_)
#     return classes_
#
# classes = get_subclass(Animal)
# print(classes)
#
# {'Cat': <class 'pets.Cat'>, 'Dog': <class 'pets.Dog'>, 'Hamster': <class 'pets.Hamster'>,
# 'Bulldog': <class 'pets.Bulldog'>, 'Horse': <class 'pack_animals.Horse'>,
# 'Donkey': <class 'pack_animals.Donkey'>, 'Camel': <class 'pack_animals.Camel'>}
