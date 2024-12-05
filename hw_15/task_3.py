# Задача 3. Планирование задач
# Напишите функцию, которая принимает количество дней от текущей даты и
# возвращает дату, которая наступит через указанное количество дней. Дополнительно,
# выведите эту дату в формате YYYY-MM-DD.
# Подсказка № 1
#   Используйте from datetime import datetime, timedelta, чтобы получить доступ к текущей
#   дате и времени, а также к функции для добавления или вычитания дней.
# Подсказка № 2
#   Вызовите datetime.now() для получения текущей даты и времени в виде объекта datetime.
# Подсказка № 3
#   Создайте объект timedelta, который представляет собой интервал времени, а затем
#   добавьте его к текущей дате для получения даты в будущем.
# Подсказка № 4
#   Примените метод strftime() для преобразования объекта datetime в строку в
#   формате YYYY-MM-DD.

from datetime import datetime, timedelta


def manager_tasks(days: int) -> datetime.date:
    cur_date = datetime.now()
    new_date = cur_date + timedelta(days)
    return new_date.strftime('%Y-%m-%d')


if __name__ == '__main__':
    print(manager_tasks(25))


# PERFECT SOLUTION
# from datetime import datetime, timedelta
#
#
# def future_date(days_from_now):
#     """
#     Возвращает дату, которая наступит через указанное количество
#     дней от текущей даты.
#     :param days_from_now: Количество дней от текущей даты.
#     :return: Отформатированная дата в формате YYYY-MM-DD.
#     Примеры:
#     >>> future_date(30)
#     '2024-09-08'
#     >>> future_date(-10)
#     '2024-07-30'
#     """
#     # Получение текущей даты и времени
#     today = datetime.now()
#     # Вычисление даты через указанное количество дней
#     future_date = today + timedelta(days=days_from_now)
#     # Форматирование будущей даты в строку в формате YYYY-MM-DD
#     formatted_future_date = future_date.strftime('%Y-%m-%d')
#     return formatted_future_date
#
#
# if __name__ == '__main__':
#     days = 30 # Количество дней для вычисления
#     print(f'Date {days} days from now: {future_date(days)}')