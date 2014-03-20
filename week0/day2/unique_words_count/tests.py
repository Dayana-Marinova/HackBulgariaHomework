import solution
import unittest


class UniqueWordsCountTest(unittest.TestCase):
    def test_unique_words_count1(self):
        self.assertEqual(1, solution.unique_words_count(['python', 'python', 'python']))

    def test_unique_words_count2(self):
        self.assertEqual(1, solution.unique_words_count(['']))

    def test_unique_words_count3(self):
        self.assertEqual(3, solution.unique_words_count(["apple", "banana", "apple", "pie"]))

    def test_unique_words_count4(self):
        self.assertEqual(3, solution.unique_words_count(['aa', 'bb', 'cc']))


if __name__ == '__main__':
    unittest.main()
