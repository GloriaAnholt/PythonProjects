# Algorithms and Data Structures: Quick Sort
# 05.06.2016
# @totallygloria

"""
Implementation of the quick sort.
Quick sort is a divide and conquer algorithm which selects an element as a pivot
point and then walks the remainder of the list from the outsides in swapping elements
to their correct location before or after the pivot point, finally swapping the pivot
into place.
"""


def quicksort(unsorted):

    # Select the pivot as the median of first-last-middle
    first = unsorted[0]
    last = unsorted[-1]
    middle = unsorted[(len(unsorted)//2)]

    if (last < first < middle) or (middle < first < last):
        pivot = first
    elif (first < middle < last) or (last < middle < first):
        pivot = middle
    else:
        pivot = last

    print pivot


quicksort([9,1,2,200,4,5,-5])