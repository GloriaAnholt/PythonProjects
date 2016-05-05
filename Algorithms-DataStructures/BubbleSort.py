# Algorithms and Data Structures: Bubble Sort
# 05.05.2016
# @totallygloria


"""
This is a basic implementation of a bubble sort.
Each item in a list is compared to it's neighbor, and is moved up the list if it is larger.
If smaller, the larger item is then compared and moved up the list until a larger item or
the EOL is found. Runs until no swaps are made.
"""


def bubblesort(unsorted):
    """ Returns a sorted list. """

    sorted = False

    while not sorted:
        swaps = False
        for i in range(len(unsorted) - 1):
            if unsorted[i] > unsorted[i+1]:
                temp = unsorted[i]
                unsorted[i] = unsorted[i+1]
                unsorted[i+1] = temp
                swaps = True
        if swaps is False:
            sorted = True

    return unsorted


print bubblesort([5,6,3,4,1])

print bubblesort([52,36,63,904,1])
