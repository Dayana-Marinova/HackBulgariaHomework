import prime_factorization
import unittest


class CalculatorTest(unittest.TestCase):
    def test_prime_factorization1(self):
        self.assertEqual({2: 2, 5: 1}, prime_factorization.prime_factorization(20))

    def test_prime_factorization2(self):
        self.assertEqual({2: 2, 89: 1}, prime_factorization.prime_factorization(356))

    def test_prime_factorization3(self):
        self.assertEqual({2: 1, 5: 1}, prime_factorization.prime_factorization(10))

    def test_prime_factorization4(self):
        self.assertEqual({89: 1}, prime_factorization.prime_factorization(89))

    def test_prime_factorization5(self):
        self.assertEqual({2: 3, 5: 3}, prime_factorization.prime_factorization(1000))

if __name__ == '__main__':
    unittest.main()
