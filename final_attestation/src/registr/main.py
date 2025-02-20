from pets import Dog, Cat, Hamster
from pack_animals import Horse, Camel, Donkey
from animals import Animal

if __name__ == '__main__':
    p1 = Cat('Mark', '2023-12-01')
    p11 = Cat('Tony', '2022-03-22')
    p2 = Dog('Lava', '2020-03-14')
    p3 = Hamster('Lili', '2024-09-07')
    p4 = Horse('Ralf', '2021-07-06')
    p5 = Donkey('Ia', '2018-08-15')
    p6 = Camel('Kop', '2019-04-13')
    p7 = Camel('Solo', '2017-05-24')

    print(Animal.lst_animals)
    print(p7.lst_animals)
    print(Animal.count)
    print(p7.skills)

