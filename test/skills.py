# from pets import Dog, Cat, Hamster
# from pack_animals import Horse, Camel, Donkey
# from animals import Animal


__all__ = ['Skill']


class Skill:
    dict_skills = {'pets': ['Name', 'Walk', 'Paw', 'Sit', 'Stand', 'Jump', 'Speak', 'Heel',
                            'Down', 'Come', 'Fetch', 'Go', 'No', 'Hunt', 'Place', 'Hide'],
                   'pack_animals': ['Name', 'Trot', 'Gallop', 'Walk', 'Calm', 'Turn', 'Stop', 'Jamp']}

    def __init__(self, skills=None):
        self.skills = [] if skills is None else skills

    def __str__(self):
        return f'skills: {self.skills}'

    def __repr__(self):
        return f'{__class__.__name__}:{self.skills}'
