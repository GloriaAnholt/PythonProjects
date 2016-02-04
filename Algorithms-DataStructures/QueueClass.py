# Data Structures and Algorithms: Queue
# 01.04.16
# @totallygloria


class Queue(object):
    def __init__(self):
        self.first = None
        self.last = None
        self.queue_size = 0

    def enqueue(self, item):
        # takes an item, adds to the end of queue, returns nothing
        new_element = Element(item)

        if self.is_empty():
            self.first = new_element
        else:
            self.last.behind = new_element

        self.last = new_element
        self.queue_size += 1

    def dequeue(self):
        # takes no args, removes and returns front item
        removed = self.first
        self.first = self.first.behind
        self.queue_size -= 1
        return removed.item

    def size(self):
        # takes no args, returns an int
        return self.queue_size

    def inefficient_size(self):
    # walks list from front, returns an int. Should be O(n) to calculate
        counter = 0
        current = self.first
        while current != None:
            counter +=1
            current = current.behind
        return counter

    def is_empty(self):
        return self.first == None

    def has_items(self):
        # takes no args, returns a boolean
        return not self.is_empty()


class Element(object):
    def __init__(self, value):
        self.item = value
        self.behind = None














