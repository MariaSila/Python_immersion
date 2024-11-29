# Задача 2. Чат
# Реализуйте программу - чат, в котором могут участвовать сразу несколько человек, то
# есть программа может работать одновременно для нескольких пользователей. При
# запуске запрашивается имя пользователя. После этого он выбирает одно из действий:
# 1. Посмотреть текущий текст чата
# 2. Отправить сообщение (затем вводит сообщение) Действия запрашиваются бесконечно.
# Подсказка № 1
#   Используйте input() для получения имени пользователя и выбора действий, чтобы
#   обеспечить взаимодействие с пользователем, используйте функцию input() для
#   получения имени и выбора действия (просмотр сообщений или отправка сообщения).
# Подсказка № 2
#   Для хранения сообщений используйте текстовый файл. Сохранение сообщений в
#   текстовом файле позволяет сохранить их между запусками программы и поддерживать
#   доступ для нескольких пользователей.
# Подсказка № 3
#   Обрабатывайте исключение FileNotFoundError при чтении сообщений. Убедитесь, что
#   программа корректно обрабатывает отсутствие файла с сообщениями, чтобы избежать
#   аварийного завершения работы.

class UserError(Exception):
    pass


class UserActionError(UserError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (f'Действие должен быть целым int() в диапазоне от 0 до 2\n'
                f' У вас тип {type(self.value)}, а значение {self.value}')


class Chat:
    file_chat = 'chat.txt'

    def __init__(self, name):
        self.name = name

    def load_chat(self):
        try:
            f_read = open(self.file_chat, 'r', encoding='utf-8')
        except FileNotFoundError:
            print(f'Сообщений нет. Файл не найден.')
        else:
            print('\nСообщения чата: ')
            for line in f_read:
                print(line, end='')
            f_read.close()

    def send_message(self):
        message = input('Введите сообщение: ')
        name = self.name
        with open(self.file_chat, 'a', encoding='utf-8') as f_w:
            f_w.write(f'{self.name}: {message}\n')

    def __eq__(self, other):
        return self.name == other.name


def get_act():
    action = int(input('\n1 - Прочитать сообщения'
                       '\n2 - Написать сообщение'
                       '\n0 - Закрыть чат'
                       '\nВыберите действие: '))
    if not isinstance(action, int) or 0 > action or 2 < action:
        raise UserActionError(action)
    return action


def main():
    while True:
        name = Chat(input('Введите свое имя: '))
        while True:
            try:
                act = get_act()
            except UserActionError as e:
                print(e)
            except ValueError:
                print('Не число')
            else:
                match act:
                    case 1:
                        name.load_chat()
                    case 2:
                        name.send_message()
                    case 0:
                        return False


if __name__ == '__main__':
    main()


# PERFECT SOLUTION
# class Chat:
#     def __init__(self, filename='chat.txt'):
#         self.filename = filename
#
#     def display_messages(self):
#         """Отображает все сообщения из файла."""
#         try:
#             with open(self.filename, 'r') as file:
#                 messages = file.readlines()
#                 print("".join(messages))
#         except FileNotFoundError:
#             print("Служебное сообщение: пока что ничего нет\n")
#
#     def add_message(self, name, message):
#         """Добавляет новое сообщение в файл."""
#         with open(self.filename, 'a') as file:
#             file.write(f"{name}: {message}\n")
#
#     def run(self):
#         """Запускает основной цикл чата."""
#         name = input("Как вас зовут? ")
#         while True:
#             print("Чтобы увидеть текущий текст чата введите 1, чтобы написать сообщение введите 2")
#             response = input("Введите 1 или 2: ")
#             if response == '1':
#                 self.display_messages()
#             elif response == '2':
#                 new_message = input("Введите сообщение: ")
#                 self.add_message(name, new_message)
#             else:
#                 print("Неизвестная команда\n")
#
#
# # Запуск программы
# if __name__ == "__main__":
#     chat = Chat()
#     chat.run()
