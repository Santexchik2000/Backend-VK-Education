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

        answer = self.game.validation("2")
        self.assertTrue(answer)
        
        answer = self.game.validation("3")
        self.assertTrue(answer)
        
        answer = self.game.validation("4")
        self.assertTrue(answer)

        answer = self.game.validation("5")
        self.assertTrue(answer)

        answer = self.game.validation("6")
        self.assertTrue(answer)
        
        answer = self.game.validation("7")
        self.assertTrue(answer)

        answer = self.game.validation("8")
        self.assertTrue(answer)

        answer = self.game.validation("9")
        self.assertTrue(answer)

    def test_validation_negative(self):
        """Проверка неверной валидации"""
        
        with self.assertRaises(ValidatedError):
            self.game.validation("r")

        with self.assertRaises(ValidatedError):
            self.game.validation("0")

        with self.assertRaises(ValidatedError):
            self.game.validation("10")

        with self.assertRaises(ValidatedError):
            self.game.validation("12")

        with self.assertRaises(ValidatedError):
            self.game.validation("-1")

        with self.assertRaises(ValidatedError):
            self.game.validation(" ")

        with self.assertRaises(ValidatedError):
            self.game.validation("-")

        with self.assertRaises(ValidatedError):
            self.game.validation("$")

    def test_hasnot_owner_positive(self):
        answer = self.game.hasnot_owner(1)
        self.assertTrue(answer)

    def test_hasnot_owner_negative(self):
        """тест проверки вторичной записи в ячейку"""
        self.game.board[0] = 'X'
        with self.assertRaises(HasOwnerError):
            self.game.hasnot_owner(1)

    def test_check_win_first_for_x(self):
        """тест выигрышных комбинаций"""
        self.game.board[0] = "X"
        self.game.board[1] = "X"
        self.game.board[2] = "X"
        self.assertTrue(self.game.check_win(self.game.board))
        
    def test_check_win_second_for_x(self):
        """тест выигрышных комбинаций"""
        self.game.board[3] = "X"
        self.game.board[4] = "X"
        self.game.board[5] = "X"
        self.assertTrue(self.game.check_win(self.game.board))

    def test_check_win_third_for_x(self):
        """тест выигрышных комбинаций"""
        self.game.board[6] = "X"
        self.game.board[7] = "X"
        self.game.board[8] = "X"
        self.assertTrue(self.game.check_win(self.game.board))
        
    def test_check_win_fourth_for_x(self):
        """тест выигрышных комбинаций"""
        self.game.board[0] = "X"
        self.game.board[4] = "X"
        self.game.board[8] = "X"
        self.assertTrue(self.game.check_win(self.game.board))

    def test_check_win_fifth_for_x(self):
        """тест выигрышных комбинаций"""
        self.game.board[2] = "X"
        self.game.board[4] = "X"
        self.game.board[6] = "X"
        self.assertTrue(self.game.check_win(self.game.board))

    def test_check_win_sixth_for_x(self):
        """тест выигрышных комбинаций"""
        self.game.board[0] = "X"
        self.game.board[3] = "X"
        self.game.board[6] = "X"
        self.assertTrue(self.game.check_win(self.game.board))

    def test_check_win_seventh_for_x(self):
        """тест выигрышных комбинаций"""
        self.game.board[1] = "X"
        self.game.board[4] = "X"
        self.game.board[7] = "X"
        self.assertTrue(self.game.check_win(self.game.board))

    def test_check_win_eighth_for_x(self):
        """тест выигрышных комбинаций"""
        self.game.board[2] = "X"
        self.game.board[5] = "X"
        self.game.board[8] = "X"
        self.assertTrue(self.game.check_win(self.game.board))

    def test_check_win_first_for_o(self):
        """тест выигрышных комбинаций"""
        self.game.board[0] = "Y"
        self.game.board[1] = "Y"
        self.game.board[2] = "Y"
        self.assertTrue(self.game.check_win(self.game.board))
        
    def test_check_win_second_for_o(self):
        """тест выигрышных комбинаций"""
        self.game.board[3] = "O"
        self.game.board[4] = "O"
        self.game.board[5] = "O"
        self.assertTrue(self.game.check_win(self.game.board))

    def test_check_win_third_for_o(self):
        """тест выигрышных комбинаций"""
        self.game.board[6] = "O"
        self.game.board[7] = "O"
        self.game.board[8] = "O"
        self.assertTrue(self.game.check_win(self.game.board))
        
    def test_check_win_fourth_for_o(self):
        """тест выигрышных комбинаций"""
        self.game.board[0] = "O"
        self.game.board[4] = "O"
        self.game.board[8] = "O"
        self.assertTrue(self.game.check_win(self.game.board))

    def test_check_win_fifth_for_o(self):
        """тест выигрышных комбинаций"""
        self.game.board[2] = "O"
        self.game.board[4] = "O"
        self.game.board[6] = "O"
        self.assertTrue(self.game.check_win(self.game.board))

    def test_check_win_sixth_for_o(self):
        """тест выигрышных комбинаций"""
        self.game.board[0] = "O"
        self.game.board[3] = "O"
        self.game.board[6] = "O"
        self.assertTrue(self.game.check_win(self.game.board))

    def test_check_win_seventh_for_o(self):
        """тест выигрышных комбинаций"""
        self.game.board[1] = "O"
        self.game.board[4] = "O"
        self.game.board[7] = "O"
        self.assertTrue(self.game.check_win(self.game.board))

    def test_check_win_eighth_for_o(self):
        """тест выигрышных комбинаций"""
        self.game.board[2] = "O"
        self.game.board[5] = "O"
        self.game.board[8] = "O"
        self.assertTrue(self.game.check_win(self.game.board))
    
    def test_check_draw_first(self):
        self.game.board[0] = "X"
        self.game.board[1] = "O"
        self.game.board[2] = "X"
        self.game.board[3] = "X"
        self.game.board[4] = "X"
        self.game.board[5] = "O"
        self.game.board[6] = "O"
        self.game.board[7] = "X"
        self.game.board[8] = "O"
        self.assertFalse(self.game.check_win(self.game.board))#возвращает False

    def test_check_draw_second(self):
        self.game.board[0] = "O"
        self.game.board[1] = "X"
        self.game.board[2] = "X"
        self.game.board[3] = "X"
        self.game.board[4] = "X"
        self.game.board[5] = "O"
        self.game.board[6] = "O"
        self.game.board[7] = "O"
        self.game.board[8] = "X"
        self.assertFalse(self.game.check_win(self.game.board))#возвращает False
