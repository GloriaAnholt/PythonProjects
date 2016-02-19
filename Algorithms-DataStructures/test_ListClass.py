# Data Structures and Algorithms: ListClass
# 02.18.16
# @totallygloria


import unittest
# import sys
# from StringIO import StringIO

from ListClass import List


class ListClassTester(unittest.TestCase):

    def test_new_list(self):
        l = List()
        self.assertEqual(l.size, 0)
        self.assertEqual(l.first, None)
        self.assertEqual(l.last, None)

    def test_add(self):
        l = List()
        l.add('apple')
        self.assertEqual(l.size, 1)
        self.assertEqual(l.first.item, 'apple')
        self.assertEqual(l.last.item, 'apple')
        l.add('banana')
        self.assertEqual(l.size, 2)
        self.assertEqual(l.first.item, 'banana')
        self.assertEqual(l.last.item, 'apple')
        l.add('coconut')
        self.assertEqual(l.size, 3)
        self.assertEqual(l.first.item, 'coconut')
        self.assertEqual(l.last.item, 'apple')

    def test_append(self):
        l = List()
        l.append('apple')
        self.assertEqual(l.size, 1)
        self.assertEqual(l.first.item, 'apple')
        l.append('banana')
        self.assertEqual(l.size, 2)
        self.assertEqual(l.first.item, 'apple')
        self.assertEqual(l.last.item, 'banana')
        l.append('coconut')
        self.assertEqual(l.size, 3)
        self.assertEqual(l.first.item, 'apple')
        self.assertEqual(l.last.item, 'coconut')


if __name__ == '__main__':
    unittest.main()
