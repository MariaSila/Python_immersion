# Задача 3. Агрегирование данных из CSV файла
# Напишите скрипт, который считывает данные из JSON файла и сохраняет их в CSV
# файл. JSON файл содержит данные о продуктах (название, цена, количество на
# складе). В CSV файле каждая строка должна соответствовать одному продукту.
# Пример: Из файла products.json нужно создать products.csv.
# Подсказка № 1
# Используйте json.load() для чтения данных из JSON файла. Функция json.load()
# позволяет загрузить данные из JSON файла в виде Python объекта, например, списка
# словарей.
# Подсказка № 2
# Используйте csv.DictWriter для записи данных в CSV файл. Функция
# csv.DictWriter позволяет записывать данные в CSV файл, где каждый словарь из
# списка становится одной строкой в CSV.
# Подсказка № 3
# Обеспечьте правильное управление строками в CSV файле. При записи в CSV файл
# используйте параметр newline='' в open(), чтобы избежать дополнительных пустых
# строк между записями на Windows.
import json
import csv


def json_to_csv(input_file: str, output_file: str) -> None:
    with (
        open(input_file, 'r', encoding='utf-8') as f_read,
        open(output_file, 'w', newline='', encoding='utf-8') as f_write
    ):
        json_file = json.load(f_read)

        keys = json_file[0].keys()
        csv_file = csv.DictWriter(f_write, fieldnames=keys, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
        csv_file.writeheader()
        csv_file.writerows(json_file)


if __name__ == '__main__':
    json_to_csv('products.json', 'products.csv')


# # perfect solution
# def json_to_csv(json_file, csv_file):
#     """Превращает данные из JSON файла в CSV файл."""
#     with open(json_file, 'r') as f:
#         data = json.load(f)
#
#     # Проверка корректности формата данных
#     if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
#         raise ValueError("Некорректный формат данных в JSON файле")
#
#     with open(csv_file, 'w', newline='') as f:
#         fieldnames = data[0].keys()
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(data)
#
#
# if __name__ == "__main__":
#     json_to_csv('products.json', 'products.csv')
