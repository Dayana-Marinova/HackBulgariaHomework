import solution
import unittest


class ContainsDigitTest(unittest.TestCase):
    def test_contains_digit1(self):
        self.assertEqual(True, solution.contains_digit(10001, 1))

    def test_contains_digit2(self):
        self.assertEqual(True, solution.contains_digit(1233321, 2))

    def test_contains_digit3(self):
        self.assertEqual(False, solution.contains_digit(000000, 10))

    def test_contains_digit4(self):
        self.assertEqual(False, solution.contains_digit(1234666432, 5))

    def test_contains_digit5(self):
        self.assertEqual(False, solution.contains_digit(42, 3))

if __name__ == '__main__':
    unittest.main()
    