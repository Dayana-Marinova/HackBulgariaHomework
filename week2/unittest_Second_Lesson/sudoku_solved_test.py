import sudoku_solved
import unittest


class SudokuTest(unittest.TestCase):
    def test_sudoku_solved1(self):
        self.assertEqual(True, sudoku_solved.sudoku_solved([
            [4, 5, 2, 3, 8, 9, 7, 1, 6],
            [3, 8, 7, 4, 6, 1, 2, 9, 5],
            [6, 1, 9, 2, 5, 7, 3, 4, 8],
            [9, 3, 5, 1, 2, 6, 8, 7, 4],
            [7, 6, 4, 9, 3, 8, 5, 2, 1],
            [1, 2, 8, 5, 7, 4, 6, 3, 9],
            [5, 7, 1, 8, 9, 2, 4, 6, 3],
            [8, 9, 6, 7, 4, 3, 1, 5, 2],
            [2, 4, 3, 6, 1, 5, 9, 8, 7]
        ]))

    def test_sudoku_solved2(self):
        self.assertEqual(False, sudoku_solved.sudoku_solved([
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ]))

    def test_sudoku_solved3(self):
        self.assertEqual(False, sudoku_solved.sudoku_solved([
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [2, 2, 2, 2, 2, 2, 2, 2, 2],
            [3, 3, 3, 3, 3, 3, 3, 3, 3],
            [4, 4, 4, 4, 4, 4, 4, 4, 4],
            [5, 5, 5, 5, 5, 5, 5, 5, 5],
            [6, 6, 6, 6, 6, 6, 6, 6, 6],
            [7, 7, 7, 7, 7, 7, 7, 7, 7],
            [8, 8, 8, 8, 8, 8, 8, 8, 8],
            [9, 9, 9, 9, 9, 9, 9, 9, 9]
        ]))


if __name__ == '__main__':
    unittest.main()