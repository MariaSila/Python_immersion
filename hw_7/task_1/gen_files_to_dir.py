# Задание №6
# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
__all__ = ['create_files', 'gen_files']

from random import randint, choices
from string import ascii_lowercase, digits
from pathlib import Path
from os import chdir


def create_files(
        extension: str='bin',
        min_name=6,
        max_name=30,
        min_size=256,
        max_size=4096,
        num_files=2
    ) -> None:
    for _ in range(num_files):
        while True:
            name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name, max_name)))
            name = f'{name}.{extension}'
            if not Path(name).is_file():
                break
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(name, 'wb') as file:
            file.write(data)


def gen_files(path: str | Path,**kwargs) -> None:
    if isinstance(path, str):
        path = Path(path)
    if not path.is_dir():
        path.mkdir(parents=True)
    chdir(path)

    for ext, count in kwargs.items():
        create_files(extension=ext, num_files=count)


if __name__ == '__main__':
    gen_files(r'C:\Users\user\Python_immersion\Lesson_7\NEW', jpg=3, mp4=2, mkv=1)