import is_number_balanced
import unittest


class IsBalanceTest(unittest.TestCase):
    def test_is_number_balanced1(self):
        self.assertEqual(True, is_number_balanced.is_number_balanced(10001))

    def test_is_number_balanced2(self):
        self.assertEqual(True, is_number_balanced.is_number_balanced(14332))

    def test_is_number_balanced3(self):
        self.assertEqual(False, is_number_balanced.is_number_balanced(4859))

    def test_is_number_balanced4(self):
        self.assertEqual(False, is_number_balanced.is_number_balanced(1231))

    def test_is_number_balanced5(self):
        self.assertEqual(True, is_number_balanced.is_number_balanced(1238033))

if __name__ == '__main__':
    unittest.main()
