# Задание №8
# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.
# Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********

SPACE = ' '
STAR = '*'

rows = int(input('Сколько рядов у елки: '))
spaces = rows - 1
stars = 1

for _ in range(rows):
    print((spaces * SPACE) + (stars * STAR))
    spaces -= 1
    stars += 2


