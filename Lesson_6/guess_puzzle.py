# Задание №6
# � Добавьте в модуль с загадками функцию, которая
# принимает на вход строку (текст загадки) и число (номер
# попытки, с которой она угадана).
# � Функция формирует словарь с информацией о результатах
# отгадывания.
# � Для хранения используйте защищённый словарь уровня
# модуля.
# � Отдельно напишите функцию, которая выводит результаты
# угадывания из защищённого словаря в удобном для чтения
# виде.
# � Для формирования результатов используйте генераторное
# выражение.
__all__ = ['save', 'secrets', 'storage', 'show']

_data = {}


def save(puzzle: str, count: int) -> None:
    _data.update({puzzle: count})


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
        save(key, res)


def show():
    res = (
        f'Загадку {puzzle} угадал с {count}-й попытки' if count
        else f'Загадку {puzzle} не угадал'
        for puzzle, count in _data.items()
    )
    print(*res, sep='\n')


if __name__ == '__main__':
    storage()
    print()
    show()