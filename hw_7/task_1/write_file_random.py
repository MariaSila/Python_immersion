# Задание №1
# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.
__all__ = ['write_random_to_file']

import random
from pathlib import Path

MIN_LIMIT = -1000
MAX_LIMIT = 1000


def write_random_to_file(num_pairs: int, file_name: str | Path) -> None:
    with open(file_name, 'a', encoding='UTF-8') as file:
        for _ in range(num_pairs):
            int_num = random.randint(MIN_LIMIT, MAX_LIMIT)
            float_num = random.uniform(MIN_LIMIT, MAX_LIMIT)
            file.write(f'{int_num:>4}|{float_num}\n')


if __name__ == '__main__':
    write_random_to_file(10, 'random_num.txt')
