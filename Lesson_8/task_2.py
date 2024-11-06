# Задание №2
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключем для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.

import json
from pathlib import Path


def set_users(user_file: Path) -> None:
    unique_id = set()
    if not user_file.is_file():
        data = {str(i): {} for i in range(1, 7 + 1)}
    else:
        with open(user_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for dict_level in data.values():
                unique_id.update(dict_level)

    while True:
        name = input('Enter name: ')
        if not name:
            break
        user_id = input('Enter id: ')
        level = input('Enter level from 1 to 7: ')
        while level not in ('1', '2', '3', '4', '5', '6', '7'):
            print('Incorrect input')
            level = input('Enter level from 1 to 7: ')
        if user_id not in unique_id:
            data[level].update({user_id: name})
            # data[level][user_id: name] = name  # второй вариант
            unique_id.add(user_id)
            with open(user_file, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':

    set_users(Path('users.json'))
