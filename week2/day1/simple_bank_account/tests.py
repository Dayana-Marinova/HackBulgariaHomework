import solution
import unittest


class CalculatorTest(unittest.TestCase):
    def test_get_balance1(self):
        solution.balance = 100
        self.assertEqual(100, solution.get_balance())

    def test_get_balance2(self):
        solution.balance = -100
        self.assertEqual(False, solution.get_balance())

    def test_deposit_money1(self):
        solution.balance = 100
        self.assertEqual(200, solution.deposit_money(100))

    def test_deposit_money2(self):
        solution.balance = 100
        self.assertEqual(False, solution.deposit_money(-20))

    def test_withdraw_money1(self):
        solution.balance = 100
        self.assertEqual(False, solution.withdraw_money(150))

    def test_withdraw_money2(self):
        solution.balance = 100
        self.assertEqual(50, solution.withdraw_money(50))

    def test_withdraw_money3(self):
        solution.balance = 100
        self.assertEqual(False, solution.withdraw_money(-50))


if __name__ == '__main__':
    unittest.main()
