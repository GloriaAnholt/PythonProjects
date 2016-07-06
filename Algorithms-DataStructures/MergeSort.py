# Algorithms and Data Structures: Merge Sort
# 07.06.2016
# @totallygloria

"""
Implementation of a merge sort.
Merge sort is a recursive algorithm that continually splits a list in half: if the
list is empty or has one item, it is sorted by definition (base case). If the list
has more than one item, the list is split and a merge sort is recursively invoked
on both halves. Once base case is reached on all branches, a merge is performed.
"""


def mergesort(unsorted):

    if len(unsorted) > 1:
        midpoint = len(unsorted) // 2
        mergesort(unsorted[:midpoint])
        mergesort(unsorted[midpoint:])

    else:
        print unsorted


mergesort([1,2,3,4,5,6,7,8,9,10])