import count_vowels
import unittest


class CountVowelsTest(unittest.TestCase):
    def test_count_vowels1(self):
        self.assertEqual(5, count_vowels.count_vowels("This is a test string"))

    def test_count_vowels2(self):
        self.assertEqual(4, count_vowels.count_vowels("babababa"))

    def test_count_vowels3(self):
        self.assertEqual(7, count_vowels.count_vowels("This is this and that is this"))

    def test_count_vowels4(self):
        self.assertEqual(16, count_vowels.count_vowels("Python is an awesome language to program in!"))

    def test_count_vowels5(self):
        self.assertEqual(8, count_vowels.count_vowels("We have nothing in common!"))

if __name__ == '__main__':
    unittest.main()
