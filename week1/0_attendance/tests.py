import unittest
import solution
import time
from subprocess import call


class AttendanceTest(unittest.TestCase):
    """docstring for AttendanceTest"""
    def setUp(self):
        self.stamp = time.strftime("%Y_%m_%d")
        self.name_file = 'attendance_' + self.stamp
        self.list_of_names_file = [self.name_file]
        self.list_of_names_file1 = ['123']
        self.list_of_names_file2 = []
        self.list_of_name_student = []

    def test_lists(self):
        self.assertEqual(1, solution.lists(self.list_of_names_file))

    def test_statistic(self):
        solution.add(
            'Даяна',
            'Маринова',
            self.list_of_name_student,
            self.list_of_names_file
        )
        file = open('123', 'r')
        count = 0
        for lines in file:
            count += 1
        self.assertEqual(count, solution.statistic(self.list_of_names_file1))

    def test_status(self):
        solution.add(
            'Даяна',
            'Маринова',
            self.list_of_name_student,
            self.list_of_names_file1
        )
        self.assertEqual('Даяна Маринова\n', solution.status())

    def test_load(self):
        self.assertEqual(
            'File 123 loaded',
            solution.load('1', self.list_of_names_file1)
        )
        self.assertEqual(
            'There is no list with that index',
            solution.load('4', self.list_of_names_file1)
        )

    def test_create(self):
        solution.it_is_changed = False
        self.assertEqual(
            'New file created and loaded: ' + self.name_file,
            solution.create(self.list_of_names_file2)
        )

    def test_create_have_file_allready(self):
        self.assertEqual(
            'You already have a file for today it is: ' + self.name_file,
            solution.create(self.list_of_names_file)
        )

    def test_create_if_it_changes(self):
        solution.it_is_changed = True
        solution.name_of_file = '123'
        self.assertEqual(
            'New file created and loaded: 123',
            solution.create(self.list_of_names_file)
        )

    def test_change_date(self):
        self.assertEqual(
            'Date changed to 123.' + '\n' + 'Current file saved & discarded.' + '\n' + 'You can create or load.',
            solution.change_date('123', self.list_of_names_file)
        )

    def test_change_date_allready_have_name_like_this(self):
        self.assertEqual(
            "File with this name: 123 is already exist for today too!",
            solution.change_date('123', self.list_of_names_file1)
        )

    def test_add_successfully(self):
        solution.name_of_file = '123'
        solution.it_is_changed = False
        self.assertEqual(
            'Даяна Маринова is now attending',
            solution.add(
                'Даяна',
                'Маринова',
                self.list_of_name_student,
                self.list_of_names_file1)
        )

    def test_add_allready_in_list(self):
        solution.name_of_file = '123'
        solution.it_is_changed = False
        solution.add(
            'Даяна',
            'Маринова',
            self.list_of_name_student, self.list_of_names_file1)
        self.assertEqual(
            'Даяна Маринова is already added to the list for today.',
            solution.add(
                'Даяна',
                'Маринова',
                self.list_of_name_student, self.list_of_names_file1)
        )

    def test_add_does_not_exist(self):
        solution.name_of_file = '123'
        solution.it_is_changed = False
        self.assertEqual(
            'This student does not exist!',
            solution.add(
                'sad',
                'sad',
                self.list_of_name_student, self.list_of_names_file1)
        )

    def tearDown(self):
        call("rm -r 123", shell=True)


if __name__ == '__main__':
    unittest.main()
