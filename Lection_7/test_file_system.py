import os
from pathlib import Path
import shutil

# # Определить текущий каталог
# print(os.getcwd())
# print(Path.cwd())

# # Изменить текущий каталог
# os.chdir('../..')
# print(os.getcwd())
# print(Path.cwd())


# #  Создание каталога
# os.mkdir('new_os_dir')
# Path('new_path_dir').mkdir()


# # Создание вложенных каталогов
# os.makedirs('dir/other_dir/new_os_dir')
# # Path('some_dir/dir/new_path_dir').mkdir() # FileNotFoundError
# Path('some_dir/dir/new_path_dir').mkdir(parents=True)


# # Удаление пустого каталога (удалится каталог последний в цепочке: new_os_dir и new_path_dir соответственно)
# os.rmdir('dir/other_dir/new_os_dir')
# Path('some_dir/dir/new_path_dir').rmdir()


# # Удаление не пустого каталога (удаление всего содержимого)
# shutil.rmtree('dir/other_dir')
# shutil.rmtree('some_dir')

# # Формирование пути
# file_1 = os.path.join(os.getcwd(), 'dir', 'new_file.txt')
# print(f'{file_1 = }\n{file_1}')
# file_2 = Path().cwd() / 'dir' / 'new_file.txt'
# print(f'{file_2 = }\n{file_2}')


# # Чтение данных о каталогах
# print(os.listdir())
#
# p = Path(Path().cwd())
# for obj in p.iterdir():
#     print(obj)


# # Проверка на директорию, файл и ссылку
# dir_list = os.listdir()
# for obj in dir_list:
#     print(f'{os.path.isdir(obj)=}', end='\t')
#     print(f'{os.path.isfile(obj)=}', end='\t')
#     print(f'{os.path.islink(obj)=}', end='\t')
#     print(f'{obj=}')
#
# print()
#
# p = Path(Path().cwd())
# for obj in p.iterdir():
#     print(f'{obj.is_dir() = }', end='\t')
#     print(f'{obj.is_file() = }', end='\t')
#     print(f'{obj.is_symlink() = }', end='\t')
#     print(f'{obj = }')

# # Обход папок через os.walk()
# for dir_path, dir_name, file_name in os.walk(os.getcwd()):
#     print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')


# for i in range(10):
#     with open(f'file_{i}.txt', 'w', encoding='utf-8') as f:
#         f.write('Hello world!')
# os.mkdir('new_dir')
# for i in range(2, 10, 2):
#     f = Path(f'file_{i}.txt')
#     f.replace('new_dir' / f)
# shutil.copytree('new_dir', Path.cwd() / 'dir_new')





