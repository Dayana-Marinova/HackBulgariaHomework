import list_to_number
import unittest


class CalculatorTest(unittest.TestCase):
    def test_list_to_number1(self):
        self.assertEqual(9999, list_to_number.list_to_number([9, 9, 9, 9]))

    def test_list_to_number2(self):
        self.assertEqual(1234, list_to_number.list_to_number([1, 2, 3, 4]))

    def test_list_to_number3(self):
        self.assertEqual(10, list_to_number.list_to_number([1, 0]))

    def test_list_to_number4(self):
        self.assertEqual(98765, list_to_number.list_to_number([9, 8, 7, 6, 5]))

    def test_list_to_number5(self):
        self.assertEqual(12345, list_to_number.list_to_number([1, 2, 3, 4, 5]))

if __name__ == '__main__':
    unittest.main()
