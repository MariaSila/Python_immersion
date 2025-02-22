from skills import Skill


__all__ = ['Animal']


class Animal:
    _lst_animals = []

    def __init__(self, name, birthday, skills=None):
        self.name = name
        self.birthday = birthday
        self.skills = [] if skills is None else skills
        self._lst_animals.append(self)

    @classmethod
    @property
    def lst_animals(cls):
        return cls._lst_animals

    def __call__(self, *args):
        for i in args:
            self.skills.append(i)
        return self.skills

