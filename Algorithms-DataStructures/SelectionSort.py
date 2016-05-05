# Algorithms and Data Structures: Selection Sort
# 05.05.2016
# @totallygloria

"""
Implementation of a selection sort.
On each pass, the largest element is found and placed where it belongs,
moving from placing at the end of the list, inwards.
"""


def selectionsort(unsorted):
    """ unsorted: Returns a sorted list using a selection sort. """

    for last in range(len(unsorted)-1, 0, -1):
        largest = 0
        for current in range(1, last+1):
            if unsorted[current] > unsorted[largest]:
                largest = current
        unsorted[last], unsorted[largest] = unsorted[largest], unsorted[current]

    return unsorted


print selectionsort([0,1,2,3,4,5,6,7,8,9])
print selectionsort([9,8,7,6,5,4,3,2,1,0])
print selectionsort([50,50,50,50,1])
print selectionsort([1, 9, 19, 7, 3, 10, 13, 15, 8, 12])


