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

class QuickSort(object):

    def __init__(self):
        self.array = []

    def quicksort(self):

        if len(self.array) <= 1:      # Nope out for an empty or one-element array
            return self.array
        else:
            self.exchanger(0, len(self.array) - 1)

    def exchanger(self, start, stop):

        if stop - start <= 0:  # Nope out for an empty set
            return
        else:
            pivot = self.getpivot(start, stop)
            lmark = start
            rmark = stop

            while lmark <= rmark:
                while self.array[lmark] < pivot:
                    lmark += 1
                while self.array[rmark] > pivot:
                    rmark -= 1
                if lmark <= rmark:
                    self.array[lmark], self.array[rmark] = self.array[rmark], self.array[lmark]
                    lmark += 1
                    rmark -= 1

            self.exchanger(start, rmark)  # sort the left side
            self.exchanger(lmark, stop)  # sort the right side

    def getpivot(self, start, stop):
        # Select the pivot as the median of first-last-middle
        first = self.array[start]
        last = self.array[stop]
        middle = self.array[(start + stop) // 2]

        if (last <= first <= middle) or (middle <= first <= last):
            return first                # Pivot is first element, or there are equals
        elif (first < middle < last) or (last < middle < first):
            return middle               # Pivot is midpoint
        else:
            return last                 # Pivot is last element

'''
t1 = QuickSort()
t1.array = [9, 5, 16, 13, 4, 10, 8, 17, 11, 18, 15, 3, 12, 7, 2, 19, 6, 1, 20, 11, 11, 11, -10]
print "starting list is:", t1.array
t1.quicksort()
print "final list is:", t1.array
'''