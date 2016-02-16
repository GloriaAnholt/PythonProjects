# Data Structures and Algorithms: Queue
# 02.15.16
# @totallygloria


import unittest

from DequeClass import Deque


class DequeTester(unittest.TestCase):

    def test_is_empty(self):
        deque = Deque()
        self.assertTrue(deque.isempty())
        self.assertEqual(deque.size, 0)
        deque.addfront('an item')
        self.assertFalse(deque.isempty())
        self.assertEqual(deque.size, 1)

    def test_addfront(self):
        deque = Deque()
        deque.addfront('apples')
        self.assertEqual(deque.first.item, 'apples')
        self.assertEqual(deque.last.item, 'apples')
        deque.addfront('bananas')
        self.assertEqual(deque.first.item, 'bananas')
        self.assertEqual(deque.last.item, 'apples')
        deque.addfront('cherries')
        self.assertEqual(deque.size, 3)
        self.assertEqual(deque.first.item, 'cherries')

    def test_addrear(self):
        deque = Deque()
        deque.addrear('cow')
        self.assertEqual(deque.first.item, 'cow')
        self.assertEqual(deque.last.item, 'cow')
        deque.addrear('donkey')
        self.assertEqual(deque.first.item, 'cow')
        self.assertEqual(deque.last.item, 'donkey')
        deque.addrear('elephant')
        self.assertEqual(deque.size, 3)
        self.assertEqual(deque.first.item, 'cow')
        self.assertEqual(deque.last.item, 'elephant')




if __name__ == '__main__':
    unittest.main()