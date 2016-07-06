# Algorithms and Data Structures: Shell Sort
# 07.05.2016
# @totallygloria

"""
Implementation of a shell (diminishing increment) sort.
The list is divided into sublists by a step, the elements hit by the step
are sorted relative to each other but not the entire list, then the step-set
advances by one and the next subset is sorted. Repeat until entire list is hit,
then insertion sort with a step of 1 the more-sorted list.
"""


def shellsort(unsorted):

    length = len(unsorted)
    gap = length // 2

    while gap > 0:
        for i in range(gap, length):
            key = unsorted[i]
            while i >= gap and unsorted[i - gap] > key:
                # If the earlier element is larger than the key, copy it over the key's slot
                unsorted[i] = unsorted[i - gap]
                # Adjust the index down the the previous step by the gap, check again
                i -= gap
            # Overwrite the earliest step with the value of the key; if sorted, does nothing
            unsorted[i] = key
        gap = gap // 2



tester = [13, 6, 9, 4, 18, 16, 7, 3, 1]
alist = [54, 26, -93, 17, 77, 31, 0, -44, 55, 20]
alreadysorted = [1, 2, 3, 4, 5, 6, 7, 7, 8]
shellsort(tester)
print tester
shellsort(alist)
print alist
shellsort(alreadysorted)
print alreadysorted