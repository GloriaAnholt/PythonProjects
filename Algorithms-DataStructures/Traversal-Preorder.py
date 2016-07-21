# Algorithms and Data Structures: Preorder Traversal of Binary Tree
# 07.20.2016
# @totallygloria



from BinaryTreeClass import BinaryTree

def preorder(tree):

    if tree:
        print tree.get_root()
        preorder(tree.get_lc())
        preorder(tree.get_rc())



oak = BinaryTree("A")
oak.insert_left("B")
oak.insert_right("C")
oak.lc.insert_left("D")
oak.lc.insert_right("E")

preorder(oak)