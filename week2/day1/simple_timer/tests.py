import solution
import unittest


class CalculatorTest(unittest.TestCase):
    def test_start_timer(self):
        solution.is_started = False
        self.assertEqual(True, solution.start_timer(10))

    def test_start_started_timer(self):
        solution.is_started = False
        self.assertEqual(True, solution.start_timer(10))
        self.assertEqual(False, solution.start_timer(10))

    def test_decrease_time_10(self):
        solution.time_left = 10
        solution.is_started = True
        self.assertEqual(True, solution.decrease_time())

    def test_decrease_time_0(self):
        solution.is_started = True
        solution.time_left = 2
        self.assertEqual(True, solution.decrease_time())
        self.assertEqual(True, solution.decrease_time())
        self.assertEqual(False, solution.decrease_time())

    def test_decrease_time_started(self):
        solution.is_started = False
        solution.time_left = 10
        self.assertEqual(False, solution.decrease_time())

    def test_decrease_time_started_0(self):
        solution.is_started = False
        solution.time_left = 0
        self.assertEqual(False, solution.decrease_time())

    def test_is_timer_running(self):
        solution.is_started = True
        solution.time_left = 2
        self.assertEqual(True, solution.decrease_time())
        self.assertEqual(True, solution.decrease_time())
        self.assertEqual(False, solution.decrease_time())

    def test_stop_timer_if_started(self):
        solution.is_started = True
        self.assertEqual(True, solution.stop_timer())

    def test_stop_timer_if_not_started(self):
        solution.is_started = False
        self.assertEqual(False, solution.stop_timer())

    def test_seconds_left1(self):
        solution.time_left = 2
        solution.is_finish = False
        solution.is_started = True
        self.assertEqual(2, solution.seconds_left())

    def test_seconds_left_not_started(self):
        solution.is_started = False
        solution.time_left = 7
        solution.is_finish = False
        self.assertEqual(0, solution.seconds_left())

    def test_seconds_left_is_finish(self):
        solution.is_started = True
        solution.time_left = 5
        solution.is_finish = True
        self.assertEqual(0, solution.seconds_left())

    def test_seconds_left2(self):
        solution.time_left = 2
        solution.is_finish = True
        solution.is_started = False
        self.assertEqual(0, solution.seconds_left())


if __name__ == '__main__':
    unittest.main()
