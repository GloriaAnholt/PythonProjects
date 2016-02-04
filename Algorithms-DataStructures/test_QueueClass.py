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

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue('thingi')
        self.assertEqual(queue.dequeue(), 'thingi')
        self.assertTrue(queue.is_empty())

    def test_size(self):
        queue = Queue()
        self.assertEqual(queue.size(), 0)
        self.assertEqual(queue.inefficient_size(), 0)
        queue.enqueue('thing 1')
        queue.enqueue('thing2')
        queue.enqueue('thing3')
        self.assertEqual(queue.size(), 3, 'size works')
        self.assertEqual(queue.inefficient_size(), 3, 'inefficient_size works')
        queue.dequeue()
        self.assertEqual(queue.size(), 2)
        self.assertEqual(queue.size(), queue.inefficient_size(), 'size methods equal')


if __name__ == '__main__':
    unittest.main()
