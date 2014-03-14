import is_decreasing
import unittest


class IsDecreasingTest(unittest.TestCase):
    def test_is_decreasing1(self):
        self.assertEqual(True, is_decreasing.is_decreasing([5, 4, 3, 2, 1]))

    def test_is_decreasing2(self):
        self.assertEqual(True, is_decreasing.is_decreasing([100, 50, 20]))

    def test_is_decreasing3(self):
        self.assertEqual(False, is_decreasing.is_decreasing([10, 5, 10]))

    def test_is_decreasing4(self):
        self.assertEqual(False, is_decreasing.is_decreasing([1, 2, 3, 4]))

    def test_is_decreasing5(self):
        self.assertEqual(True, is_decreasing.is_decreasing([2, 2, 2, 2]))

if __name__ == '__main__':
    unittest.main()
