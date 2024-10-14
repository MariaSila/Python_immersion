# Задание №5
# Погружение в Python | Коллекции
# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.


#1
data = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42]
unique_list = []

for n, item in enumerate(data, 1):
    if item % 2:
        unique_list.append(n)
print(unique_list)


#2
data1 = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42]

new_list = [n for n, elem in enumerate(data1, 1) if elem % 2]
print(new_list)
