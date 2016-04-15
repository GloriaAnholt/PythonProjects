# Algorithms & Data Structures: Recursive Exercises
# 04.15.16
# @totallygloria


import unittest
import timeit
import math


'''
Write a recursive function to compute the Fibonacci sequence.
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
Compare the performance of the recursive function to an iterative version.

Apparently, tail-end recursion is too big for the stack at fib 997th number.

The traditional answer is ridiculously ineffective, who came up with this?!
nth = 25, repeat = 100
0.00103282928467
5.89699888229
0.000303030014038
'''


def fib_calc(nth, count=1, a=0, b=1):

    if nth <= 1:
        return nth
    elif nth == count:
        return b
    else:
        return fib_calc(nth, count + 1, b, a + b)


def trad_fib(nth):

    if nth <= 1:
        return nth
    else:
        return(trad_fib(nth-1) + trad_fib(nth-2))


def fib_iterator(nth):

    a = 0; b = 1

    if nth <= 1:
        return nth
    else:
        for i in range(1, nth):
            total = a + b
            a = b
            b = total
    return total


def fib_math(nth):

    return (Phi ** nth - phi ** nth) / math.sqrt(5)


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

    def test_trad_fib(self):
        self.assertEqual(trad_fib(0), 0)
        self.assertEqual(trad_fib(1), 1)
        self.assertEqual(trad_fib(2), 1)
        self.assertEqual(trad_fib(3), 2)
        self.assertEqual(trad_fib(4), 3)
        self.assertEqual(trad_fib(5), 5)
        self.assertEqual(trad_fib(6), 8)
        self.assertEqual(trad_fib(7), 13)
        self.assertEqual(trad_fib(8), 21)
        self.assertEqual(trad_fib(9), 34)
        self.assertEqual(trad_fib(10), 55)
        self.assertEqual(trad_fib(11), 89)
        self.assertEqual(trad_fib(12), 144)
        self.assertEqual(trad_fib(13), 233)
        self.assertEqual(trad_fib(14), 377)
        self.assertEqual(trad_fib(15), 610)
        self.assertEqual(trad_fib(16), 987)

    def test_fib_iterator(self):
        self.assertEqual(fib_iterator(0), 0)
        self.assertEqual(fib_iterator(1), 1)
        self.assertEqual(fib_iterator(2), 1)
        self.assertEqual(fib_iterator(3), 2)
        self.assertEqual(fib_iterator(4), 3)
        self.assertEqual(fib_iterator(5), 5)
        self.assertEqual(fib_iterator(6), 8)
        self.assertEqual(fib_iterator(7), 13)
        self.assertEqual(fib_iterator(8), 21)
        self.assertEqual(fib_iterator(9), 34)
        self.assertEqual(fib_iterator(10), 55)
        self.assertEqual(fib_iterator(11), 89)
        self.assertEqual(fib_iterator(12), 144)
        self.assertEqual(fib_iterator(13), 233)
        self.assertEqual(fib_iterator(14), 377)
        self.assertEqual(fib_iterator(15), 610)
        self.assertEqual(fib_iterator(16), 987)

#if __name__ == '__main__':
#    unittest.main()

Phi = (1 + math.sqrt(5) ** 0.5) / 2
phi = (1 - math.sqrt(5) ** 0.5) / 2

if __name__ == '__main__':
    #print timeit.timeit("trad_fib(25)", number=100, setup="from __main__ import trad_fib")
    print timeit.timeit("fib_calc(996)", number=1000, setup="from __main__ import fib_calc")
    print timeit.timeit("fib_iterator(996)", number=1000, setup="from __main__ import fib_iterator")
    print timeit.timeit("fib_math(996)", number=1000, setup="from __main__ import fib_math" )