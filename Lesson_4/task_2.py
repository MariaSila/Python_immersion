# Задание №2
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

#1
def fix_unicode(text: str) -> list[int]:
    code_list = []
    for char in set(text):
        code_list.append(ord(char))
    return sorted(code_list, reverse=True)

#2
def fix_unicode1(text: str) -> list[int]:
    code_list = sorted([ord(char) for char in set(text)], reverse=True)
    return code_list


string = input('Введите текст: ')
print(fix_unicode(string))
print(fix_unicode1(string))


