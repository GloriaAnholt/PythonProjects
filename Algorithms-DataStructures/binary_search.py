# Algorithms and Data Structures: Binary Search
# 4.18.2016
# @totallygloria


'''
A binary search starts by examining the middle item: If it's the search item, the search
is completed. If it's not the correct item, we use the ordered nature of the list to
eliminate half of the remaining items (larger or smaller, based on the comparison).

The function takes a list and the search item and returns a boolean for membership.
'''

import unittest

def bin_search(items, wanted):

    located = False
    end = len(items)
    start = 0

    while not located and start < end:
        mid = (start + end) // 2
        # Found the item we're looking for, break out
        if wanted == items[mid]:
            located = True
            break
        # The item we want is larger than our current location, select larger half
        elif wanted > items[mid]:
            start = mid + 1
        # The item we want is smaller than our current location, select smaller half
        # Floor division rounds down, don't need to subtract one.
        elif wanted < items[mid]:
            end = mid

    return located


def recursive_bin_search(items, wanted):

    # If you trim the list down to zero and haven't found it, it's not there
    if len(items) == 0:
        return False
    else:
        mid = len(items) // 2
        # Found it, return true
        if wanted == items[mid]:
            return True
        # Call the search with the first half of the list
        elif wanted < items[mid]:
            return recursive_bin_search(items[:mid], wanted)
        # Call the search with the second half of the list
        elif wanted > items[mid]:
            return recursive_bin_search(items[mid + 1:], wanted)




class Bin_Search_Tester(unittest.TestCase):

    def test_bin_search(self):
        self.assertEquals(bin_search([1], 1), True)
        self.assertEquals(bin_search([1,2,3,4,5], 3), True)
        self.assertEquals(bin_search([1,2,3,4,5], 2), True)
        self.assertEquals(bin_search([1,2,3,4,5], 11), False)
        self.assertEquals(bin_search([3,7,12,15,17,21,35,44,49,51], 11), False)
        self.assertEquals(bin_search([3,7,12,15,17,21,35,44,49,51], 7), True)
        self.assertEquals(bin_search([3,7,12,15,17,21,35,44,49,51], 6), False)
        self.assertEquals(bin_search([3,7,12,15,17,21,35,44,49,51], 2), False)

    def test_recursive_bin_search(self):
        self.assertEquals(recursive_bin_search([1], 1), True)
        self.assertEquals(recursive_bin_search([1,2,3,4,5], 3), True)
        self.assertEquals(recursive_bin_search([1,2,3,4,5], 2), True)
        self.assertEquals(recursive_bin_search([1,2,3,4,5], 11), False)
        self.assertEquals(recursive_bin_search([3,7,12,15,17,21,35,44,49,51], 11), False)
        self.assertEquals(recursive_bin_search([3,7,12,15,17,21,35,44,49,51], 7), True)
        self.assertEquals(recursive_bin_search([3,7,12,15,17,21,35,44,49,51], 6), False)
        self.assertEquals(recursive_bin_search([3,7,12,15,17,21,35,44,49,51], 2), False)



if __name__ == '__main__':
    unittest.main()

