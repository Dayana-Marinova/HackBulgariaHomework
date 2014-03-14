import prime_number_of_divisors
import unittest


class PrimeNumberOfDivisorsTest(unittest.TestCase):
    def test_prime_number_of_divisors1(self):
        self.assertEqual(False, prime_number_of_divisors.prime_number_of_divisors(12))

    def test_prime_number_of_divisors2(self):
        self.assertEqual(True, prime_number_of_divisors.prime_number_of_divisors(7))

    def test_prime_number_of_divisors3(self):
        self.assertEqual(True, prime_number_of_divisors.prime_number_of_divisors(9))

    def test_prime_number_of_divisors4(self):
        self.assertEqual(False, prime_number_of_divisors.prime_number_of_divisors(8))

    def test_prime_number_of_divisors5(self):
        self.assertEqual(False, prime_number_of_divisors.prime_number_of_divisors(99))

if __name__ == '__main__':
    unittest.main()
