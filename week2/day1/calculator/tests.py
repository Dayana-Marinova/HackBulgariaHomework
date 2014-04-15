import solution
import unittest


class CalculatorTest(unittest.TestCase):
    """Testing the very simple and trivial calculator module"""
    def test_add(self):
        self.assertEqual(5 + 6, solution.add(5, 6))

    def test_minus(self):
        self.assertEqual(5 - 6, solution.minus(5, 6))

    def test_multiply(self):
        self.assertEqual(5 * 5, solution.multiply(5, 5))

    def test_float_division(self):
        self.assertEqual(5 / 2, solution.float_division(5, 2))

    def test_integer_division(self):
        self.assertEqual(5 // 2, solution.integer_division(5, 2))

    def test_modulo(self):
        self.assertEqual(10 % 2, solution.modulo(10, 2))


if __name__ == '__main__':
    unittest.main()
