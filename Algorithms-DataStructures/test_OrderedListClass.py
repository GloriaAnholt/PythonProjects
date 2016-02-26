# Data Structures and Algorithms: ListClass
# 02.18.16
# @totallygloria


import unittest
# import sys
# from StringIO import StringIO

from OrderedListClass import OrderedList


class OrderedListClassTester(unittest.TestCase):

    def test_new_ordered_list(self):
        l = OrderedList()
        self.assertEqual(l.size, 0)
        self.assertEqual(l.first, None)
        self.assertEqual(l.last, None)

    def test_add(self):
        l = OrderedList()
        l.add(7)  # add to an empty list
        self.assertEqual(l.size, 1)
        self.assertEqual(l.first.item, 7)
        self.assertEqual(l.last.item, 7)
        l.add(4)  # add to front of list
        self.assertEqual(l.size, 2)
        self.assertEqual(l.first.item, 4)
        self.assertEqual(l.last.item, 7)
        l.add(3)  # add to front of list
        self.assertEqual(l.size, 3)
        self.assertEqual(l.first.item, 3)
        l.add(8)  # add to end of list
        self.assertEqual(l.size, 4)
        self.assertEqual(l.last.item, 8)
        l.add(9)  # add to end of list
        self.assertEqual(l.size, 5)
        self.assertEqual(l.last.item, 9)
        l.add(5)  # add to middle of list
        self.assertEqual(l.size, 6)
        a = l.first
        for i in range(2):  # walk through the list until the num we added
            a = a.behind
        self.assertEqual(a.item, 5)  # confirm that it is what was added
        l.add(6)  # add to middle of list
        self.assertEqual(l.size, 7)
        b = l.first
        for i in range(3):  # walk through the list until the num we added
            b = b.behind
        self.assertEqual(b.item, 6)

        o = OrderedList()
        o.add('banana')
        self.assertEqual(o.size, 1)
        self.assertEqual(o.first.item, 'banana')
        self.assertEqual(o.last.item, 'banana')
        o.add('apple')
        self.assertEqual(o.size, 2)
        self.assertEqual(o.first.item, 'apple')
        self.assertEqual(o.last.item, 'banana')
        o.add('coconut')
        self.assertEqual(o.size, 3)
        self.assertEqual(o.first.item, 'apple')
        self.assertEqual(o.last.item, 'coconut')

    def test_remove(self):
        # Build a list, check that it is as expected
        l = OrderedList()
        l.add('apple')
        l.add('banana')
        l.add('coconut')
        self.assertEqual(l.size, 3)
        self.assertEqual(l.first.item, 'apple')
        self.assertEqual(l.last.item, 'coconut')

        # Case: remove from front of list
        self.assertEqual(l.first.item, 'apple')
        l.remove('apple')
        self.assertEqual(l.first.item, 'banana')
        self.assertEqual(l.size, 2)

        # Case: remove from end of list
        l.add('durian')
        self.assertEqual(l.size, 3)
        self.assertEqual(l.last.item, 'durian')
        l.remove('durian')
        self.assertEqual(l.size, 2)
        self.assertEqual(l.last.item, 'coconut')
        self.assertEqual(l.first.item, 'banana')

        # Case: remove from middle of list
        l.add('elderberry')
        self.assertEqual(l.size, 3)
        self.assertEqual(l.last.item, 'elderberry')
        l.remove('coconut')
        self.assertEqual(l.size, 2)
        self.assertEqual(l.first.item, 'banana')
        self.assertEqual(l.last.item, 'elderberry')
        l.remove('banana')
        self.assertEqual(l.size, 1)
        self.assertEqual(l.first.item, 'elderberry')
        self.assertEqual(l.last.item, 'elderberry')
        l.remove('elderberry')
        self.assertEqual(l.size, 0)
        self.assertEqual(l.first, None)
        self.assertEqual(l.last, None)
        l.remove('pear')
        self.assertEqual(l.size, 0)
        self.assertEqual(l.first, None)
        self.assertEqual(l.last, None)

    def test_search(self):
        l = OrderedList()
        l.add('apple')
        l.add('banana')
        l.add('coconut')
        l.add('durian')
        l.add('elderberry')
        self.assertEqual(l.size, 5)
        self.assertTrue(l.search('apple'))
        self.assertTrue(l.search('banana'))
        self.assertTrue(l.search('coconut'))
        self.assertTrue(l.search('durian'))
        self.assertTrue(l.search('elderberry'))
        self.assertFalse(l.search(None))
        self.assertFalse(l.search('peach'))

    def test_is_empty(self):
        l = OrderedList()
        self.assertTrue(l.is_empty())
        l.add('apple')
        self.assertFalse(l.is_empty())
        l.remove('apple')
        self.assertTrue(l.is_empty())

    def test_index(self):
        l = OrderedList()
        self.assertEqual(l.index('peach'), None)
        l.add('apple')
        l.add('banana')
        l.add('coconut')
        l.add('durian')
        l.add('elderberry')
        self.assertEqual(l.index('apple'), 0)
        self.assertEqual(l.index('banana'), 1)
        self.assertEqual(l.index('coconut'), 2)
        self.assertEqual(l.index('durian'), 3)
        self.assertEqual(l.index('elderberry'), 4)
        self.assertEqual(l.index('peach'), None)

    def test_pop(self):
        l = OrderedList()
        l.add('apple')
        l.add('banana')
        l.add('coconut')
        self.assertEqual(l.size, 3)
        self.assertEqual(l.pop(), 'coconut')
        self.assertEqual(l.size, 2)
        self.assertEqual(l.pop(), 'banana')
        self.assertEqual(l.size, 1)
        self.assertEqual(l.pop(), 'apple')
        self.assertEqual(l.size, 0)
        self.assertEqual(l.pop(), None)

    def test_grab(self):
        # Build a list, check that it is as expected
        l = OrderedList()
        l.add('apple')
        l.add('banana')
        l.add('coconut')
        self.assertEqual(l.size, 3)

        # Case: grab from front of list
        self.assertEqual(l.grab(0), 'apple')
        self.assertEqual(l.size, 2)
        self.assertEqual(l.first.item, 'banana')
        self.assertEqual(l.last.item, 'coconut')

        # Case: grab from end of list
        l.add('durian')
        self.assertEqual(l.size, 3)
        self.assertEqual(l.grab(2), 'durian')
        self.assertEqual(l.first.item, 'banana')
        self.assertEqual(l.last.item, 'coconut')

        # Case: grab from middle of list
        l.add('elderberry')
        self.assertEqual(l.size, 3)
        self.assertEqual(l.grab(1), 'coconut')
        self.assertEqual(l.first.item, 'banana')
        self.assertEqual(l.last.item, 'elderberry')


if __name__ == '__main__':
    unittest.main()
