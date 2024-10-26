# Задача 5. Яйца
# В рамках программы колонизации Марса компания «Спейс Инжиниринг»
# вывела особую породу черепах, которые, по задумке, должны размножаться,
# откладывая яйца в марсианском грунте. Откладывать яйца слишком близко к
# поверхности опасно из-за радиации, а слишком глубоко — из-за давления
# грунта и недостатка кислорода. Вообще, факторов очень много, но
# специалисты проделали большую работу и предположили, что уровень
# опасности для черепашьих яиц рассчитывается по формуле: D = x^3 − 3x^2 −
# 12x + 10, где x — глубина кладки в метрах, а D — уровень опасности в
# условных единицах. Для тестирования гипотезы нужно взять пробу грунта на
# безопасной, согласно формуле, глубине.
# Напишите программу, находящую такое значение глубины х, при котором
# уровень опасности как можно более близок к нулю. На вход программе
# подаётся максимально допустимое отклонение уровня опасности от нуля, а
# программа должна рассчитать приблизительное значение х, удовлетворяющее
# этому отклонению. Известно, что глубина точно больше нуля и меньше четырёх
# метров. Обеспечьте контроль ввода.
# Пример:
# Введите максимально допустимый уровень опасности: 0.01
# Приблизительная глубина безопасной кладки: 0.732421875 м
# Подсказка № 1
# Создайте функцию calculate_danger, которая принимает глубину x и возвращает
# уровень опасности, рассчитанный по формуле D=x3−3x2−12x+10. D = x^3 - 3x^2 - 12x +
# 10. D=x3−3x2−12x+10. Эта функция будет использоваться для расчета уровня
# опасности на разных глубинах.
# Подсказка № 2
# Создайте функцию find_safe_depth, которая принимает максимальное допустимое
# отклонение max_danger. В этой функции реализуйте метод деления интервала
# пополам (бинарный поиск) для нахождения глубины, при которой уровень опасности
# максимально близок к нулю. Внутри этой функции вызовите calculate_danger для
# вычисления уровня опасности на текущей глубине.
# Подсказка № 3
# В функции find_safe_depth, инициализируйте границы интервала (глубина от 0 до 4
# метров). В цикле while обновляйте границы интервала в зависимости от знака
# текущего уровня опасности, пока уровень опасности не станет меньше максимального
# допустимого отклонения.
# Подсказка № 4
# Создайте основную функцию main, которая будет запрашивать у пользователя ввод
# максимально допустимого уровня опасности. Обработайте случай неверного ввода,
# например, если введено отрицательное значение или нечисловое значение.
# Используйте find_safe_depth для нахождения безопасной глубины


def calculate_danger(x):
    d = x ** 3 - 3 * x ** 2 - 12 * x + 10
    return d * -1


def find_safe_depth(max_d):
    min_x = 0.0
    max_x = 4.0
    flag = True
    while flag:
        x = (max_x - min_x )/ 2 + min_x
        d = calculate_danger(x)
        if d > max_d:
            max_x = (max_x - min_x ) / 2 + min_x
        else:
            min_x = max_x - (max_x - min_x ) / 2

        if abs(d - max_d) <= 0.01:
            flag = False
            return x


def main():
    danger = float(input('Введите максимально допустимый уровень опасности: '))
    if danger < 0:
        print('Не верный вод, необходимо ввести числовое значение больше нуля')
    else:
        x = find_safe_depth(danger)
        print(f'Приблизительная глубина безопасной кладки: {x} м')


main()

# # perfect solution
# def calculate_danger(x):
#     return x ** 3 - 3 * x ** 2 - 12 * x + 10
#
#
# def find_safe_depth(max_danger):
#     d_min = 0
#     d_max = 4
#     d_middle = (d_min + d_max) / 2
#     middle_danger = calculate_danger(d_middle)
#     while abs(middle_danger) > max_danger:
#         if middle_danger > 0:
#             d_min = d_middle
#         else:
#             d_max = d_middle
#         d_middle = (d_min + d_max) / 2
#         middle_danger = calculate_danger(d_middle)
#     return d_middle
#
#
# def main():
#     max_danger = float(input('Введите допустимый уровень опасности:'))
#     if max_danger < 0:
#         print('Вы ввели недопустимое значение! Попробуйте еще раз.')
#     else:
#         safe_depth = find_safe_depth(max_danger)
#         print(f'Приблизительная глубина безопасной кладки:{safe_depth:.9f} м')
#
#
# main()