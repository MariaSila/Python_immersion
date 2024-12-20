# Задача 4. Генерация паролей
# Напишите программу, которая генерирует случайный пароль заданной длины,
# состоящий из букв, цифр и специальных символов.
# Подсказка № 1
# Используйте модуль random для генерации случайных символов и модуль string для
# доступа к наборам символов (буквы, цифры, специальные символы).
# Подсказка № 2
# Примите длину пароля от пользователя, используя функцию input(), и преобразуйте
# её в целое число с помощью int().
# Подсказка № 3
# Определите набор символов для пароля, используя строки из модуля string.
# Объедините буквы, цифры и специальные символы в одну строку.
# Подсказка № 4
# Используйте генератор выражений и функцию random.choice() для выбора
# случайных символов из набора. Соберите символы в строку с помощью метода join().


import random
import string

length = int(input('Enter password length: '))

password = ''
characters = string.ascii_letters + string.digits + string.punctuation

for i in range(length):
    password += ''.join(random.choice(characters))

print(password)


# # perfect solution
# length = int(input("Введите длину пароля: "))
#
# characters = string.ascii_letters + string.digits + string.punctuation
#
# password = ''.join(random.choice(characters) for i in range(length))
#
# print(password)


