import is_prime
import unittest


class CalculatorTest(unittest.TestCase):
    def test_is_prime1(self):
        self.assertEqual(False, is_prime.is_prime(12))

    def test_is_prime2(self):
        self.assertEqual(False, is_prime.is_prime(50))

    def test_is_prime3(self):
        self.assertEqual(True, is_prime.is_prime(2))

    def test_is_prime4(self):
        self.assertEqual(True, is_prime.is_prime(17))

    def test_is_prime5(self):
        self.assertEqual(False, is_prime.is_prime(99))

if __name__ == '__main__':
    unittest.main()
