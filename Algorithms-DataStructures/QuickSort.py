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

    if len(unsorted) <= 1:      # Nope out for an empty or one-element array
        print "noping out"
        return unsorted
    else:
        exchanger(unsorted, 0, len(unsorted) - 1)


def exchanger(unsorted, start, stop):
    pivot = getpivot(unsorted, start, stop)
    print "pivot is", pivot, "start is", start, "stop is", stop
    print unsorted

    lmark = start
    rmark = stop

    while lmark < rmark:

        while unsorted[lmark] < pivot and lmark < rmark:
            lmark += 1
        while unsorted[rmark] > pivot and lmark < rmark:
            rmark -= 1

        temp = unsorted[lmark]
        unsorted[lmark] = unsorted[rmark]
        unsorted[rmark] = temp

    print unsorted
    if start < stop:
        exchanger(unsorted, start, lmark-1)  # sort the left side
        exchanger(unsorted, rmark+1, stop)


def getpivot(unsorted, start, stop):
    # Select the pivot as the median of first-last-middle
    first = unsorted[start]
    last = unsorted[stop]
    middle = unsorted[(start + stop) // 2]

    # Need to be able to write over where the pivot was safely, so put the pivot in first
    if (last <= first <= middle) or (middle <= first <= last):
        return first                # Pivot is first element, or there are equals
    elif (first < middle < last) or (last < middle < first):
        unsorted[(start + stop) // 2] = first
        unsorted[start] = middle
        return middle               # Pivot is midpoint, move to front
    else:
        unsorted[start] = last
        unsorted[stop] = first
        return last                 # Pivot is last element, move to front



quicksort([9,5,16,13,4,10,8,17,11,15,3,12,7,2,19,6,1,0])
