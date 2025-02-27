from datetime import datetime
from exceptions import DataError, NameError

__all__ = ['Animal']


class Animal:
    _lst_animals = []
    _id_counter = 1

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.id = cls._id_counter
        Animal._id_counter += 1
        return instance

    def __init__(self, name, birthday, skills=None):
        self.__setattr__('name', name)
        self.__setattr__('birthday', birthday)
        self.skills = [] if skills is None else [*skills]
        self._lst_animals.append(self)

    def __setattr__(self, name, value):
        if name == 'name':
            if not (value and value[0].isupper() and value.replace(" ", "").isalpha()):
                raise NameError
        if name == 'birthday':
            try:
                datetime.fromisoformat(value)
            except ValueError:
                raise DataError
        super().__setattr__(name, value)

    @classmethod
    @property
    def lst_animals(cls):
        return cls._lst_animals

    def __call__(self, *args):
        for i in args:
            self.skills.append(i)
        return self.skills

    def __str__(self):
        return f'id:{self.id}, {self.__class__.__name__}: {self.name}, birthday:{self.birthday}, skills: {self.skills}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.birthday})'
