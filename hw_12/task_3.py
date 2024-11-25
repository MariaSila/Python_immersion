# Задача 3. Класс с динамическим созданием экземпляров
# Создайте класс Book, который создает экземпляры с помощью __new__. Убедитесь,
# что каждый экземпляр имеет уникальный идентификатор.
# Подсказка № 1
# Используйте метод __new__ для контроля создания экземпляров класса. Этот метод
# вызывается перед __init__ и позволяет управлять созданием экземпляра. Вы
# можете использовать его для присвоения уникального идентификатора каждому
# экземпляру.
# Подсказка № 2
# Создайте класс-атрибут для хранения текущего значения уникального
# идентификатора. Класс-атрибут, например _id_counter, поможет отслеживать и
# увеличивать идентификатор для каждого нового экземпляра.
# Подсказка № 3
# В методе __new__ создайте экземпляр с помощью super().__new__(cls). Это обеспечит
# вызов стандартного механизма создания нового экземпляра и позволит затем
# установить дополнительные атрибуты.
# Подсказка № 4
# После создания экземпляра в методе __new__ присвойте уникальный идентификатор.
# Обновите атрибут экземпляра и увеличьте значение счетчика идентификаторов для
# последующих экземпляров.
# Подсказка № 5
# Используйте метод __init__ для инициализации остальных атрибутов экземпляра,
# таких как title и author. После того как экземпляр создан и идентификатор присвоен,
# метод __init__ может использоваться для установки других свойств объекта.

class Book():
    _id_counter = 1

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.uniq_id = cls._id_counter
        cls._id_counter += 1
        return instance

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book(id={self.uniq_id}, title={self.title}, author={self.author})"


if __name__ == '__main__':
    b1 = Book('Война и мир', 'Толстой Л.Н.')
    b2 = Book('Оно', 'Кинг С.')

    print(b1)
    print(b2)


# PERFECT SOLUTION
# class Book:
#     _id_counter = 1
#
#     def __new__(cls, *args, **kwargs):
#         instance = super().__new__(cls)
#         instance.id = cls._id_counter
#         cls._id_counter += 1
#         return instance
#
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#     def __str__(self):
#         return f"Book(ID={self.id}, title={self.title}, author={self.author})"
#
#
# # Пример использования
# book1 = Book("1984", "George Orwell")
# book2 = Book("To Kill a Mockingbird", "Harper Lee")
# print(book1)
# print(book2)