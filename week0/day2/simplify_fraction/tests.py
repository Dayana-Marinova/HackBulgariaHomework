import solution
import unittest


class FractionTest(unittest.TestCase):
    def test_simplify_fraction1(self):
        self.assertEqual((3, 13), solution.simplify_fraction((18, 78)))

    def test_simplify_fraction2(self):
        self.assertEqual((12, 109), solution.simplify_fraction((12, 109)))

    def test_simplify_fraction3(self):
        self.assertEqual((28, 289), solution.simplify_fraction((56, 578)))

    def test_simplify_fraction4(self):
        self.assertEqual((3, 25), solution.simplify_fraction((12, 100)))

    def test_simplify_fraction5(self):
        self.assertEqual("we can not divide by zero", solution.simplify_fraction((0, 1)))

    def test_simplify_fraction6(self):
        self.assertEqual((0, 0), solution.simplify_fraction((9, 0)))

if __name__ == '__main__':
    unittest.main()
