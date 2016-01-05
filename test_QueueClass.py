# Data Structures and Algorithms: Queue
# 01.04.16
# @totallygloria


import unittest

from QueueClass import Queue


class QueueTester(unittest.TestCase):

    def test_is_empty(self):
        schwerns_queue = Queue()
        self.assertTrue(schwerns_queue.is_empty())
        schwerns_queue.enqueue('dicks')
        self.assertFalse(schwerns_queue.is_empty())

    def test_has_items(self):
        queue = Queue()
        self.assertFalse(queue.has_items())
        queue.enqueue('a thing')
        self.assertTrue(queue.has_items())


if __name__ == '__main__':
    unittest.main()
