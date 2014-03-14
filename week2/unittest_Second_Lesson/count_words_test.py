import count_words
import unittest


class CountWordsTest(unittest.TestCase):
    def test_count_words1(self):
        self.assertEqual({'python': 3}, count_words.count_words(['python', 'python', 'python']))

    def test_count_words2(self):
        self.assertEqual({'': 1}, count_words.count_words(['']))

    def test_count_words3(self):
        self.assertEqual({'banana': 1, 'apple': 2, 'pie': 1}, count_words.count_words(["apple", "banana", "apple", "pie"]))

    def test_count_words4(self):
        self.assertEqual({'aa': 1, 'bb': 1, 'cc': 1}, count_words.count_words(['aa', 'bb', 'cc']))

    def test_count_words5(self):
        self.assertEqual("it must be only string!", count_words.count_words([1, 1, 3, 1, 1, 6]))


if __name__ == '__main__':
    unittest.main()
