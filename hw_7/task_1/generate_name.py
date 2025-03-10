# Задание №2
# # ✔ Напишите функцию, которая генерирует
# # псевдоимена.
# # ✔ Имя должно начинаться с заглавной буквы,
# # состоять из 4-7 букв, среди которых
# # обязательно должны быть гласные.
# # ✔ Полученные имена сохраните в файл.
__all__ = ['generate_name']

from random import choice, randint
from pathlib import Path

VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'
MIN_LEN = 4
MAX_LEN = 7


def generate_name(count: int, file_name: str | Path) -> None:
    for _ in range(count):
        first_chr = choice([-1, 1])
        name = ''
        for _ in range(randint(MIN_LEN, MAX_LEN)):
            if first_chr == -1:
                name += choice(CONSONANTS)
            else:
                name += choice(VOWELS)
            first_chr *= -1

        with open(file_name, 'a', encoding='UTF-8') as f:
            f.write(name.title() + '\n')


if __name__ == '__main__':
    generate_name(10, Path('names.txt'))


# # второй способ через генератор
# def generate_name_2(count: int, file_name: str | Path) -> None:
#     for _ in range(count):
#         name = ''.join(choice(VOWELS) if i in (1, 4, 6) else choice(CONSONANTS)
#                        for i in range(randint(MIN_LEN, MAX_LEN)))
#
#         with open(file_name, 'a', encoding='UTF-8') as f:
#             f.write(name.title() + '\n')
