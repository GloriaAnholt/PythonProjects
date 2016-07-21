# Algorithms and Data Structures: Parse Tree
# 07.20.2016
# @totallygloria




'''
Implementation of a parse tree for fully parenthesized mathematical expressions.
Rules:
If the token is a ( add a new left child of the current node, descent to lc
If the token is a [+, -, *, \], set the root value of the current node to the operator
    add a new node as a right child and traverse to new rc
If the token is a number, set the key of the current node to that value, return to parent
If the token is ) traverse to the parent of the current node
'''

from StackClass import Stack
from BinaryTreeClass import BinaryTree
import operator


def buildparsetree(exp):
    plist = exp.split()
    pstack = Stack()
    tree = BinaryTree('')
    pstack.push(tree)
    current_tree = tree

    for item in plist:

        if item == '(':
            current_tree.insert_left('')
            pstack.push(current_tree)
            current_tree = current_tree.get_lc()

        elif item not in ['+', '-', '*', '/', ')']:
            current_tree.set_root(float(item))
            current_tree = pstack.pop()

        elif item in ['+', '-', '*', '/']:
            current_tree.set_root(item)
            current_tree.insert_right('')
            pstack.push(current_tree)
            current_tree = current_tree.get_rc()

        elif item == ')':
            current_tree = pstack.pop()

        else:
            raise ValueError

    return tree


def pt_evaluator(subtree):

    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    lc = subtree.get_lc()
    rc = subtree.get_rc()

    if lc and rc:
        fn = opers[subtree.get_root()]
        return fn(pt_evaluator(lc), pt_evaluator(rc))
    else:
        return subtree.get_root()


pt = buildparsetree("( ( 10 + 5 ) * 3 ) ")
print pt_evaluator(pt)