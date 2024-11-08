# Задание 1. Работа с основными данными
# Напишите функцию, которая получает на вход директорию и рекурсивно обходит
# её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и
# pickle. Для дочерних объектов указывайте родительскую директорию. Для
# каждого объекта укажите файл это или директория. Для файлов сохраните его
# размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных
# файлов и директорий. Соберите из созданных на уроке и в рамках домашнего
# задания функций пакет для работы с файлами разных форматов.
# Подсказка № 1
# Для рекурсивного обхода используйте функцию os.walk(). Эта функция генерирует
# имена файлов и директорий в указанной директории и ее поддиректориях. Внутри
# цикла можно разделять файлы и директории и собирать информацию о них.
# Подсказка № 2
# Используйте os.path.getsize() для определения размера файла. Эта функция
# возвращает размер файла в байтах. Для директорий вы можете использовать
# рекурсивный обход для вычисления общего размера всех вложенных файлов.
# Подсказка № 3
# Для сбора информации о каждом объекте создайте словарь. Словарь должен
# содержать такие ключи, как 'name', 'path', 'type', 'size', и 'parent'.
# Используйте os.path.basename() для получения имени родительской директории.
# Подсказка № 4
# Сохраняйте данные в разные форматы с помощью соответствующих библиотек.
# Используйте json.dump() для JSON, csv.DictWriter() для CSV и
# pickle.dump() для Pickle.

import json
import csv
import pickle
from pathlib import Path
from os import walk, path, listdir


def info_of_directory(path_dir: Path) -> list:
    if not path_dir.is_dir():
        print('Incorrect path')
    dict_dirs = {}
    all_data = []
    for root, dirs, files in walk(path_dir, topdown=False):
        lst = listdir(path.join(root))
        size_d = sum(path.getsize(path.join(root, name)) for name in lst)
        if dirs:
            size_d = sum(path.getsize(path.join(root, name)) for name in lst if Path(path.join(root, name)).is_file())
            for d in dirs:
                if d in dict_dirs:
                    size_d += dict_dirs[d]

        d = path.basename(root)
        dict_dirs[d] = size_d

        for name in lst:
            dict_data = {}
            k = path.join(root, name)
            dict_data['name'] = path.basename(k)
            dict_data['path'] = k
            dict_data['type'] = 'file' if Path(k).is_file() else 'directory'
            dict_data['size'] = path.getsize(k) if Path(k).is_file() else dict_dirs[path.basename(k)]
            dict_data['parent'] = path.basename(root) if Path(k).is_file() else path.basename(root)
            all_data.append(dict_data)
    return all_data


def save_to_json(input_file: Path, data: list) -> None:
    with open(input_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False, )


def save_to_csv(input_file: Path, data: list) -> None:
    keys = data[0].keys()
    with open(input_file, 'w', newline='', encoding='utf-8') as f:
        csv_write = csv.DictWriter(f, fieldnames=keys, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        csv_write.writerows(data)


def save_to_pickle(input_file: Path, data: list) -> None:
    with open(input_file, 'wb') as f:
        pickle.dump(data, f)


def main(path_dir: Path) -> None:
    data = info_of_directory(path_dir)
    save_to_json(Path('dir_info.json'), data)
    save_to_csv(Path('dir_info.csv'), data)
    save_to_pickle(Path('dir_info.pickle'), data)


if __name__ == '__main__':
    main(Path(r'/hw_7'))

