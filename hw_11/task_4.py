# Задача 4. Стек
# В программировании нередко необходимо создавать свои собственные
# структуры данных на основе уже существующих. Одной из таких базовых
# структур является стек.
# Стек — это абстрактный тип данных, представляющий собой список элементов,
# организованных по принципу LIFO (англ. last in — first out, «последним пришёл —
# первым вышел»).
# Простой пример: стек из книг на столе. Единственной книгой, обложка которой
# видна, является самая верхняя. Чтобы получить доступ, например, к третьей
# снизу книге, нам нужно убрать все книги, лежащие сверху, одну за другой.
# Напишите класс, который реализует стек и его возможности (достаточно будет
# добавления и удаления элемента).
# После этого напишите ещё один класс — «Менеджер задач». В менеджере задач
# можно выполнить команду «новая задача», в которую передаётся сама задача
# (str) и её приоритет (int). Сам менеджер работает на основе стека (не
# наследование). При выводе менеджера в консоль все задачи должны быть
# отсортированы по следующему приоритету: чем меньше число, тем выше задача.
# Вот пример основной программы:
# manager = TaskManager()
# manager.new_task("сделать уборку", 4)
# manager.new_task("помыть посуду", 4)
# manager.new_task("отдохнуть", 1)
# manager.new_task("поесть", 2)
# manager.new_task("сдать ДЗ", 2)
# print(manager)
# Результат:
# 1 — отдохнуть
# 2 — поесть; сдать ДЗ
# 4 — сделать уборку; помыть посуду
# Дополнительно: реализуйте также удаление задач и подумайте, что делать с
# дубликатами
# Подсказка № 1
# Используйте словари для хранения задач. В классе TaskManager можно использовать
# словарь для хранения стеков задач, где ключом будет приоритет, а значением — стек
# задач с этим приоритетом.
# Подсказка № 2
# Реализуйте метод для удаления задач. Добавьте метод в класс TaskManager, который
# будет удалять задачу по её тексту, независимо от приоритета.
# Подсказка № 3
# Избегайте дубликатов в стеках. Если вы не хотите, чтобы в стеке были дубликаты
# задач, проверьте перед добавлением, содержится ли задача уже в стеке.
# Подсказка № 4
# Сортировка по приоритету. Для корректного вывода задач по приоритету, отсортируйте
# ключи словаря по возрастанию и выводите задачи, начиная с наименьшего
# приоритета.


class Stack():
    def __init__(self, stack=None):
        self.stack = stack if stack is not None else []

    def add(self, item):
        self.stack.append(item)

    def delete(self):
        if not len(self.stack) == 0:
            return self.stack.pop()
        else:
            print("Стек уже пуст.")

    def is_empty(self):
        return len(self.stack) == 0

    def __str__(self):
        return f'{', '.join(i for i in self.stack)}'

    def __repr__(self):
        return f'Stack({self.stack})'


class TaskManager():
    def __init__(self):
        self.dict_task = {}
        self.set_task = set()

    def new_task(self, task: str, priority: int) -> None:
        if self.dict_task.get(priority):
            if not self.is_double(task):
                self.set_task.add(task)
                self.dict_task[priority].add(task)
                # print(f'Задача {task} добавлена к приоритету {priority} ')
            else:
                print(f'Задача {task} уже есть в Менеджере задач')
        else:
            self.dict_task[priority] = Stack([task])
            self.set_task.add(task)
            # print(f'Добавлена задача с новым приоритетом {priority}, {task}')

    def is_double(self, task):
        for el in self.set_task:
            if el == task:
                return True
        return False

    def done(self, task):
        flag = False
        for stack in self.dict_task.values():
            temp_stack = Stack()
            while not stack.is_empty():
                t = stack.delete()
                if t != task:
                    temp_stack.add(t)
                elif t == task:
                    flag = True
            while not temp_stack.is_empty():
                stack.add(temp_stack.delete())
        if flag:
            print(f'Задача {task} выполнена')
        else:
            print(f'Задачи {task} нет в списке')

    def __str__(self):
        lst_keys = sorted(self.dict_task.keys())
        return f'\nСписок задач:\n{'\n'.join(str(key) + ' - ' + str(self.dict_task[key]) for key in lst_keys)}\n'


def main():
    manager = TaskManager()
    manager.new_task('помыть посуду', 2)
    manager.new_task('помыть посуду', 2)
    manager.new_task("сделать уборку", 4)
    manager.new_task("сходить в магазин", 4)
    manager.new_task("отдохнуть", 1)
    manager.new_task("поесть", 2)
    manager.new_task("сдать ДЗ", 2)
    print(manager)
    manager.done('бег')
    manager.done('поесть')
    print(manager)


if __name__ == '__main__':
    main()


# # PERFECT SOLUTION
# class Stack:
#     def __init__(self):
#         self.__stack = list()
#
#     def pop(self):
#         if self.is_empty():
#             return None
#         return self.__stack.pop()
#
#     def push(self, item):
#         self.__stack.append(item)
#
#     def is_empty(self):
#         return len(self.__stack) == 0
#
#     def top(self):
#         if self.is_empty():
#             return None
#         return self.__stack[-1]
#
#
# class TaskManager:
#     def __init__(self):
#         self.tasks = dict()
#
#     def new_task(self, text, priority):
#         if priority not in self.tasks:
#             self.tasks[priority] = Stack()
#         self.tasks[priority].push(text)
#
#     def remove_task(self, text):
#         for stack in self.tasks.values():
#             temp_stack = Stack()
#             while not stack.is_empty():
#                 task = stack.pop()
#                 if task != text:
#                     temp_stack.push(task)
#             while not temp_stack.is_empty():
#                 stack.push(temp_stack.pop())
#
#     def __str__(self):
#         sorted_keys = sorted(self.tasks.keys())
#         out = []
#         for key in sorted_keys:
#             task_line = [str(key)]
#             temp_stack = Stack()
#             while not self.tasks[key].is_empty():
#                 task = self.tasks[key].pop()
#                 temp_stack.push(task)
#             while not temp_stack.is_empty():
#                 task_line.append(temp_stack.pop())
#             out.append(' '.join(task_line))
#         return '\n'.join(out)
#
#
# def main():
#     manager = TaskManager()
#     manager.new_task("сделать уборку", 4)
#     manager.new_task("помыть посуду", 4)
#     manager.new_task("отдохнуть", 1)
#     manager.new_task("поесть", 2)
#     manager.new_task("сдать дз", 2)
#     # Печать списка задач
#     print(manager)
#     # Удаление задачи и повторный вывод
#     print(manager.remove_task("поесть"))
#     print("\nПосле удаления задачи:")
#     print(manager)
#
#
# main()
