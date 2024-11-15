# Задача 3. Крестики-нолики
# Создайте программу, которая реализует игру «Крестики-нолики».
# Для этого напишите:
#   1. Класс, который будет описывать поле игры. class Board:
#       # Класс поля, который создаёт у себя экземпляры клетки.
#       # Пусть класс хранит информацию о состоянии поля (это может быть список из девяти элементов).
#       # Помимо этого, класс должен содержать методы:
#               # «Изменить состояние клетки». Метод получает номер клетки и, если клетка не
#                   занята, меняет её состояние. Если состояние удалось изменить, метод возвращает
#                   True, иначе возвращается False.
#               # «Проверить окончание игры». Метод не получает входящих данных, но возвращает True/False.
#                   True — если один из игроков победил, False — если победителя нет.
#   2. Класс, который будет описывать одну клетку поля: class Cell:
#       # Клетка, у которой есть значения:
#               # занята она или нет;
#               # номер клетки;
#               # символ, который клетка хранит (пустая, крестик, нолик).
#   3. Класс, который описывает поведение игрока: class Player:
#       # У игрока может быть:
#               # имя,
#               # количество побед.
#               # Класс должен содержать метод:
#               # «Сделать ход». Метод ничего не принимает и возвращает ход игрока (номер
#                   клетки). Введённый номер нужно обязательно проверить.
#   4. Класс, который управляет ходом игры: class Game:
#       # класс «Игры» содержит атрибуты:
#               # состояние игры,
#               # игроки,
#               # поле.
#       # А также методы:
#               # Метод запуска одного хода игры. Получает одного из игроков, запрашивает у
#                   игрока номер клетки, изменяет поле, проверяет, выиграл ли игрок. Если игрок победил,
#                   возвращает True, иначе False.
#               # Метод запуска одной игры. Очищает поле, запускает цикл с игрой, который
#                   завершается победой одного из игроков или ничьей. Если игра завершена, метод
#                   возвращает True, иначе False.
#               # Основной метод запуска игр. В цикле запускает игры, запрашивая после каждой
#                   игры, хотят ли игроки продолжать играть. После каждой игры выводится текущий счёт игроков.
# Подсказка № 1
#   Начните с создания класса Cell, который будет хранить номер клетки, символ (крестик, нолик или пустое значение),
#   и состояние занятости клетки. Это позволит каждой клетке иметь своё собственное состояние.
# Подсказка № 2
#   Создайте класс Board, который содержит список из 9 объектов Cell. Этот список будет представлять игровое поле.
# Подсказка № 3
#   В классе Board создайте метод display_board, который будет выводить текущее состояние доски на экран.
#   Используйте простой цикл и форматирование строк для создания наглядного интерфейса.
# Подсказка № 4
#   Напишите метод в классе Board, который изменяет символ клетки, если она не занята. Метод должен проверять состояние
#   клетки перед изменением и возвращать True или False в зависимости от успеха операции.
# Подсказка № 5
#   В классе Board создайте метод check_game_over, который проверяет все возможные
#   победные комбинации. Если одна из них выполнена, метод должен возвращать True.
# Подсказка № 6
#   Создайте класс Player, который будет хранить имя игрока, его символ (X или O), и количество побед.
#   Также добавьте метод для запроса хода игрока.
# Подсказка № 7
#   Создайте класс Game, который будет управлять процессом игры. В этот класс включите
#   игроков и доску. Добавьте метод, который выполняет ход игрока и проверяет окончание игры.
# Подсказка № 8
#   В классе Game создайте метод play_one_game, который будет запускать одну партию. Этот метод должен очищать доску,
#   поочередно запрашивать ходы игроков и завершаться либо победой одного из игроков, либо ничьей.
# Подсказка № 9
#   Добавьте метод reset_board в класс Board, который будет сбрасывать состояние
#   всех клеток. Этот метод понадобится, чтобы начать новую партию с чистого листа.
# Подсказка № 10
#   В классе Game создайте основной метод start_games, который будет в цикле
#   запускать новые игры до тех пор, пока игроки хотят продолжать. Не забудьте добавить
#   возможность показа текущего счёта и сброса доски перед началом новой игры

