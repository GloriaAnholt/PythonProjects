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
        return unsorted
    else:
        exchanger(unsorted, 0, len(unsorted) - 1)


def exchanger(unsorted, start, stop):

    if stop - start > 0:  # Nope out for an empty set
        pivot = getpivot(unsorted, start, stop)
        lmark = start
        rmark = stop

        while lmark <= rmark:
            while unsorted[lmark] < pivot: # and lmark < rmark:
                lmark += 1
            while unsorted[rmark] > pivot: # and lmark < rmark:
                rmark -= 1
            if lmark <= rmark:
                unsorted[lmark], unsorted[rmark] = unsorted[rmark], unsorted[lmark]
                lmark += 1
                rmark -= 1

        print unsorted, lmark, rmark, start, stop

        exchanger(unsorted, start, rmark)  # sort the left side
        exchanger(unsorted, lmark, stop)  # sort the right side



def getpivot(unsorted, start, stop):
    # Select the pivot as the median of first-last-middle
    first = unsorted[start]
    last = unsorted[stop]
    middle = unsorted[(start + stop) // 2]

    if (last <= first <= middle) or (middle <= first <= last):
        return first                # Pivot is first element, or there are equals
    elif (first < middle < last) or (last < middle < first):
        return middle               # Pivot is midpoint
    else:
        return last                 # Pivot is last element


tester = [9,5,16,13,4,10,8,17,11,18,15,3,12,7,2,19,6,1,20,11,11,11,-10]
quicksort(tester)
print "final list is:", tester