# Algorithms & Data Structures: Recursive Exercises
# 03.29.16
# @totallygloria


import unittest


'''
Write a recursive function to compute the factorial of a number
'''


def factorial_calc(num):

    if num <= 1:
        return 1
    else:
        total = num * factorial_calc(num-1)

    return total


class Factorial_Calc_Tester(unittest.TestCase):

    def factorial_calc(self):
        self.assertEqual(factorial_calc(0), 1)
        self.assertEqual(factorial_calc(-243), 1)
        self.assertEqual(factorial_calc(2), 2)
        self.assertEqual(factorial_calc(5), 120)
        self.assertEqual(factorial_calc(9), 362880)

        self.assertNotEquals(factorial_calc(4), 12)


if __name__ == '__main__':
    unittest.main()


