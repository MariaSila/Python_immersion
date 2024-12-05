# Проверка исполняемой документации
# Проект по созданию модуля работы с простыми числами оказался успешным. Мы
# сохранили код в prime.py и активного расширяем его возможности. Самое время
# написать файл документации к модулю. Создаём prime.md — текстовый файл,
# поддерживающий разметку Markdown
# 🔥 Важно! Обычно документацию пишут на английском языке. В учебном
# примере специально был выбран русский как основной язык на учебной
# платформе. Вы всегда можете использовать современные online переводчики
# для получения нужного языка.
# В документации есть несколько примеров, имитирующих работу в режиме
# интерпретатора. Убедимся, что они рабочие, написав в отдельном файле пару строк
# кода.
# Функция testfile построчно читает переданный ей файл и если встречает примеры
# выполнения кода, тестирует их работоспособность. Обратите внимание, что мы
# указываем на необходимость импорта функции в самом начале документации. И
# после вызова оставили пустую строку. doctest сделает импорт и не будет ожидать
# ничего в ответ. Да, это строчка будет воспринята как тест. И без него все
# последующие примеры провалятся. Ведь режим интерпретатора работает
# последовательно.


import doctest

doctest.testfile('prime.md', verbose=True)

# Запуск из терминала
# Вызываем интерпретатор python и в качестве модуля указываем doctest. Далее
# передаём путь до файла, который хотим тестировать. Если файл имеет расширение
# py, запускаеты функция testmod (строки 1 и 2). А если у файла другое расширение,
# предполагается что это исполняемая документация и запускается функция testfile
# (строки 3 и 4). Дополнительный ключ -v включает режим подробного вывода
# результатов тестирования.

# (venv) PS C:\Users\user\Python_immersion> python -m doctest .\Lecture_14\tdd_.py
# (venv) PS C:\Users\user\Python_immersion> python -m doctest .\Lecture_14\tdd_.py -v
# (venv) PS C:\Users\user\Python_immersion> python -m doctest .\Lecture_14\prime.md -v
# (venv) PS C:\Users\user\Python_immersion> python -m doctest .\Lecture_14\prime.md

