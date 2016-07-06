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

    setpivot(unsorted)
    mid = len(unsorted) // 2
    pivot = unsorted[mid]

    front = 0
    back = len(unsorted)

    for i in range(mid):
        if unsorted[front] < pivot:
            front += 1
        


def setpivot(unsorted):
    # Select the pivot as the median of first-last-middle
    mid = len(unsorted) // 2
    first = unsorted[0]
    last = unsorted[-1]
    middle = unsorted[mid]

    if (last <= first <= middle) or (middle < first < last):
        temp = middle                   # Pivot is first element, or they're all equal
        unsorted[mid] = first           # Swap first element to middle
        unsorted[0] = temp
        print "first case: ", unsorted[mid]
    elif (first < last < middle) or (first > last > middle):
        temp = middle                   # Pivot is last element
        unsorted[mid] = last           # Swap last element to middle
        unsorted[-1] = temp
        print "last case: ", unsorted[mid]
    else:
        print "middle is where it belongs"




setpivot([1,2,2,3])