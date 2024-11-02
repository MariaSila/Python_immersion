# Задача 3. Удаление старых файлов
# Напишите скрипт, который удаляет файлы в указанном каталоге, которые не
# изменялись более заданного количества дней. Скрипт должен принимать путь к
# каталогу и количество дней.
# Подсказка № 1
# Используйте time.time() для получения текущего времени в секундах с начала
# эпохи (01.01.1970). Это поможет вам определить, сколько времени прошло с
# последнего изменения файлов.
# Подсказка № 2
# Преобразуйте количество дней в секунды для сравнения. Умножьте количество дней
# на 86400 (количество секунд в одном дне), чтобы получить пороговое значение
# времени.
# Подсказка № 3
# Используйте os.walk() для рекурсивного обхода всех каталогов и файлов в
# указанном каталоге. Это позволит вам проверить каждый файл, независимо от уровня
# вложенности.
# Подсказка № 4
# Для получения времени последнего изменения файла используйте
# os.path.getmtime(). Сравните это время с пороговым значением, чтобы
# определить, нужно ли удалить файл.
# Подсказка № 5
# Для удаления файлов используйте os.remove(). Убедитесь, что файл действительно
# нужно удалить, чтобы избежать случайного удаления важных данных.

from pathlib import Path
from time import time
from os import path, walk, remove
from sys import argv

NUM_SEC_DAY = 86400


def delete_files_in_dir(path_dir: str | Path, num_days: int) -> None:
    current_time = time()
    num_sec = num_days * NUM_SEC_DAY
    print(f'{current_time=}')
    print(f'{num_days=}, {num_sec=}')
    for root, dirs, files in walk(path_dir):
        for file in files:
            file_path = path.join(root, file)
            file_create = path.getmtime(file_path)
            file_exists = current_time - file_create
            if file_exists > num_sec:
                remove(file_path)
                print(f"Удален файл '{file}' в папке '{root}'")


if __name__ == '__main__':
    delete_files_in_dir(argv[1], int(argv[2]))

# Чтобы запустить скрипт в командной строке надо ввести:
# python .\hw_7\delete_files.py 'D:\Работа\Задолженность' 100


# # perfect solution
# import os
# import time
#
#
# def delete_old_files(directory, days_old):
#     """
#     Удаляет файлы в указанном каталоге, которые не изменялись более
#     заданного количества дней.
#     :param directory: Путь к каталогу, в котором нужно удалить
#     старые файлы.
#     :param days_old: Количество дней, после которых файлы считаются
#     старыми.
#     """
#     now = time.time()  # Текущее время в секундах с начала эпохи
#     cutoff = now - (days_old * 86400)  # Преобразуем количество дней в секунды (86400 секунд в дне)
#
#     # Проходим по всем каталогам и файлам в указанном каталоге
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             file_path = os.path.join(root, file)  # Полный путь к файлу
#             file_mod_time = os.path.getmtime(file_path)  # Время последнего изменения файла
#
#             # Если время последнего изменения меньше порогового значения, удаляем файл
#             if file_mod_time < cutoff:
#                 os.remove(file_path)  # Удаляем файл
#                 print(f"Удален файл: {file_path}")
#
#
# # Пример использования функции
# delete_old_files('D:\Работа\Выписки\выписка', 30)
