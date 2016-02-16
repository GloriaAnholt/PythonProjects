# Algorithms & Data Structures: Deque
# 02.15.16
# @totallygloria


class Deque(object):
    # creates a new deque that is empty. It needs no parameters and returns an empty deque.
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def addfront(self, item):
        # adds a new item to the front of the deque. It needs the item and returns nothing.
        new_element = Element(item)
        if self.size >= 1:
            self.first.ahead = new_element
            new_element.behind = self.first
            self.first = new_element
        elif self.size == 0:
            self.first = new_element
            self.last = new_element
        self.size += 1

    def addrear(self, item):
        # adds a new item to the rear of the deque. It needs the item and returns nothing.
        new_element = Element(item)
        if self.size >= 1:
            self.last.behind = new_element
            new_element.ahead = self.last
            self.last = new_element
        elif self.size == 0:
            self.first = new_element
            self.last = new_element
        self.size += 1

    def removefront(self):
        # removes the front item from the deque. It needs no parameters and returns the item.
        # The deque is modified.
        removed = self.first
        self.first = self.first.behind
        self.size -= 1
        return removed.item

    def removerear(self):
        # removes the rear item from the deque. It needs no parameters and returns the item.
        # The deque is modified.
        removed = self.last
        self.last = self.last.ahead
        self.size -= 1
        return removed.item

    def isempty(self):
        # tests to see whether the deque is empty. It needs no parameters and returns a boolean value.
        if self.size >= 1:
            return False
        return True

    def size(self):
        # returns the number of items in the deque. It needs no parameters and returns an integer.
        return self.size


class Element(object):
    def __init__(self, value):
        self.item = value
        self.ahead = None
        self.behind = None
