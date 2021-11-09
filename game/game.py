from typing import List
from exceptions import ValidatedError, HasOwnerError


class TicTacGame:
    def __init__(self) -> None:
        self.board = list(map(str, range(1, 10)))
        self.wins_coord = [(1, 2, 3), (4, 5, 6), (7, 8, 9),
                           (1, 5, 9), (3, 5, 7), (1, 4, 7), (2, 5, 8), (3, 6, 9)]

    def draw_board(self):
        """Метод для отрисовки игрового поля"""
        print("---------")
        for i in range(3):
            print("|", self.board[0+i*3],
                  self.board[1+i*3], self.board[2+i*3], "|")
        print("---------")

    def validation(self, value: str) -> bool:
        """Метод для валидации ввода пользователя"""
        if len(value) > 1:
            raise ValidatedError(
                "Введено неправильное значение, повторите ввод")
        if not (value in "123456789"):
            raise ValidatedError("Введено неправильное значение, повторите")
        if value == '':
            raise ValidatedError("Введено пустое значение, повторите")
        return True

    def hasnot_owner(self, value: int) -> bool:
        """Метод для проверки занятости той или иной клетки"""
        if str(self.board[value - 1]) in 'XO':
            raise HasOwnerError("Данная клетка уже занята")
        return True

    def setTheValue(self, player_name: str):
        """Метод игры реализующий запоминание ходов игроков"""
        while True:
            try:
                value = input("Ходит игрок" + " " +
                              player_name + ". Назовите ячейку; ")
                self.validation(value)
                value = int(value)
                self.hasnot_owner(value)
                self.board[value-1] = player_name
                break
            except ValidatedError as e:
                print(e)
            except HasOwnerError as e:
                print(e)

    def check_win(self, board: List[str]):
        """Метод для проверки выигрышных комбинаций в wins_coord"""
        for each in self.wins_coord:
            if (board[each[0] - 1]) == (board[each[1]-1]) == (board[each[2]-1]):
                return board[each[1]-1]
        else:
            return False

    def start(self):
        """Метод для старта игры и ведения подсчёта ходов"""
        counter = 0

        while True:
            self.draw_board()
            if counter % 2 == 0:
                self.setTheValue('X')
            else:
                self.setTheValue('O')
            if counter > 3:
                winner = self.check_win(self.board)
                if winner:
                    self.draw_board()
                    print(winner, "выиграл")
                    break
            counter += 1
            if counter > 8:
                self.draw_board()
                print("ничья")
                break
