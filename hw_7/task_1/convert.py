# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.
__all__ = ['read_or_begin', 'convert']

from typing import TextIO


def read_or_begin(fd: TextIO) -> str:
    text = fd.readline()
    if text == "":
        fd.seek(0)
        text = fd.readline()
    return text.strip()


def convert(numbers: str, names: str, result: str) -> None:
    with (
        open(numbers, 'r', encoding='utf-8') as f_number,
        open(names, 'r', encoding='utf-8') as f_name,
        open(result, 'w', encoding='utf-8') as f_result
    ):
        len_names = sum(1 for _ in f_name)
        len_numbers = sum(1 for _ in f_number)
        for _ in range(max(len_names, len_numbers)):
            nums_str = read_or_begin(f_number)
            name = read_or_begin(f_name)
            num_i, num_f = nums_str.split("|")
            mult = int(num_i) * float(num_f)
            if mult < 0:
                f_result.write(f'{name.lower()} {-mult} \n')
            else:
                f_result.write(f'{name.upper()} {int(mult)} \n')


if __name__ == '__main__':
    convert('random_num.txt', 'names.txt', 'result.txt')
