# Algorithms and Data Structures: Recursion
# 03.29.2016
# @totallygloria

import unittest
from recursive_factorial import factorial_calc


class AdditionTester(unittest.TestCase):

    def test_factorial_calc(self):
        self.assertEquals(1, factorial_calc(1))
        self.assertEquals(2, factorial_calc(2))
        self.assertEquals(6, factorial_calc(3))
        self.assertEquals(24, factorial_calc(4))
        self.assertEquals(362880, factorial_calc(9))
        self.assertEquals(3628800, factorial_calc(10))


if __name__ == '__main__':
    unittest.main()
