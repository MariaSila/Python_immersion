# Задание №5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.


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
        name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name, max_name)))
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))

        with open(f'{name}.{extension}', 'wb') as file:
            file.write(data)


def gen_files(**kwargs) -> None:
    for ext, count in kwargs.items():
        create_files(extension=ext, num_files=count)


if __name__ == '__main__':
    gen_files(jpg=3, mp4=2, mkv=1)
