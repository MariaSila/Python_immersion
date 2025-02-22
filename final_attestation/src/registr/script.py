import os
import argparse
from animals import Animal
from pets import Dog, Cat, Hamster
from pack_animals import Horse, Camel, Donkey
from exceptions import ClassNotFoundError
from factory import Factory

lst_animal = []


def add_animal(class_name, *args, **kwargs):
    factory = Factory()
    animal = factory.create(class_name, *args, **kwargs)
    return animal


def get_skills_animal(class_name, name):
    animal = found_animal(class_name, name)
    return animal.skills


def teach_cmd(class_name, name, *args):
    animal = found_animal(class_name, name)
    animal(*args)
    return animal.skills


def get_lst_animal():
    # lst_animal = Animal.lst_animals.sort(key=lambda el: el.birthday, reverse=True)
    return Animal.lst_animals
    # return lst_animal.sort(key=lambda el: el.birthday, reverse=True)


def get_count():
    return len(Animal.lst_animals)
    # return len(lst_animal)


def found_animal(class_name, name):
    lst_animal = Animal.lst_animals
    flag = False
    for el in lst_animal:
        if el.__class__.__name__ == class_name:
            if el.name == name:
                flag = True
                return el
    if not flag:
        print(f'{class_name} с именем {name} не найден')


# def main():
#     parser = argparse.ArgumentParser(description="Registry animal")
#     parser.add_argument('-add', metavar='class_name, name, birthday, [see the additional function "-s"]',
#                         help='Create new animal')
#     parser.add_argument('-s', metavar='skills: list[str] in addition to function "-add"',
#                         default=None, help='Additional for create new animal', nargs='*')
#     parser.add_argument('-skills', metavar='class_name, name', type=str, help='Get list skills animal')
#     parser.add_argument('-teach', metavar='class_name, name, *skills', type=str,
#                         help='Teach animal new commands')
#     parser.add_argument('-list', metavar='No argument', help='Get list animals', default=None)
#     parser.add_argument('-count', metavar='No argument', help='Get count animals')
#     args = parser.parse_args()
#
#     if args.add is not None:
#         add_animal(args)
#     elif args.add and args.skl is not None:
#         add_animal(args)
#     elif args.skills is not None:
#         get_skills_animal(args)
#     elif args.teach is not None:
#         teach_cmd(args)
#     elif args.list is not None:
#         get_lst_animal()
#     elif args.count is not None:
#         get_count()

def main():
    while True:
        print("Выберите действие:")
        print("1. Добавить животное")
        print("2. Получить список навыков")
        print("3. Обучить новой команде")
        print("4. Просмотреть список по дате рождения")
        print("5. Количество животных в реестре")
        print("0. Выйти")

        action = input("Введите номер действия: ")
        print()

        match action:
            case '1':
                cls_name = input('Имя класса: ')
                name = input('Имя животного: ')
                birthday = input('Дата рождения: ')
                skills = input('Навыки, при наличии: ')
                print(add_animal(cls_name, name, birthday, skills))
            case '2':
                cls_name = input('Имя класса: ')
                name = input('Имя животного: ')
                print(get_skills_animal(cls_name, name))
            case '3':
                cls_name = input('Имя класса: ')
                name = input('Имя животного: ')
                skills = input('Навыки через запятую: ')
                print(teach_cmd(cls_name, name, skills))
            case '4':
                print(get_lst_animal())
            case '5':
                print(get_count())
            case '0':
                print("Завершение работы")
                break
            case _:
                print("Введены не корректные данные")


if __name__ == '__main__':
    main()
