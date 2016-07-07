# Algorithms and Data Structures: Quick Sort
# 07.07.2016
# @totallygloria

import unittest
from QuickSort import quicksort, exchanger, getpivot


class QuickSortTester(unittest.TestCase):

    def test_getpivot(self):
        # Basic case, find middle of three, regardless of location in list
        self.assertEquals(getpivot([1,2,3], 0, 2), 2)
        self.assertEquals(getpivot([2,1,3], 0, 2), 2)
        self.assertEquals(getpivot([1,3,2], 0, 2), 2)
        # One-item list
        self.assertEquals(getpivot([-7], 0, 0), -7)
        # List of the same item repeated
        self.assertEquals(getpivot([2,2,2,2,2,2,2,2,2,2], 0, 9), 2)
        # Find middle of three when they're the same and the list is longer
        self.assertEquals(getpivot([10, 2, 2, 2, 10, 2, 2, 2, 2, 10], 0, 9), 10)
        # Find middle of three when only two are the same
        self.assertEquals(getpivot([10, 2, 2, 2, 10, 2, 2, 2, 2, 0], 0, 9), 10)
        self.assertEquals(getpivot([0, 2, 2, 2, 10, 2, 2, 2, 2, 10], 0, 9), 10)
        self.assertEquals(getpivot([10, 2, 2, 2, 0, 2, 2, 2, 2, 10], 0, 9), 10)




if __name__ == '__main__':
    unittest.main()
