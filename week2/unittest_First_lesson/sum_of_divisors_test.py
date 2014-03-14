import sum_of_divisors
import unittest


class SumOfDivisorsTest(unittest.TestCase):
    def test_sum_of_divisors1(self):
        self.assertEqual(28, sum_of_divisors.sum_of_divisors(12))

    def test_sum_of_divisors2(self):
        self.assertEqual(93, sum_of_divisors.sum_of_divisors(50))

    def test_sum_of_divisors3(self):
        self.assertEqual(217, sum_of_divisors.sum_of_divisors(100))

    def test_sum_of_divisors4(self):
        self.assertEqual(18, sum_of_divisors.sum_of_divisors(17))

    def test_sum_of_divisors5(self):
        self.assertEqual(156, sum_of_divisors.sum_of_divisors(99))

if __name__ == '__main__':
    unittest.main()
