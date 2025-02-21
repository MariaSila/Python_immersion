from typing import Callable

from final_attestation.src.registr.factory import Factory
from final_attestation.src.registr.pets import Dog, Cat, Hamster
from final_attestation.src.registr.pack_animals import Horse, Camel, Donkey
from final_attestation.src.registr.animals import Animal

if __name__ == '__main__':
    factory = Factory()
    p1 = factory.create('Cat', 'Mark', '2023-12-01')
    p2 = factory.create('Cat', 'Tony', '2022-03-22')
    p3 = factory.create('Dog', 'Lava', '2020-03-14')
    p4 = factory.create('Hamster', 'Lili', '2024-09-07')
    p5 = factory.create('Horse', 'Ralf', '2021-07-06')
    p6 = factory.create('Donkey', 'Ia', '2018-08-15')
    p7 = factory.create('Camel', 'Kop', '2019-04-13')
    p8 = factory.create('Camel', 'Solo', '2017-05-24')

    print(Animal.lst_animals)
    print(p7.lst_animals)
    print(Animal.count)
    print(p7.count)
    print(p7.skills)
