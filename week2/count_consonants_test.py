import count_consonants
import unittest


class CalculatorTest(unittest.TestCase):
    def test_count_consonants1(self):
        self.assertEqual(12, count_consonants.count_consonants("This is a test string"))

    def test_count_consonants2(self):
        self.assertEqual(4, count_consonants.count_consonants("babababa"))

    def test_count_consonants3(self):
        self.assertEqual(16, count_consonants.count_consonants("This is this and that is this"))

    def test_count_consonants4(self):
        self.assertEqual(11, count_consonants.count_consonants('Theistareykjarbunga'))

    def test_count_consonants5(self):
        self.assertEqual(13, count_consonants.count_consonants("We have nothing in common!"))

if __name__ == '__main__':
    unittest.main()
