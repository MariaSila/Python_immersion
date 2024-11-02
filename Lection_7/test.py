# # запись методом write
# text = ['text write 1', 'text write 2', 'text write 3']
# with open('new_data.txt', 'a', encoding='utf-8') as f:
#     for line in text:
#         res = f.write(f'{line}\n')
#         print(f'{res=}\n{len(line)=}')


# # запись методом writelines
# text = ['text writelines 4', 'text writelines 5', 'text writelines 6']
# with open('new_data.txt', 'a', encoding='utf-8') as f:
#     f.writelines('\n'.join(text))


# # запись через print в файл
# text = ['text print 7', 'text print 8', 'text print 9']
# with open('new_data.txt', 'a', encoding='utf-8') as f:
#     for line in text:
#         print(line, file=f)


# # перемещение "курсора" метод tell
# text = ['text tell 1', 'text tell 2', 'text tell 3']
# with open('new_data.txt', 'w', encoding='utf-8') as f:
#     print(f.tell())
#     for line in text:
#         f.write(f'{line}\n')
#         print(f.tell())
#     print(f.tell())

# # перемещение "курсора" метод seek
# last = before = 0
# text = ['text seek 4', 'text seek 5', 'text seek 6']
# with open('new_data.txt', 'r+', encoding='utf-8') as f:
#     while line := f.readline():
#         last, before = f.tell(), last
#     print(f'{last=}, {before=}')
#     print(f'{f.seek(before, 0)=}')
#     f.write('\n'.join(text))


# # перемещение "курсора" Метод truncate
# last = before = 0
# with open('new_data.txt', 'r+', encoding='utf-8') as f:
#     while line := f.readline():
#         last, before = f.tell(), last
#     print(f'{last}, {before}')
#     print(f.seek(before, 0))
#     print(f.truncate())


# size = 64
# with open('new_data.txt', 'r+', encoding='utf-8') as f:
#     print(f.truncate(size))


# # пример
# start = 10
# stop = 100
# with open('data.bin', 'bw+') as f:
#     for i in range(start, stop + 1):
#         f.write(str(i).encode('utf-8'))  # кодируем строку в байты, предварительно число преобразовано в строку
#         # print(f'{i=} {f.tell()=}')  # печать для демонстрации перемещения курсора
#         if i % 3 == 0:
#             f.seek(-2, 1)  # перемещение курсора на 2 влево
#     f.truncate(stop)  # изменяем размер файла, в данном случае усекаем до stop=100
#     f.seek(0)  # перемещаем курсор в начало
#     res = f.read(start)  # читаем 10 байтов (start=10) из файла и записываем в переменную res
#     print(res.decode('utf-8'))  # декодируем данные обратно в строку

    # >>> на выходе получаем первые 10 байтов преобразованных в текст

