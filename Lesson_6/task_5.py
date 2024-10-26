# Задание №5
# � Добавьте в модуль с загадками функцию, которая хранит
# словарь списков.
# � Ключ словаря - загадка, значение - список с отгадками.
# � Функция в цикле вызывает загадывающую функцию, чтобы
# передать ей все свои загадки.

def secrets(puzzle: str, answers: list[str], count: int = 3) -> int:
    print(f'Отгадай загадку: {puzzle}')
    for i in range(1, count + 1):
        answer = input(f'Попытка номер {i}, Твой ответ: ').lower()
        if answer in answers:
            return i
    return 0


def storage():
    puzzles = {
        'Зимой и летом одним цветом': ['ель', 'сосна', 'елка'],
        'Висит груша - нельзя скушать': ['лампочка', 'лампа', 'люстра'],
        'Сидит дед - во сто шуб одет': ['лук', 'луковица', 'капуста']
    }
    for key, value in puzzles.items():
        res = secrets(key, value)
        print(f'Угадал с {res} попытки' if res else 'Не угадал')


if __name__ == '__main__':
    storage()
