# Задание №8
# Погружение в Python | Коллекции
# ✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться
# на любое большее количество друзей.


#1
hike = {
'Aaz': ("спички", "спальник", "дрова", "топор"),
'Skeeve': ("спальник", "спички", "вода", "еда"),
'Tananda': ("вода", "спички", "косметичка"),
}

all_things = set()
# all_things.update(*hike.values())
for values in hike.values():
    all_things.update(values)
print(f'Полный список вещей: {all_things = }')

unique = {}
for master_friend, master_things in hike.items():
    for slave_friend, slave_things in hike.items():
        if master_friend != slave_friend:
            if master_friend not in unique:
                unique[master_friend] = set(master_things) - set(slave_things)
            else:
                unique[master_friend] -= set(slave_things)

print(f'Уникальные вещи: {unique = }')


dublicates = set(all_things)

# uniq_things = set()
# uniq_things.update(*unique.values())
# print(uniq_things)
# dublicates -= uniq_things
# print(dublicates)


for things in unique.values():
    dublicates -= things
print(f'Дублирующиеся вещи: {dublicates = }')

for friend, things in hike.items():
    no_things = dublicates - set(things)
    if no_things:
        print(f'У {friend} отсутствует {no_things}')



#2 other solution task
# data = {"Вася": ("Палатка", "Котелок", "Спички", "Шашлык"),
# "Витя": ("Палатка", "Котелок", "Топор"),
# "Петя": ("Палатка", "Котелок", "Топор", "Спирт"),
# "Саша": ("Палатка", "Спирт")}
#
# # ✔ Какие вещи взяли все три друга
# # intersection - возвращает пересечение — элементы данного множества,
# # также присутствующие в указанных объектах.
# lst = []
# for k, v in data.items():
#     lst.append(set(v))
#
# for i in range(len(lst) - 2):
#     res_all = lst[i].intersection(lst[i + 1])
#     res_all = res_all.intersection(lst[i + 2])
#
# print(f"{res_all} есть у всех")
#
# # ✔ Какие вещи уникальны, есть только у одного друга
# # difference - Возвращает разницу — из элементов данного множества удаляются
# # элементы, присутствующие в указанных объектах.
# st = set()
#
# for s in data:
#     st = set(data[s])
#     for f in data:
#         if s != f:
#             st = st.difference(set(data[f]))
#     if st:
#         print(f"Только {s} имеет {st}")
#
# # ✔ Какие вещи есть у всех друзей кроме одного
# # и имя того, у кого данная вещь отсутствует
# for s in data:
#     st = set(data[s])
#     st_f = set()
#     for f in data:
#         if s != f:
#             st_f = st_f.intersection(set(data[f])) if st_f else set(data[f])
#     if st_f:
#         delta = st_f.difference(st)
#         if delta:
#             print(f"Только {s} не имеет {delta}")