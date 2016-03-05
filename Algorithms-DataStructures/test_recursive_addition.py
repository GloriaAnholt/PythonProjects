# Algorithms and Data Structures: Recursion
# 03.04.2016
# @totallygloria

import unittest
from recursive_addition import Adder


class AdditionTester(unittest.TestCase):

    def test_Adder(self):
        known_sum = 0
        known_list = []
        for i in range(11):
            known_sum += i
            known_list.append(i)
        print known_sum

        self.assertEquals(known_sum, Adder(known_list))



if __name__ == '__main__':
    unittest.main()
