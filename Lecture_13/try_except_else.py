#Команда else


# --------------------------------------------------------------------
# Если надо выполнить код только в случае успешного завершения блока try, можно
# воспользоваться командой else в связке try-except-else
# В приведённом примере пользователь вводит число. Если получаем ошибку,
# сообщаем о ней пользователю. Всего даём MAX_COUNT попыток. Но стоит успешно
# преобразовать текст в целое как сработает блок else. Он сохранит результат
# деления и завершит цикл попыток.
# Если внутри блока try произойдёт одно из событий ниже, блок else не будет вызван:
# ● возбуждено исключение
# ● выполнена команда return
# ● выполнена команда break
# ● выполнена команда continue
# Именно по этой причине в нашем примере break перекочевал из try в else.
# Блок else может быть лишь один и обязан следовать за блоком except.

# MAX_COUNT = 5
# result = None
# for count in range(1, MAX_COUNT + 1):
#     try:
#         num = int(input('Введите целое число: '))
#         print('Успешно получили целое число')
#     except ValueError as e:
#         print(f'Попытка {count} из {MAX_COUNT} завершилась ошибкой {e}')
#     else:
#         result = 100 / num
#     break
#
# print(f'{result=}')


# -------------------------------------------------------------------------------------
# Вложенные блоки обработки исключений
# При необходимости одни try блоки могут включать другие. Аналогично работа.т
# вложенные циклы или вложенные if — сложные ветвления.
# Перепишем код выше так, чтобы ошибка деления на ноль обрабатывалась внутри
# блока else верхнего try.
# Если удалось получить целое число, заглядываем в else и пытаемся делить. Но если
# деление на ноль, возвращаем бесконечность вместо ошибки.

MAX_COUNT = 5
result = None
for count in range(1, MAX_COUNT + 1):
    try:
        num = int(input('Введите целое число: '))
        print('Успешно получили целое число')
    except ValueError as e:
        print(f'Попытка {count} из {MAX_COUNT} завершилась ошибкой {e}')
    else:
        try:
            result = 100 / num
        except ZeroDivisionError as e:
            result = float('inf')
            break


print(f'{result=}')