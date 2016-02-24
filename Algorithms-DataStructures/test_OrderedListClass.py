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
        l.add(7)
        self.assertEqual(l.size, 1)
        self.assertEqual(l.first.item, 7)
        self.assertEqual(l.last.item, 7)
        l.add(4)
        self.assertEqual(l.size, 2)
        self.assertEqual(l.first.item, 4)
        self.assertEqual(l.last.item, 7)
        l.add(5)
        self.assertEqual(l.size, 3)
        self.assertEqual(l.first.item, 4)
        self.assertEqual(l.last.item, 7)

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
'''
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
'''
'''
    def test_pop(self):
        l = OrderedList()
        l.add('apple')
        l.add('banana')
        l.add('coconut')
        self.assertEqual(l.size, 3)
        self.assertEqual(l.pop(), 'apple')
        self.assertEqual(l.size, 2)
        self.assertEqual(l.pop(), 'banana')
        self.assertEqual(l.size, 1)
        self.assertEqual(l.pop(), 'coconut')
        self.assertEqual(l.size, 0)
        self.assertEqual(l.pop(), None)

    def test_search(self):
        l = OrderedList()
        l.add('apple')
        l.append('banana')
        l.append('coconut')
        l.append('durian')
        l.append('elderberry')
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
        l.pop()
        self.assertTrue(l.is_empty())

    def test_index(self):
        l = OrderedList()
        self.assertEqual(l.index('peach'), None)
        l.add('apple')
        l.append('banana')
        l.append('coconut')
        l.append('durian')
        l.append('elderberry')
        self.assertEqual(l.index('apple'), 0)
        self.assertEqual(l.index('banana'), 1)
        self.assertEqual(l.index('coconut'), 2)
        self.assertEqual(l.index('durian'), 3)
        self.assertEqual(l.index('elderberry'), 4)
        self.assertEqual(l.index('peach'), None)

    def test_grab(self):
        # Build a list, check that it is as expected
        l = OrderedList()
        l.add('apple')
        l.append('banana')
        l.append('coconut')
        self.assertEqual(l.size, 3)

        # Case: grab from front of list
        self.assertEqual(l.grab(0), 'apple')
        self.assertEqual(l.size, 2)
        self.assertEqual(l.first.item, 'banana')
        self.assertEqual(l.last.item, 'coconut')

        # Case: grab from end of list
        l.append('durian')
        self.assertEqual(l.size, 3)
        self.assertEqual(l.grab(2), 'durian')
        self.assertEqual(l.first.item, 'banana')
        self.assertEqual(l.last.item, 'coconut')

        # Case: grab from middle of list
        l.append('elderberry')
        self.assertEqual(l.size, 3)
        self.assertEqual(l.grab(1), 'coconut')
        self.assertEqual(l.first.item, 'banana')
        self.assertEqual(l.last.item, 'elderberry')

    def test_insert(self):
        l = OrderedList()
        # Case: insert into empty list
        l.insert(0, 'apricot')
        self.assertEqual(l.first.item, 'apricot')
        self.assertEqual(l.last.item, 'apricot')
        self.assertEqual(l.size, 1)

        # Case: insert at a pos longer than the list
        l.insert(100, 'wintergreen')
        self.assertEqual(l.first.item, 'apricot')
        self.assertEqual(l.last.item, 'wintergreen')
        self.assertEqual(l.size, 2)

        # Case: insert into front of list
        l.insert(0, 'apple')
        self.assertEqual(l.first.item, 'apple')
        self.assertEqual(l.size, 3)

        # Case: insert into middle of list
        l.insert(2, 'banana')
        self.assertEqual(l.size, 4)
        self.assertEqual(l.first.item, 'apple')
        self.assertEqual(l.last.item, 'wintergreen')
        self.assertTrue(l.search('banana'))

        # Checking that order is as expected
        self.assertEqual(l.pop(), 'wintergreen')
        self.assertEqual(l.pop(), 'banana')
        self.assertEqual(l.pop(), 'apricot')
        self.assertEqual(l.pop(), 'apple')
        self.assertEqual(l.pop(), None)

        # Case, inserting at a weird index into empty list
        l.insert(42, 'apricot')
        self.assertEqual(l.first.item, 'apricot')
        self.assertEqual(l.last.item, 'apricot')
        self.assertEqual(l.size, 1)
'''

if __name__ == '__main__':
    unittest.main()
