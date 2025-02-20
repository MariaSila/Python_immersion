from skills import Skills

__all__ = ['Animal']


class Animal():
    _count = 0
    _lst_animals = []

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self.skills = Skills()
        self._lst_animals.append(self)
        Animal._count += 1

    @classmethod
    @property
    def count(cls):
        return f'Total animals: {cls._count}'

    @classmethod
    @property
    def lst_animals(cls):
        return f'List animals: {cls._lst_animals}'

