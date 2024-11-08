# Задача 4. Агрегирование данных из CSV файла
# Напишите скрипт, который считывает данные из CSV файла, содержащего
# информацию о продажах (название продукта, количество, цена за единицу), и
# подсчитывает общую выручку для каждого продукта. Итог должен быть сохранён в
# новом CSV файле.
# Пример: Из файла sales.csv нужно создать файл total_sales.csv, где для каждого
# продукта будет указана общая выручка.
# Подсказка № 1
# Используйте csv.DictReader для чтения данных из исходного CSV файла.
# csv.DictReader позволяет читать строки CSV файла как словари, где ключи
# соответствуют заголовкам столбцов.
# Подсказка № 2
# Создайте словарь для хранения выручки по каждому продукту. Используйте продукт в
# качестве ключа и выручку в качестве значения. Убедитесь, что добавляете выручку при
# встрече одинакового продукта.
# Подсказка № 3
# Используйте csv.DictWriter для записи данных в новый CSV файл. Запишите итоговые
# данные в новый файл, указывая заголовки столбцов и записывая итоговую выручку
# для каждого продукта.
# Подсказка № 4
# Преобразуйте данные в числовые типы для корректного вычисления выручки.
# Убедитесь, что данные из CSV преобразованы в целые или вещественные числа,
# чтобы корректно производить арифметические операции.

import csv


def revenue_csv(input_file: str, output_file: str) -> None:
    with (
        open(input_file, 'r', newline='') as f_read,
        open(output_file, 'w', newline='', encoding='utf-8') as f_write
    ):
        csv_read = csv.DictReader(f_read, dialect='excel')
        total_sales = {}
        for row in csv_read:
            product = row['product']
            count = int(row['quantity'])
            price = float(row['price'])
            revenue = round(count * price, 2)
            if product in total_sales:
                total_sales[product] += revenue
            else:
                total_sales[product] = revenue

        csv_write = csv.DictWriter(f_write, fieldnames=['product', 'revenue'],
                                   dialect='excel-tab', quoting=csv.QUOTE_NONE)
        csv_write.writeheader()
        for product, revenue in total_sales.items():
            csv_write.writerow({'product': product, 'revenue': revenue})


if __name__ == '__main__':
    revenue_csv('sales.csv', 'revenue_sales.csv')


# # perfect solution
# def calculate_total_sales(input_file, output_file):
#     sales_totals = {}
#     with open(input_file, 'r') as f:
#         reader = csv.DictReader(f)
#         for row in reader:
#             print(row)
#             product = row['название продукта']
#             quantity = int(row['количество'])
#             price_per_unit = float(row['цена за единицу'])
#             total_sales = quantity * price_per_unit
#
#             if product in sales_totals:
#                 sales_totals[product] += total_sales
#             else:
#                 sales_totals[product] = total_sales
#
#         with open(output_file, 'w', newline='') as f:
#             fieldnames = ['название продукта', 'общая выручка']
#             writer = csv.DictWriter(f, fieldnames=fieldnames)
#             writer.writeheader()
#         for product, total_sales in sales_totals.items():
#             writer.writerow({'название продукта': product, 'общая выручка': total_sales})
#
#
# if __name__ == "__main__":
#     calculate_total_sales('sales.csv', 'total_sales.csv')

