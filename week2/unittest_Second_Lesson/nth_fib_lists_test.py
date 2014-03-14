import nth_fib_lists
import unittest


class FiboncciListCountTest(unittest.TestCase):
    def test_nth_fib_lists1(self):
        self.assertEqual([], nth_fib_lists.nth_fib_lists([], [], 100))

    def test_nth_fib_lists2(self):
        self.assertEqual([1, 2, 3, 4, 3, 4, 1, 2, 3, 4], nth_fib_lists.nth_fib_lists([1, 2], [3, 4], 4))

    def test_nth_fib_lists3(self):
        self.assertEqual([1, 2, 3], nth_fib_lists.nth_fib_lists([1, 2, 3], [4, 5, 6], 1))

    def test_nth_fib_lists4(self):
        self.assertEqual([4, 5, 6], nth_fib_lists.nth_fib_lists([1, 2, 3], [4, 5, 6], 2))

    def test_nth_fib_lists5(self):
        self.assertEqual([4, 5, 6, 1, 2, 3, 4, 5, 6], nth_fib_lists.nth_fib_lists([1, 2, 3], [4, 5, 6], 3))


if __name__ == '__main__':
    unittest.main()
