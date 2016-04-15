# Algorithms & Data Structures: Recursive Exercises
# 03.29.16
# @totallygloria


import unittest

'''
Write a recursive function to reverse a list.
'''


def reverser(original_list, reversed_list):

    if len(original_list) == 1:
        reversed_list.append(original_list[0])
    else:
        lastnum = original_list.pop()
        reversed_list.append(lastnum)
        reverser(original_list, reversed_list)

    return reversed_list





class ReverserTester(unittest.TestCase):

    def reverser(self):
        self.assertEqual(reverser([], []), [])
        self.assertEqual(reverser([1], []), [1])
        self.assertEqual(reverser([1,2,3,4,5], []), [5,4,3,2,1])
        self.assertEqual(reverser(['a','b','c','d'], []), ['d','c','b','a'])
        
        self.assertNotEquals(reverser([1,2,3,4,5], []), [1,2,3,4,5])






if __name__ == '__main__':
    unittest.main()