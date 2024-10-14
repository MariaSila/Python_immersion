# Задание №4
# Погружение в Python | Коллекции
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды


# 1
data = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42]

result_1 = [item for item in data if data.count(item) != 2]
print(f'{result_1=}')


# 2
result_2 = []

for item in data:
    if data.count(item) != 2:
        result_2.append(item)
print(f'{result_2=}')

# 3
data2 = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42]
COUNT = 2

for item in set(data2):
    if data2.count(item) == COUNT:
        for _ in range(COUNT):
            data2.remove(item)
print(f'{data2=}')
