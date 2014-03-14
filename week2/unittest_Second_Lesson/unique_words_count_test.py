import unique_words_count
import unittest


class UniqueWordsCountTest(unittest.TestCase):
    def test_unique_words_count1(self):
        self.assertEqual(1, unique_words_count.unique_words_count(['python', 'python', 'python']))

    def test_unique_words_count2(self):
        self.assertEqual(1, unique_words_count.unique_words_count(['']))

    def test_unique_words_count3(self):
        self.assertEqual(3, unique_words_count.unique_words_count(["apple", "banana", "apple", "pie"]))

    def test_unique_words_count4(self):
        self.assertEqual(3, unique_words_count.unique_words_count(['aa', 'bb', 'cc']))

    def test_unique_words_count5(self):
        self.assertEqual('it must be only string!', unique_words_count.unique_words_count([1, 1, 3, 1, 1, 6]))


if __name__ == '__main__':
    unittest.main()
