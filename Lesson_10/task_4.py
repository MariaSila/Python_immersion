# Задание №4
# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
#   ○ шестизначный идентификационный номер
#   ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
class Human:
    def __init__(self, fio, age):
        self._age = age
        self.fio = fio

    def get_age(self):
        return self._age

    def birthday(self):
        self._age += 1

    def full_name(self):
        return f'{self.fio=}'


class Worker(Human):
    MAX_LEVEL = 7
    MIN_ID = 100_000
    MAX_ID = 999_999

    def __init__(self, user_id, fio, age):
        super().__init__(fio, age)
        if user_id < self.MIN_ID or user_id > self.MAX_ID:
            self.user_id = self.MIN_ID
        else:
            self.user_id = user_id

    def access(self):
        user_id_str = str(self.user_id)
        s = sum(int(num) for num in user_id_str)
        print(self.user_id)
        return s % self.MAX_LEVEL


if __name__ == '__main__':
    worker = Worker(999999, 'Petr Petrov', 44)
    print(worker.access())
