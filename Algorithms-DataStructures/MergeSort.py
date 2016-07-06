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

    if len(unsorted) > 1:                   # If the list is longer than 1, keep splitting
        midpoint = len(unsorted) // 2
        left = unsorted[:midpoint]
        right = unsorted[midpoint:]
        mergesort(left)
        mergesort(right)

        l, r, i = 0, 0, 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:         # If the left is smaller, add to list (preserves order)
                unsorted[i] = left[l]
                l += 1
            else:
                unsorted[i] = right[r]      # Otherwise, r is smaller so add the right element
                r += 1
            i += 1

        while l < len(left):                # If there's any left-list remaining, add them
            unsorted[i] = left[l]
            l += 1
            i += 1

        while r < len(right):               # Otherwise, if any r-side remaining, add them
            unsorted[i] = right[r]
            r += 1
            i += 1


a = [98,76,54,43,21,0,-12]
b = [1,2,3,4,5,8,1,2,3,9,-1,0]
c = [9,8,7,6,5,4,3,2,1,0,-1]
mergesort(a)
mergesort(b)
mergesort(c)
print a
print b
print c