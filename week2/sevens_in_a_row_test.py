import sevens_in_a_row
import unittest


class CalculatorTest(unittest.TestCase):
    def test_sevens_in_a_row1(self):
        self.assertEqual(True, sevens_in_a_row.sevens_in_a_row([10,8,7,6,7,7,7,20,-7], 3))

    def test_sevens_in_a_row2(self):
        self.assertEqual(True, sevens_in_a_row.sevens_in_a_row([10, 10, 10, 10], 0))

    def test_sevens_in_a_row3(self):
        self.assertEqual(True, sevens_in_a_row.sevens_in_a_row([7,7,7,1,1,1,7,7,7,7], 4))

    def test_sevens_in_a_row4(self):
        self.assertEqual(False, sevens_in_a_row.sevens_in_a_row([22, 23, 24, 25], 6))

    def test_sevens_in_a_row5(self):
        self.assertEqual(False, sevens_in_a_row.sevens_in_a_row([], 4))

if __name__ == '__main__':
    unittest.main()
