import unittest
from solution import sum_numbers
from subprocess import call


class SumNumbersTest(unittest.TestCase):
    """docstring for SumNumbersTest"""
    def setUp(self):
        file = open('filename.txt', 'w')
        array_num = ['1', '2', '3', '4', '5']
        file.write(' '.join(array_num))
        file.close()

    def test_sum_numbers1(self):
        call("python3.3 solution.py filename.txt", shell=True)
        file = open('filename.txt', 'r')
        content = file.read()
        count_numbers = len(content.split(" "))
        self.assertEqual(5, count_numbers)

    def test_sum_numbers2(self):
        self.assertEqual(15, sum_numbers('filename.txt'))

    def tearDown(self):
        call("rm -r filename.txt", shell=True)

if __name__ == '__main__':
    unittest.main()
