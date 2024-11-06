# Задание №7
# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку.

import csv
import pickle
from pathlib import Path


def csv_to_pickle(file_name: Path) -> None:
    pickle_list = []
    with open(file_name, 'r', newline='', encoding="utf-8") as f_p:
        reader = csv.reader(f_p, dialect='excel-tab')
        for i, row in enumerate(reader):
            if i == 0:
                keys = row
            else:
                pickle_dict = dict(zip(keys, row))
                pickle_list.append(pickle_dict)
    print(pickle.dumps(pickle_list))


if __name__ == '__main__':
    csv_to_pickle(Path('users2.csv'))
