import csv


# # ● Чтение CSV
# # Функция csv.reader принимает на вход файловый дескриптор и построчно читает информацию.
# # Важно! При работе с CSV необходимо указывать параметр newline=’’ во время открытия файла.
# with open('biostats.csv', 'r', newline='') as f:
#     csv_file = csv.reader(f)
#     for line in csv_file:
#         print(line)
#
#     print(type(line))



# # Кроме файлового дескриптора можно передать любой объект поддерживающий
# # итерацию и возвращающий строки. Также функция reader может принимать
# # диалект отличный от заданного по умолчанию — “excel”. А при необходимости и
# # дополнительные параметры форматирования, если файл имеет свои особенности.
# # Файл biostats_tab.csv хранит те же данные, что и файл выше, но вместо разделителя
# # используется символ табуляции. По сути это разновидность TSV — файл с
# # разделителем табуляцией.
#
# with open('biostats_tab.csv', 'r', newline='') as f:
#     csv_file = csv.reader(f, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
#     for line in csv_file:
#         print(line)
# print(type(line))
#
# # ➢ dialect='excel-tab' — указали диалект с табуляцией в качестве разделителя
# # ➢ quoting=csv.QUOTE_NONNUMERIC — передали встроенную константу,
# # указывающую функции, что числа без кавычек необходимо преобразовать к типу float.



# # Чтение в список
# with open('biostats_tab.csv', 'r', newline='') as f_read:
#     csv_read = csv.reader(f_read, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
#     all_data = []
#     for line in csv_read:
#         all_data.append(line)
#     print(all_data)



# Чтение в словарь
# Если передать список строк в параметр fieldnames, они будут использоваться для
# ключей словаря, а не первая строка файла. В нашем примере передан “лишний”
# ключ count. Т.к. в таблице нет шестого столбца, ему было присвоено значение из
# параметра restval.
with open('biostats_tab.csv', 'r', newline='') as f:
    csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age", "height", "weight", "office"],\
               restkey="new", restval="Main Office", dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(f'{line=}')
        # print(f'{line["name"]=}\t{line["age"]=}')


# # Если количество ключей оказывается меньше, чем столбцов, недостающий ключ
# # берётся из параметра restkey. При этом все столбцы без ключа сохраняются как
# # элементы списка в restkey ключ.
# with open('biostats_tab.csv', 'r', newline='') as f:
#     csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age", ], restkey="new", restval="Main Office",
#                               dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
#     for line in csv_file:
#         print(f'{line = }')
#         print(f'{line["name"] = }\t{line["age"] = }')
