# Algorithms and Data Structures: Binary Tree
# 05.06.2016
# @totallygloria


'''
Implementation of a binary tree using lists of lists, where the structure is recursive.
The root of the tree is myTree[0], the left subtree of the root is myTree[1],
and the right subtree is myTree[2].
In the case where the tree is more than a binary tree, another subtree is just another list.
'''


def create_tree(r):

    return [r, [], [] ]


def insert_left(root, newbranch):

    subtree = root.pop(1)       # 0 is root, 1 is left branch
    if len(subtree > 1):
        root.insert(1, [newbranch, subtree, [] ])
    else:
        root.insert(1, [newbranch, [], [] ])

    return root


def insert_right(root, newbranch):

    subtree = root.pop(2)       # 0 is root, 2 is right branch
    if len(subtree > 1):
        root.insert(2, [newbranch, [], subtree])
    else:
        root.insert(2, [newbranch, [], []])

    return root


def get_root(root):
    return root[0]


def set_root(root, newval):
    root[0] = newval


def get_left(root):
    return root[1]


def get_right(root):
    return root[2]


'''
Example of a tree structure:
mytree = ['a',  # root
          ['b', # left subtree
           ['d', [], [] ],
           ['e', [], [] ] ],
          ['c', # right subtree
           ['f', [], [] ],
           [] ]
          ]

print mytree
print "Root is", mytree[0]
print "Left subtree", mytree[1]
print "Right subtree", mytree[2]
'''