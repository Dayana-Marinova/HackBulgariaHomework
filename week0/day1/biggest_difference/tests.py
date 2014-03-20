import solution
import unittest


class BiggestDifferenceTest(unittest.TestCase):
    def test_biggest_difference1(self):
        self.assertEqual(-4, solution.biggest_difference([1, 2, 3, 4, 5]))

    def test_biggest_difference2(self):
        self.assertEqual(-9, solution.biggest_difference([-10, -9, -1]))

    def test_biggest_difference3(self):
        self.assertEqual(-99, solution.biggest_difference(range(100)))

    def test_biggest_difference4(self):
        self.assertEqual(-100, solution.biggest_difference(range(50, 151)))

    def test_biggest_difference5(self):
        self.assertEqual(-12, solution.biggest_difference(range(-10, 3)))

if __name__ == '__main__':
    unittest.main()
