import solution
import unittest


class CountSubstringTest(unittest.TestCase):
    def test_count_substring1(self):
        self.assertEqual(2, solution.count_substrings("This is a test string", "is"))

    def test_count_substring2(self):
        self.assertEqual(3, solution.count_substrings("babababa", "baba"))

    def test_count_substring3(self):
        self.assertEqual(2, solution.count_substrings("This is this and that is this", "this"))

    def test_count_substring4(self):
        self.assertEqual(4, solution.count_substrings("Python is an awesome language to program in!", "o"))

    def test_count_substring5(self):
        self.assertEqual(0, solution.count_substrings("We have nothing in common!", "really?"))

if __name__ == '__main__':
    unittest.main()
