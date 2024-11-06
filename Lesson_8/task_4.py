# Задание №4
# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.

import csv
import json
from pathlib import Path


def csv_to_json(input_file: Path, output_file: Path) -> None:
    data = []
    with open(input_file, 'r', newline='', encoding='utf-8') as file:
        csv_read = csv.reader(file, dialect='excel-tab')
        for i, line in enumerate(csv_read):
            json_dict = {}
            if i:
                level, user_id, name = line
                json_dict['level'] = int(level)
                json_dict['user_id'] = f'{int(user_id):010}'
                json_dict['name'] = name.title()
                json_dict['has'] = hash(f'{json_dict['name']}{json_dict['user_id']}')
                data.append(json_dict)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


csv_to_json(Path('users.csv'), Path('users2.json'))

