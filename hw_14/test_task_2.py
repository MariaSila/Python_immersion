import unittest
from task_2 import Library, BookNotFoundError


class TestCaseLibrary(unittest.TestCase):
    def setUp(self):
        self.lib = Library(['Война и мир, Л.Толстой'])

    def test_add_book(self):
        self.lib.add_book('Тихий дон, М.Шолохов')
        self.assertEqual(self.lib.list_books(), ['Война и мир, Л.Толстой', 'Тихий дон, М.Шолохов'])

    def test_remove_book(self):
        self.lib.remove_book('Война и мир, Л.Толстой')
        self.assertEqual(self.lib.list_books(), [])

    def test_remove_err(self):
        with self.assertRaises(BookNotFoundError):
            self.lib.remove_book('Оно, С.Кинг')

    def test_list_books(self):
        self.lib.add_book('Маленький принц, Э.Экзюпери')
        self.lib.add_book('Старик и море, Хемингвей')
        self.assertEqual(self.lib.list_books(), ['Война и мир, Л.Толстой', 'Маленький принц, Э.Экзюпери', 'Старик и море, Хемингвей'])
        self.lib.remove_book('Старик и море, Хемингвей')
        self.assertEqual(self.lib.list_books(), ['Война и мир, Л.Толстой', 'Маленький принц, Э.Экзюпери'])


if __name__ == '__main__':
    unittest.main()
