import unittest
from solution import concat_files
from subprocess import call


class ConcatFilesTest(unittest.TestCase):
    """docstring for ConcatFilesTest"""
    def setUp(self):
        file1 = open('filename1.txt', 'w')
        file2 = open('filename2.txt', 'w')
        file1.write("Hi my name is Dayana!")
        file2.write("Your name is?")
        file1.close()
        file2.close()

    def test_concat_files(self):
        self.assertEqual("Hi my name is Dayana!\nYour name is?", concat_files('filename1.txt', 'filename2.txt'))

    def tearDown(self):
        call("rm -r filename1.txt filename2.txt MEGATRON.txt", shell=True)


if __name__ == '__main__':
    unittest.main()
