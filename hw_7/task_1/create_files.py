# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.
__all__ = ['create_files']

from random import randint, choices
from string import ascii_lowercase, digits


def create_files(
        extension: str = 'txt',
        min_name=6,
        max_name=30,
        min_size=256,
        max_size=4096,
        num_files=2
) -> None:
    for _ in range(num_files):
        # print(ascii_lowercase)
        # print(choices(ascii_lowercase + digits + '_', k=5))
        name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name, max_name)))
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))

        with open(f'{name}.{extension}', 'wb') as file:
            file.write(data)


if __name__ == '__main__':
    create_files()
