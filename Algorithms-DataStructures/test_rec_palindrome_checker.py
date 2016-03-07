# Algorithms and Data Structures: Recursion
# 03.07.2016
# @totallygloria

import unittest
from rec_palindrome_checker import palindrome_checker


class PalindromeTester(unittest.TestCase):

    def test_palindrome_checker(self):

        self.assertTrue(palindrome_checker(''))
        self.assertTrue(palindrome_checker('!!'))
        self.assertTrue(palindrome_checker('a'))
        self.assertTrue(palindrome_checker('bb'))
        self.assertTrue(palindrome_checker('ccc'))
        self.assertTrue(palindrome_checker('aba'))
        self.assertTrue(palindrome_checker('abba'))
        self.assertTrue(palindrome_checker('abbba'))
        self.assertTrue(palindrome_checker('abcba'))
        self.assertTrue(palindrome_checker('abccba'))
        self.assertTrue(palindrome_checker('abcdcba'))
        self.assertTrue(palindrome_checker('abcddcba'))
        self.assertTrue(palindrome_checker('madamimadam'))
        self.assertTrue(palindrome_checker("madam, i'm adam"))

        self.assertFalse(palindrome_checker('ab'))
        self.assertFalse(palindrome_checker('abc'))
        self.assertFalse(palindrome_checker('aabb'))
        self.assertFalse(palindrome_checker('aabbc'))
        self.assertFalse(palindrome_checker('aabbcc'))
        self.assertFalse(palindrome_checker('aabb##@%!!#$%$##'))

if __name__ == '__main__':
    unittest.main()
