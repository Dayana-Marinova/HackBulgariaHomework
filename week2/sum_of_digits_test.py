import sum_of_digits
import unittest


class CalculatorTest(unittest.TestCase):
    def test_fibonacci_123(self):
        self.assertEqual(6, sum_of_digits.sum_of_digits(-123))

    def test_fibonacci_79810(self):
        self.assertEqual(25, sum_of_digits.sum_of_digits(79810))

    def test_fibonacci_1000000(self):
        self.assertEqual(1, sum_of_digits.sum_of_digits(1000000))

    def test_fibonacci_377(self):
        self.assertEqual(17, sum_of_digits.sum_of_digits(377))

    def test_fibonacci_354224848179261915075(self):
        self.assertEqual(111, sum_of_digits.sum_of_digits(3542248485599278518291))

if __name__ == '__main__':
    unittest.main()
