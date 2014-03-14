import number_to_list
import unittest


class NumberToListTest(unittest.TestCase):
    def test_number_to_list1(self):
        self.assertEqual([9, 9, 9, 9], number_to_list.number_to_list(9999))

    def test_number_to_list2(self):
        self.assertEqual([1, 2, 3, 4], number_to_list.number_to_list(1234))

    def test_number_to_list3(self):
        self.assertEqual([1, 0], number_to_list.number_to_list(10))

    def test_number_to_list4(self):
        self.assertEqual([9, 8, 7, 6, 5], number_to_list.number_to_list(98765))

    def test_number_to_list5(self):
        self.assertEqual([1, 2, 3, 4, 5], number_to_list.number_to_list(12345))

if __name__ == '__main__':
    unittest.main()
