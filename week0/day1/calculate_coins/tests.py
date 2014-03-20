import solution
import unittest


class CalculateCoinsTest(unittest.TestCase):
    def test_calculate_coins1(self):
        self.assertEqual({1: 1, 2: 1, 100: 0, 5: 0, 10: 0, 50: 1, 20: 0}, solution.calculate_coins(0.53))

    def test_calculate_coins2(self):
        self.assertEqual({1: 0, 2: 2, 100: 8, 5: 0, 10: 0, 50: 1, 20: 2}, solution.calculate_coins(8.94))

    def test_calculate_coins3(self):
        self.assertEqual({1: 0, 2: 2, 100: 7, 5: 0, 10: 0, 50: 0, 20: 1}, solution.calculate_coins(7.24))

    def test_calculate_coins4(self):
        self.assertEqual({1: 1, 2: 1, 100: 3, 5: 0, 10: 0, 50: 1, 20: 1}, solution.calculate_coins(3.73))

    def test_calculate_coins5(self):
        self.assertEqual({1: 0, 2: 1, 100: 0, 5: 1, 10: 0, 50: 1, 20: 2}, solution.calculate_coins(0.97))

if __name__ == '__main__':
    unittest.main()
