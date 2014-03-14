import sort_fractions
import unittest


class SortFractionsTest(unittest.TestCase):
    def test_sort_fractions1(self):
        self.assertEqual([(1, 2), (2, 3)], sort_fractions.sort_fractions([(2, 3), (1, 2)]))

    def test_sort_fractions2(self):
        self.assertEqual([(1, 3), (1, 2), (2, 3)], sort_fractions.sort_fractions([(2, 3), (1, 2), (1, 3)]))

    def test_sort_fractions3(self):
        self.assertEqual([(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)],sort_fractions.sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))

    def test_sort_fractions4(self):
        self.assertEqual([(1, 100), (1, 50), (1,25), (1, 5), (1, 1)], sort_fractions.sort_fractions([(1, 25), (1, 100), (1, 1), (1, 50), (1, 5)]))


    def test_sort_fractions5(self):
        self.assertEqual([(1, 1), (2, 1), (3, 1)], sort_fractions.sort_fractions([(2, 1), (3, 1), (1, 1)]))


if __name__ == '__main__':
    unittest.main()
