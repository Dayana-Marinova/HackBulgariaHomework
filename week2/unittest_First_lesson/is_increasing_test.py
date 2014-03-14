import is_increasing
import unittest


class IsIncreasingTest(unittest.TestCase):
    def test_is_increasing1(self):
        self.assertEqual(True, is_increasing.is_increasing([0, 1, 2, 3]))

    def test_is_increasing2(self):
        self.assertEqual(False, is_increasing.is_increasing([2, 1]))

    def test_is_increasing3(self):
        self.assertEqual(False, is_increasing.is_increasing([1, 5, -10]))

    def test_is_increasing4(self):
        self.assertEqual(True, is_increasing.is_increasing([4, 5, 50, 200]))

    def test_is_increasing5(self):
        self.assertEqual(True, is_increasing.is_increasing([1, 5, 5]))

if __name__ == '__main__':
    unittest.main()
