import goldbach
import unittest


class GoldbachTest(unittest.TestCase):
    def test_goldbach1(self):
        self.assertEqual([(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)], goldbach.goldbach(100))

    def test_goldbach2(self):
        self.assertEqual([(3, 7), (5, 5)], goldbach.goldbach(10))

    def test_goldbach3(self):
        self.assertEqual([(2, 2)], goldbach.goldbach(4))

    def test_goldbach4(self):
        self.assertEqual([(3, 5)], goldbach.goldbach(8))

    def test_goldbach5(self):
        self.assertEqual([], goldbach.goldbach(17))


if __name__ == '__main__':
    unittest.main()
