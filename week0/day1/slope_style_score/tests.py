import solution
import unittest


class SlopeScoreTest(unittest.TestCase):
    def test_slope_style_score1(self):
        self.assertEqual(94.67, solution.slope_style_score([94, 95, 95, 95, 90]))

    def test_slope_style_score2(self):
        self.assertEqual(93.5, solution.slope_style_score([96, 95.5, 93, 89, 92]))

    def test_slope_style_score3(self):
        self.assertEqual(4, solution.slope_style_score([1, 2, 3, 4, 5, 6, 7]))

    def test_slope_style_score4(self):
        self.assertEqual(10, solution.slope_style_score([10, 10, 1]))

    def test_slope_style_score5(self):
        self.assertEqual(2, solution.slope_style_score([1, 2, 3]))

if __name__ == '__main__':
    unittest.main()
