# Algorithms and Data Structures: Quick Sort
# 07.07.2016
# @totallygloria

import unittest
import random
from QuickSort import QuickSort


class QuickSortTester(unittest.TestCase):

    def test_getpivot(self):
        qs = QuickSort()
        # Basic case, find middle of three, regardless of location in list
        qs.array = [1,2,3]
        self.assertEquals(qs.getpivot(0, 2), 2)
        qs.array = [2,1,3]
        self.assertEquals(qs.getpivot(0, 2), 2)
        qs.array = [1,3,2]
        self.assertEquals(qs.getpivot(0, 2), 2)
        # One-item list
        qs.array = [-7]
        self.assertEquals(qs.getpivot(0, 0), -7)
        # List of the same item repeated
        qs.array = [2,2,2,2,2,2,2,2,2,2]
        self.assertEquals(qs.getpivot(0, 9), 2)
        # Find middle of three when they're the same and the list is longer
        qs.array = [10, 2, 2, 2, 10, 2, 2, 2, 2, 10]
        self.assertEquals(qs.getpivot(0, 9), 10)
        # Find middle of three when only two are the same
        qs.array = [10, 2, 2, 2, 10, 2, 2, 2, 2, 0]
        self.assertEquals(qs.getpivot(0, 9), 10)
        qs.array = [0, 2, 2, 2, 10, 2, 2, 2, 2, 10]
        self.assertEquals(qs.getpivot(0, 9), 10)
        qs.array = [10, 2, 2, 2, 0, 2, 2, 2, 2, 10]
        self.assertEquals(qs.getpivot(0, 9), 10)

    def test_quicksort(self):
        qs = QuickSort()
        # Base case: empty list or list of one element should return itself
        self.assertEquals(qs.quicksort(), [])
        qs.array = [1]
        self.assertEquals(qs.quicksort(), [1])
        # quicksort doesn't return anything, it just calls exchanger
        # probably not possible to test that the list comes back sorted

    def test_exchanger(self):
        qs = QuickSort()
        # A list of len <= 1 should return the list itself
        self.assertEquals(qs.exchanger(10, 10), None)
        self.assertEquals(qs.exchanger(10, 0), None)
        qs.array = [n for n in random.randrange(1,101,1)]




if __name__ == '__main__':
    unittest.main()
