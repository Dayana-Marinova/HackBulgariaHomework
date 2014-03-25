import unittest
from time import time
from datetime import datetime
from solution import take, status, save, lists, load, finish


class PizzaTest(unittest.TestCase):
    """docstring for PizzaTest"""

    def test_take(self):
        dict_orders = {}
        self.assertEqual("Taking order from dayana for 10", take('dayana', 10, dict_orders))
        self.assertEqual(1, len(dict_orders))

    def test_status(self):
        dict_orders = {'dayana': 10, 'ivo': 12}
        self.assertEqual(2, status(dict_orders))

    def test_save(self):
        ts = time()
        name_of_order = 'orders_' + datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
        dict_orders = {'dayana': 10}
        list_of_orders = []
        self.assertEqual("Saved the current order to %s." % name_of_order, save(dict_orders, list_of_orders))
        self.assertEqual(1, len(list_of_orders))

    def test_lists(self):
        list_of_orders = []
        dict_orders = {'dayana': 10}
        save(dict_orders, list_of_orders)
        save(dict_orders, list_of_orders)
        self.assertEqual(2, lists(list_of_orders))

    def test_load(self):
        list_of_orders = []
        dict_orders = {'dayana': 10}
        save(dict_orders, list_of_orders)
        save(dict_orders, list_of_orders)
        save(dict_orders, list_of_orders)
        self.assertEqual(2, load('1', list_of_orders, True))
        self.assertEqual(
            'You have unsaved order.' + '\n' + 'If you wish to discard the current order, type load again',
            load(10, list_of_orders, False)
        )

    def test_finish(self):
        self.assertEqual('Finishing order. Goodbye!', finish(True))
        self.assertEqual(
            'You have not saved your order.' + '\n' + 'If you wish to continue, type finish again.' + '\n' + 'If you want to save your order, type save',
            finish(False)
        )


if __name__ == '__main__':
    unittest.main()
