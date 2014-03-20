import solution
import unittest


class MemberOfFibonacciTest(unittest.TestCase):
    def test_member_of_nth_fib_lists1(self):
        self.assertEqual(False, solution.member_of_nth_fib_lists([1, 2], [3, 4], [5, 6]))

    def test_member_of_nth_fib_lists2(self):
        self.assertEqual(True, solution.member_of_nth_fib_lists([1, 2], [3, 4], [1,2,3,4,3,4,1,2,3,4]))

    def test_member_of_nth_fib_lists3(self):
        self.assertEqual(True, solution.member_of_nth_fib_lists([7,11], [2], [7,11,2,2,7,11,2]))

    def test_member_of_nth_fib_lists4(self):
        self.assertEqual(False, solution.member_of_nth_fib_lists([7,11], [2], [11,7,2,2,7]))

    def test_member_of_nth_fib_lists5(self):
        self.assertEqual(True, solution.member_of_nth_fib_lists([3, 4 ,5], [2], [3, 4, 5 ,2]))


if __name__ == '__main__':
    unittest.main()
