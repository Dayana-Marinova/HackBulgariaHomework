import solution
import unittest


class GroupbyTest(unittest.TestCase):
    def test_groupby1(self):
        self.assertEqual({"big": [35, 40, 45], "small": [0, 5, 10, 15, 20, 25, 30]}, solution.groupby(lambda x: 'big' if x > 30 else 'small', range(0, 50, 5)))

    def test_groupby2(self):
        self.assertEqual({0: [0, 2, 4, 6], 1: [1, 3, 5, 7]}, solution.groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]))

    def test_groupby3(self):
        self.assertEqual({}, solution.groupby(lambda x: x, []))

    def test_groupby4(self):
        self.assertEqual({0: [0, 3, 6], 1: [1, 4, 7], 2: [2, 5]}, solution.groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]))

    def test_groupby5(self):
        self.assertEqual({"odd": [1, 3, 5, 9], "even": [2, 8, 10, 12]}, solution.groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]))


if __name__ == '__main__':
    unittest.main()
