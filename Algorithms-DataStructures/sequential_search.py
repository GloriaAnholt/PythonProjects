# Algorithms and Data Structures: Sequential Search
# 4.18.2016
# @totallygloria


'''
Starting at the first item in the list, check each item using the sequential ordering
until we find what we are looking for or run out of items.

The function takes a list and the search item and returns a boolean for membership,
and the index, if found.
'''

import unittest

def seq_search(items, wanted):

    located = False
    pos = 0

    for item in items:
        if item == wanted:
            located = True
            break
        pos += 1

    return located


class Sec_Search_Tester(unittest.TestCase):

    def test_seq_search(self):
        self.assertEquals(seq_search([], ''), False)
        self.assertNotEquals(seq_search([], ''), True)
        self.assertEquals(seq_search([], '1'), False)
        self.assertEquals(seq_search(['1'], '1'), True)
        self.assertEquals(seq_search(['1'], 1), False)
        self.assertEquals(seq_search([1], 1), True)
        self.assertEquals(seq_search([5,4,3,2,1], 1), True)
        self.assertEquals(seq_search([5,4,3,2,1], 11), False)
        self.assertEquals(seq_search([5,4, None, 'a', 3,2,'whelp',1], 'a'), True)
        self.assertEquals(seq_search([5,4, None, 'a', 3,2,'whelp',1], None), True)
        self.assertEquals(seq_search([5,4, None, [1,2,3], 'a', 3,2,'whelp',1], [1,2,3]), True)



if __name__ == '__main__':
    unittest.main()
