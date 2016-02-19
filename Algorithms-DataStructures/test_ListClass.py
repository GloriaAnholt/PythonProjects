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


if __name__ == '__main__':
    unittest.main()
