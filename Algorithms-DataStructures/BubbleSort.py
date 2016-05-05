# Algorithms and Data Structures: Bubble Sort
# 05.05.2016
# @totallygloria


"""
This is a basic implementation of a 'short' bubble sort.
Each item in a list is compared to it's neighbor, and is moved up the list if it is larger.
If smaller, the larger item is then compared and moved up the list until a larger item or
the EOL is found. Runs until no swaps are made.
"""


def bubblesort(unsorted):
    """ Returns a sorted list. """

    sorted = False
    eol = 1

    while not sorted:
        swaps = False
        for i in range(len(unsorted) - eol):
            if unsorted[i] > unsorted[i+1]:
                unsorted[i], unsorted[i+1] = unsorted[i+1], unsorted[i]
                swaps = True
        if swaps is False:
            sorted = True
        else:
            eol += 1

    return unsorted


print bubblesort([5,6,3,4,1])
print bubblesort([50,396,63,904,1])
print bubblesort([1, 9, 19, 7, 3, 10, 13, 15, 8, 12])
