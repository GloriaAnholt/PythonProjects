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
        for i in range(length - gap):
            print "i equals", i
            if unsorted[i] < unsorted[i + gap]:
                pass
            else:
                temp = unsorted[i]
                unsorted[i] = unsorted[i + gap]
                unsorted[i + gap] = temp

            print unsorted

        gap = gap // 2

    return unsorted


tester = [13, 6, 9, 4, 18, 16, 7, 3, 1]
shellsort(tester)
print tester