def gen_combo_win(size):
    lst = [[i + j for j in range(int(size ** 0.5))] for i in range(1, size + 1, int(size ** 0.5))]
    lst_1 = [[i + j for j in range(1, size + 1, int(size ** 0.5))] for i in range(int(size ** 0.5))]
    lst_2 = [[i for i in range(1, size + 1, int(size ** 0.5) + 1)]]
    lst_3 = [[i for i in range(int(size ** 0.5), size, int(size ** 0.5) - 1)]]
    lst.extend(lst_1)
    lst.extend(lst_2)
    lst.extend(lst_3)
    return lst


class Cell():
    EMPTY = '_'

    def __init__(self, number):
        self.number = number
        self.free = True
        self.symbol = self.EMPTY

    def __repr__(self):
        return f'\nКлетка {self.number}, {self.free=}, {self.symbol=}'


class Board():
    SIZE_BOARD = 9
    list_win_combo = gen_combo_win(SIZE_BOARD)

    def __init__(self):
        self.list_cell = [Cell(i) for i in range(1, self.SIZE_BOARD + 1)]

    def change_state(self, player, num):
        state_cell = self.list_cell[num - 1]
        if state_cell.free:
            state_cell.free = False
            state_cell.symbol = player.token
            return True
        return False

    def check_game_over(self, player):
        for combo in self.list_win_combo:
            check = 0
            for num in combo:
                if not self.list_cell[num - 1].free and player.token == self.list_cell[num - 1].symbol:
                    check += 1
            if check == int(self.SIZE_BOARD ** 0.5):
                return True
        return False

    def is_draw(self):
        check = 0
        for cell in self.list_cell:
            if cell.free:
                check += 1
        if check == 0:
            print('Ничья')
            return True
        return False

    def reset_board(self):
        for cell in self.list_cell:
            cell.symbol = cell.EMPTY
            cell.free = True

    def display_board(self):
        for i in self.list_cell:
            res = f'{i.number} {i.symbol}'
            if i.number % 3 == 0:
                print(f'{res}')
            else:
                print(f'{res:<5}', end='')


class Player():
    ZERO = '0'
    CROSS = 'X'

    def __init__(self, name, token=None, win=0):
        self.name = name
        self.token = token
        self.win = win

    def move(self):
        num_cell = int(input(f'Ход {self.name}, введи номер клетки от 1 до 9: '))
        if not isinstance(num_cell, int) or num_cell > 9 or num_cell < 1:
            print('Некорректный ввод')
        return int(num_cell)

    def __repr__(self):
        return f'{self.name} : {self.win}'


class Game():
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.board = Board()
        self.score_game = [player_1, player_2]

    def play_one_move(self, player):
        self.board.display_board()
        flag = True
        while flag:
            num = player.move()
            if self.board.change_state(player, num):
                flag = False
            else:
                print('Клетка занята')
        else:
            if self.board.check_game_over(player):
                print(f'{player.name} выйграл')
                self.board.display_board()
                player.win += 1
                return True
            elif self.board.is_draw():
                return True
            return False

    def play_one_game(self):
        self.board.reset_board()
        flag = False
        while not flag:
            move_1 = self.play_one_move(self.player_1)
            if move_1:
                flag = True
                break
            move_2 = self.play_one_move(self.player_2)
            if move_2:
                flag = True
                break
        return flag

    def start_game(self):
        self.play_one_game()
        print(self.score_game)
        while True:
            answer = input('Еще партию? 1 - да, 0 - нет: ')
            match answer:
                case '1':
                    self.play_one_game()
                    print(self.score_game)
                case '0':
                    print(self.score_game)
                    return False


def main():
    pl_1 = Player('Player_X', 'X')
    pl_2 = Player('Player_O', 'O')

    game_1 = Game(pl_1, pl_2)
    game_1.start_game()


if __name__ == '__main__':
    main()


