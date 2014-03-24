import unittest
from subprocess import call


class GenerateNumbersTest(unittest.TestCase):
    """docstring for Generate_NumbersTest"""
    def test_gen_number_10(self):
        call("python3.3 solution.py file.txt 10", shell=True)
        file = open('file.txt', 'r')
        content = file.read()
        count_numbers = len(content.split(", "))
        self.assertEqual(10, count_numbers)

    def test_gen_number_100(self):
        call("python3.3 solution.py file.txt 100", shell=True)
        file = open('file.txt', 'r')
        content = file.read()
        count_numbers = len(content.split(", "))
        self.assertEqual(100, count_numbers)

    def tearDown(self):
        call("rm -r file.txt", shell=True)

if __name__ == '__main__':
    unittest.main()
