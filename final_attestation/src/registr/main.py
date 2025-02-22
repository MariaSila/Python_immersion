from pets import Dog, Cat, Hamster
from pack_animals import Horse, Camel, Donkey
from script import found_animal, add_animal, get_skills_animal, get_lst_animal, get_count, teach_cmd

from factory import Factory
from animals import Animal

if __name__ == '__main__':
    print(add_animal('Cat', 'Mark', '2023-12-01', ['Jump', 'Speak']))
    print(add_animal('Dog', 'Lava', '2020-03-14'))
    print(get_skills_animal('Cat', 'Mark'))
    print(teach_cmd('Cat', 'Mark', 'Name', 'Walk'))
    print(get_lst_animal())
    print(get_count())
    # print(found_animal('Cat', 'Mark'))

    # factory = Factory()
    # factory.create('Cat', 'Mark', '2023-12-01', ['Jump', 'Speak'])
    # factory.create('Cat', 'Tony', '2022-03-22')
    # factory.create('Dog', 'Lava', '2020-03-14')
    # factory.create('Hamster', 'Lili', '2024-09-07')
    # factory.create('Horse', 'Ralf', '2021-07-06')
    # factory.create('Donkey', 'Ia', '2018-08-15')
    # factory.create('Camel', 'Kop', '2019-04-13')
    # factory.create('Camel', 'Solo', '2017-05-24')


    # lst_animal = Animal.lst_animals
    # for el in lst_animal:
    #     print(el.name == 'Mark')

    # lst_animal = Animal.lst_animals
    # print(len(lst_animal))
    # lst_animal.sort(key=lambda el: el.birthday, reverse=True)
    # for el in lst_animal:
    #     el('Name', 'Walk')
    #     print(f'{el.name} {el.birthday} {el.skills}')




