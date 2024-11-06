# Задание №6
# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.

import pickle
import csv
from pathlib import Path


def pickle_to_csv(path: Path) -> None:
    with (
        open(path, 'rb') as f_r,
        open(f'{path.stem}.csv', 'w', newline='', encoding='utf-8') as f_w
    ):
        data = pickle.load(f_r)
        keys = data[0].keys()
        csv_writer = csv.DictWriter(f_w, fieldnames=keys, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writeheader()
        csv_writer.writerows(data)


if __name__ == '__main__':
    pickle_to_csv(Path('users2.pickle'))
