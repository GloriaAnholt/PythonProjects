# Algorithms and Data Structures: Insertion Sort
# 05.06.2016
# @totallygloria

"""
Implementation of a insertion sort.
The first element is 'sorted' into its current place, then the algorithm
walks the list to the next unsorted element, and slides elements over until
the correct spot is found and it is reinserted into the list. The list turns
into a sorted front and unsorted back as it runs, completing when the last
element is slid into its spot.
"""


def insertionsort(unsorted):

    key = None

    for i in range(len(unsorted)):
        key = unsorted[i]
        for j in range(i-1, -1, -1):
            if key >= unsorted[j]:
                break
            else:
                key < unsorted[j]
                unsorted[j+1] = unsorted[j]
            unsorted[j] = key
    return unsorted


print insertionsort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
print insertionsort([10, 9, 8, 22, 7, 6, 35, 5, 4, 3, 41, 2, 1, 100, 0])
