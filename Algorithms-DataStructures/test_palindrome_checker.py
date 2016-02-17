# Data Structures and Algorithms: Palindrome checker
# 02.17.16
# @totallygloria


import unittest
import sys
from StringIO import StringIO

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

    def test_user_input(self):
        control = "banana"
        test_input = StringIO("banana")
        sys.stdin = test_input
        sys.stdout = StringIO()
        testcase = palindrome_checker.user_input()
        self.assertEqual(testcase, control)


    def test_pal_checker(self):
        deque = Deque()
        for letter in 'level':
            deque.addfront(letter)
        self.assertTrue(palindrome_checker.pal_checker(deque))
        dtwo = Deque()
        for letter in 'banana':
            dtwo.addrear(letter)
        self.assertFalse(palindrome_checker.pal_checker(dtwo))
        dthree = Deque()
        for letter in 'abba':
            deque.addfront(letter)
        self.assertTrue(palindrome_checker.pal_checker(dthree))

if __name__ == '__main__':
    unittest.main()