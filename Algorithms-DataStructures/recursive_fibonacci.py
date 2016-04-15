# Algorithms & Data Structures: Recursive Exercises
# 04.15.16
# @totallygloria


import unittest


'''
Write a recursive function to compute the Fibonacci sequence.
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
Compare the performance of the recursive function to an iterative version.
'''


def fib_calc(nth, count=1, a=0, b=1):

    if nth <= 1:
        return nth
    elif nth == count:
        return b
    else:
        print nth, count, a, b
        return fib_calc(nth, count + 1, b, a + b)


class Fib_Calc_Tester(unittest.TestCase):

    def test_fib_calc(self):
        self.assertEqual(fib_calc(0), 0)
        self.assertEqual(fib_calc(1), 1)
        self.assertEqual(fib_calc(2), 1)
        self.assertEqual(fib_calc(3), 2)
        self.assertEqual(fib_calc(4), 3)
        self.assertEqual(fib_calc(5), 5)
        self.assertEqual(fib_calc(6), 8)
        self.assertEqual(fib_calc(7), 13)
        self.assertEqual(fib_calc(8), 21)
        self.assertEqual(fib_calc(9), 34)
        self.assertEqual(fib_calc(10), 55)
        self.assertEqual(fib_calc(11), 89)
        self.assertEqual(fib_calc(12), 144)
        self.assertEqual(fib_calc(13), 233)
        self.assertEqual(fib_calc(14), 377)
        self.assertEqual(fib_calc(15), 610)
        self.assertEqual(fib_calc(16), 987)



if __name__ == '__main__':
    unittest.main()


