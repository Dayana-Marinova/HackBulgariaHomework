import what_is_my_sign
import unittest


class CalculatorTest(unittest.TestCase):
    def test_what_is_my_sign1(self):
        self.assertEqual('Libra', what_is_my_sign.what_is_my_sign(22, 10))

    def test_what_is_my_sign2(self):
        self.assertEqual('Scorpio', what_is_my_sign.what_is_my_sign(4, 11))

    def test_what_is_my_sign3(self):
        self.assertEqual('Capricorn', what_is_my_sign.what_is_my_sign(1, 1))

    def test_what_is_my_sign4(self):
        self.assertEqual('Aquarius', what_is_my_sign.what_is_my_sign(31, 1))

    def test_what_is_my_sign5(self):
        self.assertEqual('Pisces', what_is_my_sign.what_is_my_sign(20, 3))

    def test_what_is_my_sign6(self):
        self.assertEqual('Virgo', what_is_my_sign.what_is_my_sign(30, 8))

if __name__ == '__main__':
    unittest.main()
