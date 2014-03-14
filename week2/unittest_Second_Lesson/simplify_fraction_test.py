import simplify_fraction
import unittest


class FractionTest(unittest.TestCase):
    def test_simplify_fraction1(self):
        self.assertEqual((3, 13), simplify_fraction.simplify_fraction((18, 78)))

    def test_simplify_fraction2(self):
        self.assertEqual((12, 109), simplify_fraction.simplify_fraction((12, 109)))

    def test_simplify_fraction3(self):
        self.assertEqual((28, 289), simplify_fraction.simplify_fraction((56, 578)))

    def test_simplify_fraction4(self):
        self.assertEqual((3, 25), simplify_fraction.simplify_fraction((12, 100)))

    def test_simplify_fraction5(self):
        self.assertEqual("we can not divide by zero", simplify_fraction.simplify_fraction((0, 1)))

    def test_simplify_fraction6(self):
        self.assertEqual((0, 0), simplify_fraction.simplify_fraction((9, 0)))

if __name__ == '__main__':
    unittest.main()