# # perfect solution
# class Cell:
#     def __init__(self, number):
#         self.number = number
#         self.symbol = " " # Символ клетки ('X', 'O' или пробел)
#         self.occupied = False # Статус занятости клетки
#
#
# class Board:
#     def __init__(self):
#         self.cells = [Cell(i) for i in range(1, 10)]  # Создаем 9 клеток для доски
#
#     def display_board(self):
#         """Отображает игровую доску."""
#         print("-------------")
#         for i in range(0, 9, 3):
#             print(f"| {self.cells[i].symbol} | {self.cells[i + 1].symbol} | {self.cells[i + 2].symbol} |")
#             print("-------------")
#
#     def change_cell(self, cell_number, symbol):
#         """Изменяет символ клетки, если она не занята."""
#         cell = self.cells[cell_number - 1]
#         if cell.occupied:
#             return False
#         cell.symbol = symbol
#         cell.occupied = True
#         return True
#
#     def check_game_over(self):
#         """Проверяет, завершена ли игра (выигрыш или ничья)."""
#         # Проверка строк, столбцов и диагоналей
#         win_positions = [
#             (0, 1, 2), (3, 4, 5), (6, 7, 8),  # горизонтальные линии
#             (0, 3, 6), (1, 4, 7), (2, 5, 8),  # вертикальные линии
#             (0, 4, 8), (2, 4, 6)  # диагонали
#         ]
#
#         for pos in win_positions:
#             if (self.cells[pos[0]].symbol != " " and
#                     self.cells[pos[0]].symbol == self.cells[pos[1]].symbol == self.cells[pos[2]].symbol):
#                 return True
#         return False
#
#     def reset_board(self):
#         """Сбрасывает игровую доску для новой игры."""
#         for cell in self.cells:
#             cell.symbol = " "
#             cell.occupied = False
#
#
# class Player:
#     def __init__(self, name, symbol):
#         self.name = name
#         self.symbol = symbol
#         self.wins = 0  # Количество побед игрока
#
#     def make_move(self):
#         """Запрашивает ход игрока и проверяет корректность ввода."""
#         while True:
#             try:
#                 move = int(input(f"{self.name}, введите номер клетки для вашего хода(1 - 9): "))
#                 if move < 1 or move > 9:
#                     raise ValueError
#                 return move
#             except ValueError:
#                 print("Неправильный ввод. Пожалуйста, введите число от 1 до 9.")
#
#
# class Game:
#     def __init__(self, player1, player2):
#         self.players = [player1, player2]
#         self.board = Board()
#
#     def launch_move(self, player):
#         """Выполняет ход текущего игрока."""
#         while True:
#             self.board.display_board()
#             cell_number = player.make_move()
#             if self.board.change_cell(cell_number, player.symbol):
#                 if self.board.check_game_over():
#                     return True
#                 return False
#             print("Клетка занята. Сделайте другой ход.")
#
#     def play_one_game(self):
#         """Проводит одну игру до победы одного из игроков или ничьи."""
#         print("Игра началась!")
#         while True:
#             for player in self.players:
#                 if self.launch_move(player):
#                     self.board.display_board()
#                     print(f"Поздравляем, {player.name}! Вы выиграли!")
#                     player.wins += 1
#                     return
#                 if all(cell.occupied for cell in self.board.cells):
#                         self.board.display_board()
#                         print("Ничья!")
#                         return
#
#     def start_games(self):
#         """Запускает серию игр с возможностью перезапуска."""
#         print("Добро пожаловать в игру Крестики-Нолики!")
#         while True:
#             self.board.reset_board()  # Сбрасываем доску для новой игры
#             self.play_one_game()
#             print(f"Счет: {self.players[0].name} - {self.players[0].wins}, "
#                   f"{self.players[1].name} - {self.players[1].wins}")
#             again = input("Хотите продолжить игру? (да/нет): ")
#             if again.lower() != 'да':
#                 print("Спасибо за игру!")
#                 break
#
#
# # Создаем двух игроков
# player1 = Player("Игрок 1", 'X')
# player2 = Player("Игрок 2", 'O')
# # Запускаем игру
# game = Game(player1, player2)
# game.start_games()