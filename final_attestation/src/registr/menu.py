from animals import Animal
from pets import Dog, Cat, Hamster
from pack_animals import Horse, Camel, Donkey
from exceptions import UserException, NameNotFoundError, InputError
from factory import Factory
from subclasses_ import Subclasses_

__all__ = ['add_animal', 'get_skills_animal', 'teach_cmd', 'get_lst_animal', 'get_count', 'found_animal', 'Menu']

parent = Animal


def add_animal(cls_name, name, birthday, *args):
    factory = Factory()
    animal = factory.create(cls_name, name, birthday, *args)
    return animal


def get_skills_animal(*args):
    animal = found_animal(*args)
    return animal.skills


def teach_cmd(cls_name, name, *args):
    animal = found_animal(cls_name, name)
    animal(*args)
    return animal.skills


def get_lst_animal(data):
    return list(sorted(data, key=lambda x: x.birthday, reverse=True))


def get_count():
    return len(parent.lst_animals)


def found_animal(class_name, name):
    # lst_animal = parent.lst_animals
    flag = False
    for el in parent.lst_animals:
        if el.__class__.__name__ == class_name:
            if el.name == name:
                flag = True
                return el
    if not flag:
        raise NameNotFoundError(class_name, name)


class Menu():
    def actions_with_animal(cls, name):
        while True:
            act = input("""Выберите действие:
    1. Список навыков
    2. Обучить новой команде
    3. Все данные животного
    0. Выход
    """)
            match act:
                case '1':
                    skl = get_skills_animal(cls, name)
                    if skl:
                        print(f'{cls} {name} знает команды: {skl}')
                    else:
                        print(f'{cls} {name} еще не обучен командам')
                case '2':
                    new_skl = input('Навыки через пробел: ').split()
                    skl = teach_cmd(cls, name, *new_skl)
                    print(f'{cls} {name} знает команды: {skl}')
                case '3':
                    animal = found_animal(cls, name)
                    print(animal)
                case '0':
                    break
                case _:
                    print("Введены не корректные данные")

    def select_subclass(parent):
        cls_ = Subclasses_.lst_subclasses(parent)
        lst = [i.__name__ for i in cls_]
        print('Доступные виды: ')
        for i, el in enumerate(lst):
            print(f'{i + 1}. {el}')
        answer = int(input('Введите номер вида: '))
        if len(lst) < answer < len(lst):
            raise InputError(len(lst))
        return cls_[answer - 1]

    while True:
        action = input("""Выберите действие:
1. Добавить животное
2. Выбрать животное
3. Просмотреть список по дате рождения
4. Количество животных
0. Выход
""")
        match action:
            case '1':
                sub = select_subclass(parent)
                cls_name = select_subclass(sub).__name__
                name = input('Имя животного: ')
                birthday = input('Дата рождения в формате гггг-мм-дд: ')
                skills = list(input('Навыки при наличии через пробел: ').split())
                animal = add_animal(cls_name, name, birthday, skills)
                print(animal)
            case '2':
                cls_name = input('Вид: ')
                name = input('Имя: ')
                actions_with_animal(cls_name, name)
            case '3':
                print(get_lst_animal(parent.lst_animals))
            case '4':
                count = get_count()
                print(f'Количество животных в реестре: {count}')
            case '0':
                print("Завершение работы")
                break
            case _:
                print("Введены не корректные данные")


if __name__ == '__main__':
    try:
        Menu()
    except UserException as e:
        print(e)
