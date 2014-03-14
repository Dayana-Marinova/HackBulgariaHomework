import slope_style_score
import unittest


class CalculatorTest(unittest.TestCase):
    def test_slope_style_score1(self):
        self.assertEqual(94.67, slope_style_score.slope_style_score([94, 95, 95, 95, 90]))

    def test_slope_style_score2(self):
        self.assertEqual(93.5, slope_style_score.slope_style_score([96, 95.5, 93, 89, 92]))

    def test_slope_style_score3(self):
        self.assertEqual(4, slope_style_score.slope_style_score([1, 2, 3, 4, 5, 6, 7]))

    def test_slope_style_score4(self):
        self.assertEqual(10, slope_style_score.slope_style_score([10, 10, 1]))

    def test_slope_style_score5(self):
        self.assertEqual(2, slope_style_score.slope_style_score([1, 2, 3]))

if __name__ == '__main__':
    unittest.main()
