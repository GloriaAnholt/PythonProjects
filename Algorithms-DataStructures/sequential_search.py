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

    for pos, item in enumerate(items):
        if item == wanted:
            located = True
            break

    return (located, pos)


def seq_ordered_search(items, wanted):

    located = False
    pos = 0

    for pos, item in enumerate(items):
        if item == wanted:
            located = True
            break
        elif item > wanted:
            pos = None
            break
    return (located, pos)


class Sec_Search_Tester(unittest.TestCase):

    def test_seq_search(self):
        self.assertEquals(seq_search([], ''), (False, 0))
        self.assertNotEquals(seq_search([], ''), (True, 0))
        self.assertEquals(seq_search([], '1'), (False, 0))
        self.assertEquals(seq_search(['1'], '1'), (True, 0))
        self.assertEquals(seq_search(['1'], 1), (False, 0))
        self.assertEquals(seq_search([1], 1), (True, 0))
        self.assertEquals(seq_search([5,4,3,2,1], 1), (True, 4))
        self.assertEquals(seq_search([5,4,3,2,1], 11), (False, 4))
        self.assertEquals(seq_search([5,4, None, 'a', 3,2,'whelp',1], 'a'), (True, 3))
        self.assertEquals(seq_search([5,4, None, 'a', 3,2,'whelp',1], None), (True, 2))
        self.assertEquals(seq_search([5,4, None, [1,2,3], 'a', 3,2,'whelp',1], [1,2,3]), (True, 3))

    def test_seq_oredered_search(self):
        self.assertEquals(seq_ordered_search([], ''), (False, 0))
        self.assertNotEquals(seq_ordered_search([], ''), (True, 0))
        self.assertEquals(seq_ordered_search([1], 1), (True, 0))
        self.assertEquals(seq_ordered_search([1,2,3], 2), (True, 1))
        self.assertEquals(seq_ordered_search([1,2,3], 4), (False, 2))
        self.assertEquals(seq_ordered_search([1,2,3,5,6], 4), (False, None))
        

if __name__ == '__main__':
    unittest.main()
