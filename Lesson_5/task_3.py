# Задание №3
# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

COUNT = 5
str_1 = 'Создайте из строки словарь, где ключ — буква, а значение — код буквы.'
dict_1 = {char: ord(char) for char in str_1}
print(f'{dict_1 = }')
dict_iter = iter(dict_1.items())
for _ in range(COUNT):
    print(*next(dict_iter))
