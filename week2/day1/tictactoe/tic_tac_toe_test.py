import tic_tac_toe
import unittest


class CalculatorTest(unittest.TestCase):
    def test_who_win_X(self):
        table = [
            ['X', 'X', 'X'],
            ['X', 'O', 'O'],
            ['O', 'O', 'X']
        ]
        self.assertEqual('X wins', tic_tac_toe.who_win(table))

    def test_who_win_O(self):
        table = [
            ['X', 'X', 'O'],
            ['X', 'O', 'O'],
            ['O', 'X', 'X']
        ]
        self.assertEqual('O wins', tic_tac_toe.who_win(table))

    def test_who_win_drawn(self):
        table = [
            ['X', 'O', 'X'],
            ['X', 'O', 'O'],
            ['O', 'X', 'X']
        ]
        self.assertEqual('nobody wins', tic_tac_toe.who_win(table))

    def test_who_win_not_all(self):
        table = [
            ['X', 'X', 'X'],
            ['O', 'O', '_'],
            ['_', '_', '_']
        ]
        self.assertEqual('X wins', tic_tac_toe.who_win(table))

    def test_who_win_X_col(self):
        table = [
            ['X', 'X', 'O'],
            ['X', 'O', 'O'],
            ['X', '_', '_']
        ]
        self.assertEqual('X wins', tic_tac_toe.who_win(table))

if __name__ == '__main__':
    unittest.main()
