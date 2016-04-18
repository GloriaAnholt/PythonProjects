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
    end = len(items)
    mid = end // 2

    while not located:
        # Found the item we're looking for, break out
        if wanted == items[mid]:
            located = True
            break
        # The item we want is larger than our current location, select larger half
        elif wanted > items[mid]:
            if mid >= end - 1:
                return False   # Hit the end of the list without finding it
            else:
                mid = (mid + end) // 2
        # The item we want is smaller than our current location, select smaller half
        elif wanted < items[mid]:
            if mid <= 0:
                return False   # Hit the start of the list without finding it
            else:
                mid = mid // 2
    return located



class Bin_Search_Tester(unittest.TestCase):

    def test_bin_search(self):
        self.assertEquals(bin_search([1], 1), True)
        self.assertEquals(bin_search([1,2,3,4,5], 3), True)
        self.assertEquals(bin_search([1,2,3,4,5], 2), True)
        self.assertEquals(bin_search([1,2,3,4,5], 11), False)
        #self.assertEquals(bin_search([3,7,12,15,17,21,35,44,49,51], 11), False)
        self.assertEquals(bin_search([3,7,12,15,17,21,35,44,49,51], 7), True)
        #self.assertEquals(bin_search([3,7,12,15,17,21,35,44,49,51], 6), False)
        self.assertEquals(bin_search([3,7,12,15,17,21,35,44,49,51], 2), False)


if __name__ == '__main__':
    unittest.main()



