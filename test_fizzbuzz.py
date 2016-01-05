# Programming Problems: Implement a Fizz Buzz Counter
# 12.29.2015
# @totallygloria

import unittest
from fizzbuzz import fizzbuzz_generator


class FBTester(unittest.TestCase):

    def test_first_ten_fb(self):
        self.assertEquals(fizzbuzz_generator(10),
                          [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz'],
                          msg='First ten match')

    def test_incorrect_seq(self):
        self.assertNotEquals(fizzbuzz_generator(10),
                             [1, 2, 'Fizz', 'Fizz', 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz'],
                             msg='Caught the mismatch')


if __name__ == '__main__':
    unittest.main()
