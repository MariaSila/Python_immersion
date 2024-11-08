# Задача 5. Конвертация CSV в JSON с изменением структуры данных
# Напишите скрипт, который считывает данные из CSV файла и сохраняет их в
# JSON файл с другой структурой. CSV файл содержит данные о книгах (название,
# автор, год издания). В JSON файле данные должны быть сгруппированы по
# авторам, а книги каждого автора должны быть записаны как список.
# Пример: Из файла books.csv нужно создать файл books_by_author.json, где
# книги сгруппированы по авторам.
# Подсказка № 1
# Используйте csv.DictReader для чтения данных из CSV файла. Эта функция читает
# данные из CSV файла и преобразует каждую строку в словарь, где ключи
# соответствуют заголовкам столбцов.
# Подсказка № 2
# Создайте словарь, где ключи будут авторами, а значения — списками книг.
# Используйте словарь для группировки книг по авторам. Для каждого автора создавайте
# список книг, который будет заполняться по мере чтения CSV файла.
# Подсказка № 3
# Преобразуйте данные в формат JSON с помощью json.dump(). После того как данные
# сгруппированы, используйте json.dump() для записи данных в файл JSON.
# Убедитесь, что данные имеют нужный формат и структуру.

import csv
import json


def books_by_author(input_file: str, output_file: str) -> None:
    with open(input_file, 'r', newline='') as f_read:
        read_f = csv.DictReader(f_read, delimiter=';')
        author_books = {}
        for book in read_f:
            author = book['authors']
            book = {'book': book['title'], 'publication_date': book['publication_date']}
            if author not in author_books:
                author_books[author] = [book]
            else:
                author_books[author].append(book)
        with open(output_file, 'w', encoding='utf-8') as f_write:
            json.dump(author_books, f_write, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    books_by_author('books.csv', 'books_by_author.json')


# # perfect solution
# def convert_csv_to_json(input_file, output_file):
#     books_by_author = {}
#     with open(input_file, 'r') as f:
#         reader = csv.DictReader(f, delimiter=';')
#         for row in reader:
#             author = row['authors']
#             book = {
#                 'title': row['title'],
#                 'publication_date': row['publication_date']
#             }
#             if author in books_by_author:
#                 books_by_author[author].append(book)
#             else:
#                 books_by_author[author] = [book]
#
#     with open(output_file, 'w') as f:
#         json.dump(books_by_author, f, indent=4, ensure_ascii=False)
#
#
# if __name__ == "__main__":
#     convert_csv_to_json('books.csv', 'books_by_author2.json')
