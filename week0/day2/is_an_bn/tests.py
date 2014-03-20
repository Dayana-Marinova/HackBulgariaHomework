import solution
import unittest


class AnBnTest(unittest.TestCase):
    def test_is_an_bn1(self):
        self.assertEqual(False, solution.is_an_bn('aabbaabb'))

    def test_is_an_bn2(self):
        self.assertEqual(True, solution.is_an_bn('aaaaabbbbb'))

    def test_is_an_bn3(self):
        self.assertEqual(False, solution.is_an_bn('rado'))

    def test_is_an_bn4(self):
        self.assertEqual(True, solution.is_an_bn('bbaa'))

    def test_is_an_bn5(self):
        self.assertEqual(True, solution.is_an_bn(''))


if __name__ == '__main__':
    unittest.main()
