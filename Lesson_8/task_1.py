# Задание №1
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json
from pathlib import Path


def convert_to_json(input_file: Path):
    data = {}
    with open(input_file, "r") as file:
        for line in file:
            name, number = line.strip().split()
            data[name.capitalize()] = float(number)

    with open(input_file.stem + '.json', "w", encoding='utf-8') as file_ex:
        json.dump(data, file_ex, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    convert_to_json(Path('result.txt'))
