# Задача 4. Счетчик Очков в Игрe
# Создайте класс GameScore для отслеживания очков игрока. В этом классе
# должны быть методы для добавления и уменьшения очков. Однако:
#       ● Очки не могут быть отрицательными.
#       ● Если игрок пытается добавить больше очков, чем 1000, должно быть
#           выброшено исключение ScoreLimitExceededError.
# Создайте пользовательское исключение ScoreLimitExceededError.
# Подсказка № 1
#   Создайте пользовательское исключение. Определите класс
#   ScoreLimitExceededError, который наследует от Exception. В конструкторе этого
#   класса задайте сообщение об ошибке, которое будет отображаться при выбросе исключения.
# Подсказка № 2
#   Реализуйте метод add_score. В методе add_score класса GameScore проверьте, не
#   превышает ли новая сумма очков допустимый лимит (1000). Если превышает,
#   выбросите исключение ScoreLimitExceededError.
# Подсказка № 3
#   Реализуйте метод subtract_score. В методе subtract_score проверьте, чтобы после
#   вычитания очков не образовался отрицательный результат. Если это произойдет,
#   выбросите стандартное исключение ValueError с соответствующим сообщением.
# Подсказка № 4
#   В основном блоке программы используйте конструкцию try-except для обработки
#   исключений, выбрасываемых методами add_score и subtract_score. Выведите
#   соответствующее сообщение об ошибке, чтобы пользователь понял, что произошло

class ScoreLimitExceededError(Exception):
    def __str__(self):
        return f'Ошибка! Количество очков не должно превышать 1000'


class GameScore:
    MAX_VALUE = 1000

    def __init__(self, name, score=None):
        self.name = name
        self.score = 0 if score is None else score

    def add_score(self, value):
        if self.score + value > self.MAX_VALUE:
            raise ScoreLimitExceededError
        self.score += value
        return self.score

    def subtract_score(self, value):
        if self.score - value < 0:
            raise ValueError('Ошибка! Вы достигли отрицательного значения очков.')
        self.score -= value
        return self.score


if __name__ == '__main__':
    game = GameScore('Шашки')
    try:
        print(f'Счет {game.add_score(100)}')
        print(f'Счет {game.add_score(500)}')
        print(f'Счет {game.add_score(600)}')
    except ScoreLimitExceededError as e_add:
        print(e_add)

    try:
        print(f'Счет {game.subtract_score(100)}')
        print(f'Счет {game.subtract_score(100)}')
        print(f'Счет {game.subtract_score(100)}')
    except ValueError as e_sub:
        print(e_sub)

    try:
        print(f'Счет {game.subtract_score(400)}')
    except ValueError as e_sub:
        print(e_sub)


# PERFECT SOLUTION
# class ScoreLimitExceededError(Exception):
#     """Исключение, выбрасываемое при попытке добавить очки,
#     превышающие лимит."""
#     def __init__(self):
#         super().__init__("Очки не могут быть больше 1000.")
#
#
# class GameScore:
#     """Класс для отслеживания очков игрока с ограничениями."""
#     def __init__(self):
#         """Инициализирует начальное значение очков."""
#         self.score = 0
#
#     def add_score(self, points):
#         """Добавляет очки к текущему счету, проверяя лимит."""
#         if self.score + points > 1000:
#             raise ScoreLimitExceededError()
#         self.score += points
#
#     def subtract_score(self, points):
#         """Уменьшает очки, проверяя, чтобы счет не стал
#         отрицательным."""
#         if self.score - points < 0:
#             raise ValueError("Очки не могут быть отрицательными.")
#         self.score -= points
#
#
# # Пример использования класса GameScore:
# game_score = GameScore()
# try:
#     # Добавляем 500 очков
#     game_score.add_score(500)
#     print(f"Текущий счет: {game_score.score}")
#     # Пытаемся добавить еще 600 очков, что вызовет исключение
#     game_score.add_score(600)
# except ScoreLimitExceededError as e:
#     print(e)
# except ValueError as e:
#     print(e)
#
# try:
#     # Пытаемся вычесть больше очков, чем есть
#     game_score.subtract_score(600)
# except ValueError as e:
#     print(e)
#
# # Проверка работы метода subtract_score
# try:
#     game_score.subtract_score(100)
#     print(f"Текущий счет после вычитания: {game_score.score}")
# except ValueError as e:
#     print(e)


