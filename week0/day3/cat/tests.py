import unittest
from solution import cat
from subprocess import call


class CatTest(unittest.TestCase):
    """docstring for CatTest"""
    def setUp(self):
        file = open('filename.txt', 'w')
        file.write("Hi my name is Dayana!")
        file.close()

    def test_cat(self):
        self.assertEqual("Hi my name is Dayana!", cat('filename.txt'))

    def tearDown(self):
        call("rm -r filename.txt", shell=True)


if __name__ == '__main__':
    unittest.main()
