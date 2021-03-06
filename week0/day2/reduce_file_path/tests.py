import solution
import unittest


class FilePathTest(unittest.TestCase):
    def test_reduce_file_path1(self):
        self.assertEqual("/srv/www/htdocs/wtf", solution.reduce_file_path('/srv/www/htdocs/wtf/'))

    def test_reduce_file_path2(self):
        self.assertEqual("/srv", solution.reduce_file_path('/srv/./././././'))

    def test_reduce_file_path3(self):
        self.assertEqual("/etc/wtf", solution.reduce_file_path('/etc//wtf/'))

    def test_reduce_file_path4(self):
        self.assertEqual("/", solution.reduce_file_path("/etc/../etc/../etc/../"))

    def test_reduce_file_path5(self):
        self.assertEqual("/home/didi", solution.reduce_file_path("/home/didi/lesson/../"))


if __name__ == '__main__':
    unittest.main()
