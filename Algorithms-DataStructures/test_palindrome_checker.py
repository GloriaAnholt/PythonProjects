# Data Structures and Algorithms: Palindrome checker
# 02.17.16
# @totallygloria


import unittest

from DequeClass import Deque
import palindrome_checker


class PalindromeTester(unittest.TestCase):

    def test_build_deque(self):
        deque = Deque()
        deque.addrear('a')
        deque.addrear('b')
        deque.addrear('c')
        pal = palindrome_checker.build_deque('abc')
        self.assertEqual(deque.size, pal.size)
        self.assertEqual(deque.removefront(), pal.removefront())
        self.assertEqual(deque.removerear(), pal.removerear())
        self.assertEqual(deque.size, pal.size)
        self.assertEqual(deque.removefront(), pal.removefront())
        self.assertEqual(deque.size, 0)
        self.assertEqual(pal.size, 0)


if __name__ == '__main__':
    unittest.main()