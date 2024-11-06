import json
my_dict = {
    "first_name": "Джон",
    "last_name": "Смит",
    "hobbies": ["кузнечное дело", "программирование", "путешествия"],
    "age": 35,
    "children": [
        {
            "first_name": "Алиса",
            "age": 5
        },
        {
            "first_name": "Маруся",
            "age": 3
        }
    ]
}
print(f'{type(my_dict)=}\n{my_dict = }')
with open('new_user.json', 'w') as f:
    json.dump(my_dict, f)

# В файле new_user.json получим одну длинную строку
# Символы отличные от ASCII будут заменены на специальные коды.
# Это не означает, что файл повреждён или что-то пошло не так

#  Проведём десериализацию уже знакомым способом и проверим целостность данных
with open('new_user.json', 'r', encoding='utf-8') as f:
    new_dict = json.load(f)
print(f'{new_dict=}')

# Если же мы хотим отказаться от символов экранирования в JSON файле, следует
# установить дополнительный параметр ensure_ascii в значение ложь.
with open('new_user2.json', 'w', encoding='utf-8') as f:
    json.dump(my_dict, f, ensure_ascii=False)


# Получить объект типа str хранящий структуру json
dict_to_json_text = json.dumps(my_dict, ensure_ascii=False)
print(f'{type(dict_to_json_text)=}\n{dict_to_json_text=}')


res = json.dumps(my_dict, indent=2, separators=(',', ':'), sort_keys=True)
print(res)
# ➢ Параметр indent отвечает за форматирование с отступами. Теперь JSON
# выводится не в одну строку, а в несколько. Читать стало удобнее, но размер
# увеличился.
# ➢ Параметр separators принимает на вход кортеж из двух строковых элементов.
# Первый — символ разделитель элементов. По умолчанию это запятая и
# пробел. Второй — разделитель ключа и значения. По умолчанию это
# двоеточие и пробел. Передав запятую и двоеточие без пробела JSON стал
# компактнее.
# ➢ Параметр sort_keys отвечает за сортировку ключей по алфавиту. Нужна
# сортировка или нет, решать только вам.

