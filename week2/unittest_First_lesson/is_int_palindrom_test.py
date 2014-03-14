import is_int_palindrom
import unittest


class IsIntPalindromTest(unittest.TestCase):
    def test_is_int_palindrom1(self):
        self.assertEqual(True, is_int_palindrom.is_int_palindrom(10001))

    def test_is_int_palindrom2(self):
        self.assertEqual(True, is_int_palindrom.is_int_palindrom(1233321))

    def test_is_int_palindrom3(self):
        self.assertEqual(True, is_int_palindrom.is_int_palindrom(000000))

    def test_is_int_palindrom4(self):
        self.assertEqual(False, is_int_palindrom.is_int_palindrom(12345666432))

    def test_is_int_palindrom5(self):
        self.assertEqual(False, is_int_palindrom.is_int_palindrom(42))

if __name__ == '__main__':
    unittest.main()
