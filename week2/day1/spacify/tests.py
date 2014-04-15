import solution
import unittest
from subprocess import call


class SpacifyTest(unittest.TestCase):
    def setUp(self):
        file1 = open("my_file.txt", 'w')
        file1.write("   hi! What    yor name?")
        file1.close()

    def test_spacefy(self):
        self.assertEqual("  hi! What  yor name?", solution.spacify('my_file.txt'))

    def tearDown(self):
        call("rm -r my_file.txt", shell=True)


if __name__ == '__main__':
    unittest.main()
