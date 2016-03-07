# Algorithms and Data Structures: Recursion
# 03.07.2016
# @totallygloria

import unittest
from rec_palindrome_checker import palindrome_checker


class PalindromeTester(unittest.TestCase):

    def test_palindrome_checker(self):

        self.assertEqual(palindrome_checker(''), True)
        self.assertEqual(palindrome_checker('!!'), True)
        self.assertEqual(palindrome_checker('a'), True)
        self.assertEqual(palindrome_checker('bb'), True)
        self.assertEqual(palindrome_checker('ccc'), True)
        self.assertEqual(palindrome_checker('aba'), True)
        self.assertEqual(palindrome_checker('abba'), True)
        self.assertEqual(palindrome_checker('abbba'), True)
        self.assertEqual(palindrome_checker('abcba'), True)
        self.assertEqual(palindrome_checker('abccba'), True)
        self.assertEqual(palindrome_checker('abcdcba'), True)
        self.assertEqual(palindrome_checker('abcddcba'), True)
        self.assertEqual(palindrome_checker('madamimadam'), True)
        self.assertEqual(palindrome_checker("madam, i'm adam"), True)

        self.assertEqual(palindrome_checker('ab'), False)
        self.assertEqual(palindrome_checker('abc'), False)
        self.assertEqual(palindrome_checker('aabb'), False)
        self.assertEqual(palindrome_checker('aabbc'), False)
        self.assertEqual(palindrome_checker('aabbcc'), False)
        self.assertEqual(palindrome_checker('aabb##@%!!#$%$##'), False)
        self.assertEqual(palindrome_checker('hello'), False)

if __name__ == '__main__':
    unittest.main()
