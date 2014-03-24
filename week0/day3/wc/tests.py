import unittest
from solution import lines_count, words_count, chars_count
from subprocess import call


class WCTest(unittest.TestCase):
    """docstring for WCTest"""
    def setUp(self):
        file = open('filename.txt', 'w')
        file.write("hi my name is dayana marinova.\nyour name is?\nnice too meet you! \nGoodbye!")
        file.close()

    def test_lines_count(self):
        self.assertEqual(4, lines_count('filename.txt'))

    def test_words_count(self):
        self.assertEqual(14, words_count('filename.txt'))

    def test_chars_count(self):
        self.assertEqual(73, chars_count('filename.txt'))

    def tearDown(self):
        call("rm -r filename.txt", shell=True)

if __name__ == '__main__':
    unittest.main()
