# Задача 4. Поиск файлов по расширению
# Напишите функцию, которая находит и перечисляет все файлы с заданным
# расширением в указанном каталоге и всех его подкаталогах. Функция должна
# принимать путь к каталогу и расширение файла.
# Подсказка № 1
# Используйте os.walk() для рекурсивного обхода указанного каталога. Это позволяет
# вам обрабатывать все файлы в текущем каталоге и во всех его подкаталогах.
# Подсказка № 2
# Используйте метод str.endswith() для проверки, имеет ли имя файла указанное
# расширение. Это поможет вам отфильтровать файлы по заданному типу.
# Подсказка № 3
# Используйте os.path.join() для объединения пути к каталогу и имени файла,
# чтобы получить полный путь к файлу. Это поможет корректно обрабатывать файлы в
# разных каталогах

from pathlib import Path
from os import path, chdir, walk
from sys import argv


def find_files_with_extension(src_dir: str | Path, extension: str) -> None:
    if path.isdir(src_dir) and isinstance(src_dir, str):
        src_dir = Path(src_dir)

    chdir(src_dir)

    for root, dirs, files in walk(src_dir):
        for file in files:
            if file.endswith(extension):
                file_path = path.join(root, file)
                print(file_path)


if __name__ == '__main__':
    find_files_with_extension(argv[1], argv[2])

# Чтобы запустить скрипт в командной строке надо ввести:
# python .\hw_7\find_files.py 'C:\Users\user\Python_immersion\Lesson_7' 'txt'


# # perfect solution
# import os
#
#
# def find_files_by_extension(directory, extension):
#     """
#     Находит и перечисляет все файлы с заданным расширением в
#     указанном каталоге и всех его подкаталогах.
#     :param directory: Путь к каталогу, в котором нужно искать файлы.
#     :param extension: Расширение файлов для поиска (например,
#     '.txt').
#     """
#     # Проходим по всем каталогам и файлам в указанном каталоге
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             # Проверяем, заканчивается ли имя файла на заданное расширение
#             if file.endswith(extension):
#                 # Формируем полный путь к файлу и выводим его
#                 print(os.path.join(root, file))
#
#
# # Пример использования функции
# find_files_by_extension(r'C:\Users\user\Python_immersion\Lesson_7', '.txt')
