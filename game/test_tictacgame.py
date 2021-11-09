import unittest
from game import TicTacGame
from exceptions import ValidatedError, HasOwnerError


class TestTicTacGame(unittest.TestCase):
    """Класс для написания тестов для класса TicTacGame"""

    def setUp(self) -> None:
        self.game = TicTacGame()

    def test_validation_positive(self):
        answer = self.game.validation("1")
        self.assertTrue(answer)

    def test_validation_negative(self):
        """Проверка неверной валидации"""

        with self.assertRaises(ValidatedError):
            self.game.validation("r")

        with self.assertRaises(ValidatedError):
            self.game.validation("12")

        with self.assertRaises(ValidatedError):
            self.game.validation("-1")

        with self.assertRaises(ValidatedError):
            self.game.validation(" ")

    def test_hasnot_owner_positive(self):
        answer = self.game.hasnot_owner(1)
        self.assertTrue(answer)

    def test_hasnot_owner_negative(self):
        """тест проверки вторичной записи в ячейку"""
        self.game.board[0] = 'X'
        with self.assertRaises(HasOwnerError):
            self.game.hasnot_owner(1)

    def test_check_win(self):
        """тест выигрышных комбинаций"""
        self.game.board[0] = "X"
        self.game.board[1] = "X"
        self.game.board[2] = "X"
        self.assertTrue(self.game.check_win(self.game.board))
