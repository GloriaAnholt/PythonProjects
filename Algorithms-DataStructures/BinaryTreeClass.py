# Algorithms and Data Structures: Binary Tree
# 07.20.2016
# @totallygloria



class BinaryTree(object):
    """ Implementation of a Binary Tree using a python class. """

    def __init__(self, value):
        self.key = value
        self.lc = None
        self.rc = None

    def insert_left(self, value):

        newnode = BinaryTree(value)

        if self.lc is None:
            self.lc = newnode
        else:
            newnode.lc = self.lc
            self.lc = newnode

    def insert_right(self, value):

        newnode = BinaryTree(value)

        if self.rc is None:
            self.rc = newnode
        else:
            newnode.rc = self.rc
            self.rc = newnode

    def get_lc(self):
        return self.lc

    def get_rc(self):
        return self.rc

    def set_root(self, newval):
        self.key = newval

    def get_root(self):
        return self.key

    def preorder(self):

        print self.key
        if self.lc:
            self.lc.preorder()
        if self.rc:
            self.rc.preorder()



oak = BinaryTree("A")
oak.insert_left("B")
oak.insert_right("C")
oak.lc.insert_left("D")
oak.lc.insert_right("E")

oak.preorder()