import prepare_meal
import unittest


class MealTest(unittest.TestCase):
    def test_prepare_meal1(self):
        self.assertEqual('eggs', prepare_meal.prepare_meal(5))

    def test_prepare_meal2(self):
        self.assertEqual('spam spam and eggs', prepare_meal.prepare_meal(15))

    def test_prepare_meal3(self):
        self.assertEqual('spam spam ', prepare_meal.prepare_meal(9))

    def test_prepare_meal4(self):
        self.assertEqual('spam spam spam and eggs', prepare_meal.prepare_meal(45))

    def test_prepare_meal5(self):
        self.assertEqual("''", prepare_meal.prepare_meal(0))

    def test_prepare_meal6(self):
        self.assertEqual("''", prepare_meal.prepare_meal(7))


if __name__ == '__main__':
    unittest.main()
