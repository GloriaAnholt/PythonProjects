# Data Structures and Algorithms: Queue
# 01.04.16
# @totallygloria


class Queue(object):
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, item):
        # takes an item, adds to the end of queue, returns nothing
        new_element = Element(item)
        new_element.ahead = self.last
        self.last = new_element

        if self.is_empty():
            self.first = new_element

    def dequeue(self):
        # takes no args, removes and returns front item
        removed = self.queue.behind

 #   def size(self):
 #       # takes no args, returns an int
 #       return len(self.queue)

    def is_empty(self):
        return self.first == None

    def has_items(self):
        # takes no args, returns a boolean
        return not self.is_empty()

class Element(object):
    def __init__(self, value):
        self.item = value
        self.ahead = self













