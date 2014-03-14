import fibonacci
import unittest


class FibonacciTest(unittest.TestCase):
    def test_fibonacci_1(self):
        self.assertEqual(1, fibonacci.nth_fibonacci(1))

    def test_fibonacci_2(self):
        self.assertEqual(1, fibonacci.nth_fibonacci(2))

    def test_fibonacci_8(self):
        self.assertEqual(21, fibonacci.nth_fibonacci(8))

    def test_fibonacci_14(self):
        self.assertEqual(377, fibonacci.nth_fibonacci(14))

    def test_fibonacci_100(self):
        self.assertEqual(354224848179261915075, fibonacci.nth_fibonacci(100))

if __name__ == '__main__':
    unittest.main()
