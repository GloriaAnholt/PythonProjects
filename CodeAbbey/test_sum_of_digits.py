# CodeAbbey: Problem 11 - Sum of digits in a calculated number
# 1.05.2016
# @totallygloria

import unittest
from sum_of_digits import initial_math

class SumTester(unittest.TestCase):

    def test_initial_math(self):
        self.assertEquals(initial_math([[3,5,2],[1,1,1]]), [17,2])
        self.assertNotEquals(initial_math([[2,2,2],[0,0,2]]),[40,1])



if __name__ == '__main__':
    unittest.main()
