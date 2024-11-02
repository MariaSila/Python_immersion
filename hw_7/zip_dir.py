# Задача 2. Создание архива каталога
# Напишите скрипт, который создает архив каталога в формате .zip. Скрипт
# должен принимать путь к исходному каталогу и путь к целевому архиву. Архив
# должен включать все файлы и подпапки исходного каталога.
# Подсказка № 1
# Используйте функцию os.walk() для обхода всех файлов и подпапок в исходном
# каталоге. Это функция возвращает корневую папку, список директорий и список
# файлов в каждом корневом каталоге.
# Подсказка № 2
# Для создания архива используйте zipfile.ZipFile() с режимом 'w' для записи.
# Также передайте параметр zipfile.ZIP_DEFLATED, чтобы применить сжатие к
# файлам в архиве.
# Подсказка № 3
# Чтобы сохранить структуру каталогов в архиве, используйте функцию
# os.path.relpath(), чтобы добавить файлы в архив с путями относительно
# исходного каталога.
# Подсказка № 4
# Для получения полного пути к файлу используйте os.path.join(root, file), где
# root - это текущая корневая папка, а file - это имя файла.
# Подсказка № 5
# Перед созданием архива убедитесь, что исходный каталог существует, чтобы избежать
# ошибок. Используйте os.path.isdir() для проверки существования каталога

from pathlib import Path
from os import walk, path
from sys import argv
from zipfile import ZipFile, ZIP_DEFLATED


def zip_dir(src_dir: str | Path, dest_dir: str | Path) -> None:
    source = Path(src_dir)
    if not Path.is_dir(source):
        print(f"Каталог '{source}' не найден.")

    with ZipFile(dest_dir, 'w', ZIP_DEFLATED) as arch:
        for dir_path, dir_name, file_name in walk(src_dir):
            for file in file_name:
                file_path = path.join(dir_path, file)
                arch.write(file_path, path.relpath(file_path, src_dir))


if __name__ == '__main__':
    zip_dir(argv[1], argv[2])

    # Просмотр содержимого архива
    with ZipFile(r'C:\Users\user\Python_immersion\arch.zip', mode="r") as archive:
        archive.printdir()

# Чтобы запустить скрипт в командной строке надо ввести:
# python .\hw_7\zip_dir.py 'C:\Users\user\Python_immersion\Lesson_7' 'C:\Users\user\Python_immersion\arch.zip'


# # perfect solution
# import os
# import zipfile
# def zip_directory(source_dir, output_zip):
#     """
#     Создает архив .zip из указанного каталога.
#     :param source_dir: Путь к исходному каталогу для архивирования.
#     :param output_zip: Путь к целевому архиву .zip.
#     """
#     # Создаем объект ZipFile для записи архива
#     with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
#         # Проходим по всем файлам и папкам в исходном каталоге
#         for root, dirs, files in os.walk(source_dir):
#             for file in files:
#                 # Полный путь к текущему файлу
#                 file_path = os.path.join(root, file)
#                 # Добавляем файл в архив с путем относительно исходного каталога
#                 zipf.write(file_path, os.path.relpath(file_path, source_dir))
#
#
# # Пример использования функции
# zip_directory(r'C:\Users\user\Python_immersion\Lesson_7', r'C:\Users\user\Python_immersion\arch.zip')
#
# with zipfile.ZipFile(r'C:\Users\user\Python_immersion\arch.zip', mode="r") as archive:
#     archive.printdir()
