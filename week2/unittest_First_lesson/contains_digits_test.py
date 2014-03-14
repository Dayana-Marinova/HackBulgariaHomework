import contains_digits
import unittest


class ContainsDigitsTest(unittest.TestCase):
    def test_contains_digits1(self):
        self.assertEqual(True, contains_digits.contains_digits(10001, [0, 1]))

    def test_contains_digits2(self):
        self.assertEqual(True, contains_digits.contains_digits(123332, [2, 1]))

    def test_contains_digits3(self):
        self.assertEqual(False, contains_digits.contains_digits(0000, [1, 5]))

    def test_contains_digits4(self):
        self.assertEqual(False, contains_digits.contains_digits(3464, [4, 5]))

    def test_contains_digits5(self):
        self.assertEqual(False, contains_digits.contains_digits(42, [1, 5]))

if __name__ == '__main__':
    unittest.main()
