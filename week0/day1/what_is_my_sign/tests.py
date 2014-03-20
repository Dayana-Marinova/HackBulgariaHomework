import solution
import unittest


class MySingTest(unittest.TestCase):
    def test_what_is_my_sign1(self):
        self.assertEqual('Libra', solution.what_is_my_sign(22, 10))

    def test_what_is_my_sign2(self):
        self.assertEqual('Scorpio', solution.what_is_my_sign(4, 11))

    def test_what_is_my_sign3(self):
        self.assertEqual('Capricorn', solution.what_is_my_sign(1, 1))

    def test_what_is_my_sign4(self):
        self.assertEqual('Aquarius', solution.what_is_my_sign(31, 1))

    def test_what_is_my_sign5(self):
        self.assertEqual('Pisces', solution.what_is_my_sign(20, 3))

    def test_what_is_my_sign6(self):
        self.assertEqual('Virgo', solution.what_is_my_sign(30, 8))

if __name__ == '__main__':
    unittest.main()
