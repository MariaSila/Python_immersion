# 4. Пара полезных структур данных
# Модуль collections

# -----------------------------------------------------------------------------------
# Модуль предоставляет доступ к встроенным в Python типам данных, но
# “спрятанным” от начинающего разработчика. Внутри хранится много интересных и
# полезных структур данных. А в collections.abc огромный набор абстрактных типов.
# Но сегодня мы рассмотрим функцию namedtuple из модуля.


# Фабричная функция namedtuple
# -----------------------------------------------------------------------------------
# Функция namedtuple является фабрикой классов. Из названия следует, что она
# создаёт именованные кортежи. Рассмотрим простой пример, чтобы понять что это.
# Функция принимает пару обязательных значений:
#       1. Имя класса. Это строка, содержащее точно такое же имя как и переменная
#           слева от знака равно.
#       2. Список строк или строка с пробелами в качестве разделителей. Имена из
#           списка превращаются в свойства класса.
# На выходе получаем класс, аналогичный созданному вручную классу class. При
# этом в классе помимо указанных в списке свойств автоматически создаются
# некоторые дандер методы. Например мы с лёгкостью распечатали экземпляр u_1,
# потому что он определил свой дандер __repr__.

# from collections import namedtuple
# from datetime import datetime
#
# User = namedtuple('User', ['first_name', 'last_name', 'birthday'])
# u_1 = User('Исаак', 'Ньютон', datetime(1643, 1, 4))
#
# print(u_1)
# print(f'{type(User)}, {type(u_1)}')


# -----------------------------------------------------------------------------------
# Как и с экземплярами класса, мы можем получить доступ к свойствам используя
# точечную нотацию.
# Обратите внимание, что свойство день рождение является объектом datetime со
# своими свойствами. Доступ к ним мы получаем также через точечную нотацию

# from collections import namedtuple
# from datetime import datetime
#
# User = namedtuple('User', ['first_name', 'last_name', 'birthday'])
# u_1 = User('Исаак', 'Ньютон', datetime(1643, 1, 4))
# print(u_1)
# print(u_1.first_name, u_1.birthday.year)


# -----------------------------------------------------------------------------------
# При создании класса можно дополнительно передать список значений по
# умолчанию. И если дефолтных значений меньше, чем свойств в классе, назначение
# происходит справа налево
# Составление списка с именами полей и значениями по умолчанию движется справа
# налево, поэтому в birthday попадает текущая дата, а фамилию по умолчанию -
# Иванов. Значения подставляются только в том случае, когда экземпляр не передаёт
# свои, как и с обычными классами.
# 💡 Внимание! Посмотрите на даты у каждого из экземпляров. Время
# совпадает до секунды несмотря на 7 секунд разницы в создании. Значения для
# birthday было вычислено один раз, в момент создания класса.
# На самом деле ситуация с функциями неоднозначно. С одной стороны ничего не
# мешает присвоить экземпляру в качестве свойства созданную функцию. Но в
# отличии от классических классов, классы namedtuple рассчитаны на хранение
# свойств, а не методов.
# 🔥 Важно! Если вам нужен объект с методами, используйте классический
# ООП.

# import time
# from collections import namedtuple
#
# from datetime import datetime
# User = namedtuple('User', ['first_name', 'last_name', 'birthday'], defaults=['Иванов', datetime.now()])
# u_1 = User('Исаак')
# print(f'{u_1.last_name}, {u_1.birthday.strftime("%H:%M:%S")}')
#
# time.sleep(7)
#
# u_2 = User('Галилей', 'Галилео')
# print(f'{u_2.last_name}, {u_2.birthday.strftime("%H:%M:%S")}')


# -----------------------------------------------------------------------------------
# Как и в случае с неизменяемыми датами, экземпляры namedtuple также неизменны.
# Но если надо внести правку в какое-то поле, встроенный метод _replace создаст
# копию, заменив только указанные значения.

# from collections import namedtuple
#
# Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
# a = Point(2, 3, 4)
# b = a._replace(z=0, x=a.x + 4)
# print(b)
# print(a)


# -----------------------------------------------------------------------------------
# Экземпляры можно сортировать. Метод проверки “меньше” определяется для
# свойств автоматически
# Как вы могли заметить при совпадении значений первого по счёту свойства
# происходит сравнение второго и т.д. пока не определится меньший элемент

# from collections import namedtuple
#
# Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
# data = [Point(2, 3, 4), Point(10, -100, -500), Point(3, 7, 11),
# Point(2, 202, 1)]
# print(sorted(data))


# -----------------------------------------------------------------------------------
# И ещё одна интересная особенность namedtuple. Если все свойства являются
# объектами неизменяемого типа, экземпляр может быть ключом словаря, элементом
# множества и т.п.
# Точка mut_point была создана и ошибки нет. namedtuple допускает изменяемые
# типы для свойств. Но такой экземпляр перестают быть хэшируемым. Как результат
# ошибка при добавлении точки в качестве ключа словаря.
# И конечно же стоит упомянуть о таком плюсе namedtuple как экономия памяти.
# Экземпляры занимают в памяти столько же, сколько и обычные кортежи.

# from collections import namedtuple
#
# Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
# d = {
#     Point(2, 3, 4): 'first',
#     Point(10, -100, -500): 'second',
#     Point(3, 7, 11): 'last',
# }
# print(d)
# mut_point = Point(2, [3, 4, 5], 6)
# print(mut_point)
# # d.update({mut_point: 'bad_point'})  # TypeError: unhashable type: 'list'