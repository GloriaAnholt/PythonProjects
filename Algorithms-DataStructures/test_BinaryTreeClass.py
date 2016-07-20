# Algorithms and Data Structures: Quick Sort
# 07.20.2016
# @totallygloria

import unittest
from BinaryTreeClass import BinaryTree


class BinaryTreeTester(unittest.TestCase):

    def test_BinaryTree(self):
        # Check if you can make a new node of different types, or change types
        t1 = BinaryTree("maple")
        self.assertEquals(t1.key, "maple")
        t1.key = "oak"
        self.assertEquals(t1.key, "oak")
        t1.key = 0
        self.assertEquals(t1.key, 0)
        t1.key = [1, 2, 3]
        self.assertEquals(t1.key, [1, 2, 3])
        t2 = BinaryTree(0)
        self.assertEquals(t2.key, 0)
        t3 = BinaryTree([])
        self.assertEquals(t3.key, [])
        # Check that you can set the nodes
        t1.lc = "left leaf"
        t1.rc = "right leaf"
        self.assertEquals(t1.lc, "left leaf")
        self.assertEquals(t1.rc, "right leaf")

    def test_insert_left(self):
        t1 = BinaryTree("redwood")
        t1.insert_left("left branch")
        self.assertEquals(t1.lc.key, "left branch")
        t1.insert_left("new branch")
        self.assertEquals(t1.lc.key, "new branch")
        self.assertEquals(t1.lc.lc.key, "left branch")

    def test_insert_right(self):
        t1 = BinaryTree("cypress")
        t1.insert_right("right branch")
        self.assertEquals(t1.rc.key, "right branch")
        t1.insert_right("new branch")
        self.assertEquals(t1.rc.key, "new branch")
        self.assertEquals(t1.rc.rc.key, "right branch")

    def test_set_root(self):
        t1 = BinaryTree("cedar")
        t1.key = "oak"
        self.assertEquals(t1.key, "oak")
        t1.set_root("maple")
        self.assertEquals(t1.key, "maple")
        t1.set_root(100)
        self.assertEquals(t1.key, 100)

    def test_get(self):
        t1 = BinaryTree("pine")
        t1.insert_right("right branch")
        t1.insert_left("left branch")
        self.assertEquals(t1.get_rc(), "right branch")
        self.assertEquals(t1.get_lc(), "left branch")
        self.assertEquals(t1.get_root(), "pine")
        t1.insert_right("right stick")
        t1.insert_left("left stick")
        t1.set_root("hemlock")
        self.assertEquals(t1.get_rc(), "right stick")
        self.assertEquals(t1.get_lc(), "left stick")
        self.assertEquals(t1.get_root(), "hemlock")

if __name__ == '__main__':
    unittest.main()
