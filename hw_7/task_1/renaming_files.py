# Задание 1. Функцию группового переименования файлов.
# Напишите функцию группового переименования файлов. Она должна:
# 1. принимать параметр желаемое конечное имя файлов. При
# переименовании в конце имени добавляется порядковый номер.
# 2. принимать параметр количество цифр в порядковом номере.
# 3. принимать параметр расширение исходного файла. Переименование
# должно работать только для этих файлов внутри каталога.
# 4. принимать параметр расширение конечного файла.
# 5. принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик
# файлов и расширение. 3.Соберите из созданных на уроке и в рамках домашнего
# задания функций пакет для работы с файлами.
# Подсказка № 1
# Используйте функцию os.listdir() для получения всех файлов в указанном
# каталоге и фильтруйте их по расширению с помощью метода endswith().
# Подсказка № 2
# Для форматирования порядкового номера используйте форматную строку
# f"{{:0{num_digits}d}}", где num_digits определяет количество цифр в номере.
# Подсказка № 3
# Используйте срезы строки для извлечения нужной части базового имени файла в
# зависимости от диапазона. Помните, что индексы в Python начинаются с 0, поэтому
# корректируйте диапазон.
# Подсказка № 4
# Перед переименованием файлов убедитесь, что указанный каталог существует,
# используя функцию os.path.isdir(). Это предотвратит ошибки в случае неверного
# пути.
# Подсказка № 5
# Для переименования файлов используйте функцию os.rename(), передавая ей
# полные пути старого и нового имени файла. Убедитесь, что новые имена файлов
# формируются корректно, включая порядковый номер и расширение.

__all__ = ['renaming_files']

from os import listdir, path, rename, chdir
from pathlib import Path


def renaming_files(
        path_dir: str | Path,
        new_name: str,
        num_digits: int,
        expan_old: str,
        expan_new: str,
        range_old_name: list[int]
):
    if path.isdir(path_dir) and isinstance(path_dir, str):
        path_dir = Path(path_dir)

    chdir(path_dir)

    dir_list = listdir()
    start = range_old_name[0]
    end = range_old_name[1]
    end += 1
    counter = 1
    for obj in dir_list:
        if path.isfile(obj) and obj.endswith(expan_old):
            name = path.join(path_dir, f'{obj.split('.')[0][start:end]}{new_name}{counter:0{num_digits}d}.{expan_new}')
            rename(f'{path_dir}/{obj}', name)
            counter += 1


if __name__ == '__main__':
    renaming_files(
        Path.cwd(),
        'new',
        2,
        'txt',
        'md',
        [0, 3]
    )


# # Perfect solution
# def batch_rename_files(directory, final_name, num_digits, old_extension, new_extension, name_range):
#     if not path.isdir(directory):
#         raise FileNotFoundError(f"Каталог '{directory}' не найден.")
#
#     files = [f for f in listdir(directory) if f.endswith(old_extension)]
#
#     if not files:
#         print("Файлы с указанным расширением не найдены.")
#         return
#
#     format_string = f"{{:0{num_digits}d}}"
#
#     for index, file_name in enumerate(files, start=1):
#         # Извлекаем базовое имя файла без расширения
#         base_name = path.splitext(file_name)[0]
#         # Извлекаем часть имени файла по заданному диапазону
#         if name_range:
#             start, end = name_range
#             extracted_name = base_name[start-1:end]  # Индексы диапазона начинаются с 0
#         else:
#             extracted_name = base_name
#
#         # Формируем новое имя файла
#         new_file_name = f"{extracted_name}{final_name}{format_string.format(index)}{new_extension}"
#         # Полные пути для старого и нового файла
#
#         old_file_path = path.join(directory, file_name)
#         new_file_path = path.join(directory, new_file_name)
#
#         # Переименование файла
#         rename(old_file_path, new_file_path)
#         print(f"Переименован '{file_name}' в '{new_file_name}'")
#
#
# # Пример использования функции
# if __name__ == "__main__":
#     import sys
#     # Проверяем количество аргументов командной строки
#     if len(sys.argv) != 6:
#         print("Usage: python file_rename.py <directory> <final_name> <num_digits> <old_extension> <new_extension>")
#         sys.exit(1)
#
#     directory = sys.argv[1]
#     final_name = sys.argv[2]
#     num_digits = int(sys.argv[3])
#     old_extension = sys.argv[4]
#     new_extension = sys.argv[5]
#
#     # Например, диапазон [3, 6]
#     name_range = [3, 6]
#
#     batch_rename_files(directory, final_name, num_digits, old_extension, new_extension, name_range)
