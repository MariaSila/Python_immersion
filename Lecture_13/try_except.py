# Команда try + Команда except


# -------------------------------------------------------------------------
# Что делать, если мы не хотим завершать программу в случае появления ошибки?
# Команда try позволяет обернуть блок кода с возможной ошибкой и отловить её.
# 🔥 Важно! Блок кода внутри try в идеале должен состоять из одной строки
# кода — потенциального источника ошибки. Оборачивание всей программы в
# блок try считается плохим стилем программирования.
# Команда try должна
# работать в связке с командой except или finally.
# Рассмотрим вариант обработки ошибки в нашем коде:
# После зарезервированного слова except указывается класс ошибки, которую мы
# хотим обработать. Обычно используется запись вида except NameError as e: Таким
# образом в переменную e попадает информация об ошибке. Например для вывода
# её в консоль, сохранения в логи и т.п. В нашем случае при невозможности получить
# целое число из пользовательского ввода сообщаем ему об этом. Далее делаем вид,
# что была введена единица. Программа продолжает работать несмотря на ошибку.

# def get(text: str = None) -> int:
#     data = input(text)
#     try:
#         num = int(data)
#     except ValueError as e:
#         print(f'Ваш ввод привёл к ошибке ValueError: {e}')
#         num = 1
#         print(f'Будем считать результатом ввода число {num}')
#     return num
#
#
# if __name__ == '__main__':
#     number = get('Введите целый делитель: ')
#     print(f'100 / {number} = {100 / number}')


# -----------------------------------------------------------------------
# ● Цикл while для обработки ошибок ввода
# Иногда необходимо получить данные повторно, если попытка не удалась. В случае с
# пользователем можем спрашивать его бесконечно, пока не добъёмся ввода целого числа.

# def get(text: str = None) -> int:
#     while True:
#         try:
#             num = int(input(text))
#             break
#         except ValueError as e:
#             print(f'Ваш ввод привёл к ошибке ValueError: {e}\n' f'Попробуйте снова')
#     return num
#
#
# if __name__ == '__main__':
#     number = get('Введите целый делитель: ')
#     print(f'100 / {number} = {100 / number}')


# -------------------------------------------------------------------------------------
# ● Несколько except для одного try
# Как вы уже догадались при вводе нуля в примерах на деление выше мы получим
# ошибку. Это ZeroDivisionError: division by zero.
# Вспомним высшую математику, а именно то, что при делении любого числа на ноль
# получаем бесконечность.
# В приведённом примере блок try обрабатывает сразу несколько строчек, которые
# способны вызвать разные ошибки. Не лучший вариант. Правильнее было бы
# разделить код на отдельные try блоки со своими возможными исключениями. Но
# зато мы познакомились с обработкой нескольких ошибок разом.
# Если не удалось получить целое число, обрабатываем ошибку значения и даём ещё
# один шанс. А если делим на ноль, вместо ошибки возвращаем бесконечность.
# Внимание! Язык Python поддерживает такие математические числа как
# бесконечность и минус бесконечность. Записываются они как особая форма
# вещественного числа:
# ● float(‘inf’) - бесконечность
# ● float(‘-inf’) - минус бесконечность

def hundred_div_num(text: str = None) -> tuple[int, float]:
    while True:
        try:
            num = int(input(text))
            div = 100 / num
            break
        except ValueError as e:
            print(f'Ваш ввод привёл к ошибке ValueError: {e}\n' f'Попробуйте снова')
        except ZeroDivisionError as e:
            div = float('inf')
            break
    return num, div


if __name__ == '__main__':
    n, d = hundred_div_num('Введите целый делитель: ')
    print(f'Результат операции: "100 / {n} = {d}"')