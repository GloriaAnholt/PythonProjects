# Algorithms and Data Structures: Binary Tree
# 07.20.2016
# @totallygloria


'''
Implementation of a Binary Tree using a python class.
'''


class BinaryTree(object):

    def __init__(self, value):
        self.key = value
        self.lc = None
        self.rc = None

    def insert_left(self, node, value):

        newnode = NodeClass(value)

        if node.lc is None:
            node.lc = newnode
        else:
            newnode.lc = node.lc
            node.lc = newnode


class NodeClass(object):

    def __init__(self, value):
        self.key = value
        self.lc = None
        self.rc = None


mytree = BinaryTree("oak")
mytree.insert_left(mytree, "branch")
mytree.insert_left(mytree.lc, "stick")
mytree.insert_left(mytree.lc.lc, "twig")

print mytree.key
print mytree.lc.key
print mytree.lc.lc.key
print mytree.lc.lc.lc.key
