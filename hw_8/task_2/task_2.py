# Задача 2. Объединение данных из нескольких JSON файлов
# Напишите скрипт, который объединяет данные из нескольких JSON файлов в
# один. Каждый файл содержит список словарей, описывающих сотрудников
# компании (имя, фамилия, возраст, должность). Итоговый JSON файл должен
# содержать объединённые списки сотрудников из всех файлов.
# Пример: У вас есть три файла employees1.json, employees2.json,
# employees3.json. Нужно объединить их в один файл all_employees.json.
# Подсказка № 1
# Используйте функцию glob.glob() для поиска всех JSON файлов в указанной
# директории.
# Подсказка № 2
# Откройте каждый JSON файл с помощью json.load() и добавьте данные в общий
# список. Функция json.load() позволяет прочитать содержимое JSON файла и
# преобразовать его в Python объект. Используйте list.extend() для объединения
# данных.
# Подсказка № 3
# Сохраните объединенные данные в новый JSON файл с помощью json.dump(). После
# объединения данных, используйте json.dump() для записи списка в новый JSON
# файл.

import json
import glob
from pathlib import Path
from os import path


def update_json(path_dir: str, find_files: str, input_file: str) -> None:
    lst = glob.glob('employees*.json')
    all_data = []
    for file_path in lst:
        with open(file_path, 'r', encoding='utf-8') as f_read:
            json_file = json.load(f_read)
            all_data.extend(json_file)
    with open(input_file, 'w', encoding='utf-8') as f_write:
        json.dump(all_data, f_write, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    update_json(r'C:\Users\user\Python_immersion',
                'employees',
                'all_employees.json')


# # perfect solution
# def merge_json_files(input_files, output_file):
#     """Объединяет данные из нескольких JSON файлов в один."""
#     merged_data = []
#     for file in input_files:
#         try:
#             with open(file, 'r') as f:
#                 data = json.load(f)
#                 merged_data.extend(data)
#         except json.JSONDecodeError:
#             print(f"Ошибка чтения JSON файла: {file}")
#     with open(output_file, 'w') as f:
#         json.dump(merged_data, f, indent=4)
#
#
# if __name__ == "__main__":
#     json_files = glob.glob('employees*.json')
#     merge_json_files(json_files, 'all_employees.json')
