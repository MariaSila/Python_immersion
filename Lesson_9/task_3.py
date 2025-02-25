# Задание №3
# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.

import json
from typing import Callable
from pathlib import Path


def save_to_json(func: Callable):
    file = Path(f'{func.__name__}.json')
    if file.is_file():
        with open (file, 'r', encoding='utf-8') as f_r:
            list_of_dicts = json.load(f_r)
    else:
        list_of_dicts = []

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        json_dict = {'args': args, **kwargs, 'result': result}
        list_of_dicts.append(json_dict)
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(list_of_dicts, f, indent=4, ensure_ascii=False)
        return result

    return wrapper


@save_to_json
def get_all(num1: int, *args, **kwargs):
    return num1


if __name__ == '__main__':
    get_all(5, 2, 3, 'str', 85, x=5, y=8)
