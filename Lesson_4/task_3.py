# Задание №3
# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

def create_dict(string: str) -> dict[str, int]:
    num1, num2 = map(int, string.split())
    result = {}
    for num in range(min(num1, num2), max(num1, num2) + 1):
        result[chr(num)] = num
    return result


print(create_dict('100 105'))
