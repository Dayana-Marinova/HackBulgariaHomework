import solution
import unittest


class SumMinMaxTest(unittest.TestCase):
    def test_sum_of_min_and_max1(self):
        self.assertEqual(2, solution.sum_of_min_and_max([1]))

    def test_sum_of_min_and_max2(self):
        self.assertEqual(10, solution.sum_of_min_and_max([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test_sum_of_min_and_max3(self):
        self.assertEqual(0, solution.sum_of_min_and_max([0]))

    def test_sum_of_min_and_max4(self):
        self.assertEqual(1, solution.sum_of_min_and_max([0, 1]))

    def test_sum_of_min_and_max5(self):
        self.assertEqual(6, solution.sum_of_min_and_max([1, 2, -3, 9]))

if __name__ == '__main__':
    unittest.main()
