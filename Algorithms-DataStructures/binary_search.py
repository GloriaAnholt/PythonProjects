# Algorithms and Data Structures: Binary Search
# 4.18.2016
# @totallygloria


'''
A binary search starts by examining the middle item: If it's the search item, the search
is completed. If it's not the correct item, we use the ordered nature of the list to
eliminate half of the remaining items (larger or smaller, based on the comparison).

The function takes a list and the search item and returns a boolean for membership,
and the index, if found.
'''

import unittest

def bin_search(items, wanted):

    located = False
    pos = 0
    size = len(items)
    mid = size // 2

    if items[mid] == wanted:
        located = True
        pos = mid
    elif items[mid] > wanted:
        for i in range(mid, -1, -1):
            pos = i
            if items[i] == wanted:
                located = True
                break
    elif items[mid] < wanted:
        for i in range(mid, size):
            pos = i
            if items[i] == wanted:
                located = True
                break

    return (located, pos)



class Bin_Search_Tester(unittest.TestCase):

    def test_bin_search(self):
        self.assertEquals(bin_search([1], 1), (True, 0))
        self.assertEquals(bin_search([1,2,3,4,5], 3), (True, 2))
        self.assertEquals(bin_search([1,2,3,4,5], 2), (True, 1))
        self.assertEquals(bin_search([1,2,3,4,5], 11), (False, 4))
        self.assertEquals(bin_search([3,7,12,15,17,21,35,44,49,51], 11), (False, 0))
        self.assertEquals(bin_search([3,7,12,15,17,21,35,44,49,51], 7), (True, 1))
        self.assertEquals(bin_search([3,7,12,15,17,21,35,44,49,51], 6), (False, 0))
        self.assertEquals(bin_search([3,7,12,15,17,21,35,44,49,51], 2), (False, 0))


if __name__ == '__main__':
    unittest.main()