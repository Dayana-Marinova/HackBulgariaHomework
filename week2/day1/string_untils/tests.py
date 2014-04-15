import solution
import unittest


class CalculatorTest(unittest.TestCase):
    def test_lines(self):
        self.assertEqual(['hi', 'dayana'], solution.lines('hi\ndayana'))

    def test_unlines(self):
        self.assertEqual('hi dayana', solution.unlines(["hi", "dayana"]))

    def test_words(self):
        self.assertEqual(['d', 'a'], solution.words('da'))

    def test_unwords(self):
        self.assertEqual('d a n e', solution.unwords(['d', 'a', 'n', 'e']))

    def test_tabs_to_spaces(self):
        self.assertEqual('hi  dayana  ', solution.tabs_to_spaces('hi\tdayana\t', 2))


if __name__ == '__main__':
    unittest.main()
