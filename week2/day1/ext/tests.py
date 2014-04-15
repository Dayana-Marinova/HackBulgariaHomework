import unittest
from solution import ext


class ExtTest(unittest.TestCase):
    def test_ext_0(self):
        self.assertEqual(2, ext('.py'))

    def test_ext_1(self):
        self.assertEqual(0, ext('py'))

    def test_ext_2(self):
        self.assertEqual(0, ext('.txt'))

if __name__ == '__main__':
    unittest.main()
