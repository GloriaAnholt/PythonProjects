# Data Structures and Algorithms: List Class
# 02.17.16
# @totallygloria


class List(object):

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def add(self, item):
        # adds a new item to the list. It needs the item and returns nothing.
        # Assume the item is not already in the list.
        new_item = Element(item)
        if self.size == 0:
            self.first = new_item
            self.last = new_item
        else:
            new_item.ahead = self.last
            self.last.behind = new_item
            self.last = new_item
        self.size += 1


    def remove(self, item):
        # removes the item from the list. It needs the item and modifies the list.
        # Assume the item is present in the list.
        pass

    def search(self, item):
        # searches for the item in the list. It needs the item and returns a boolean value.
        pass

    def is_empty(self):
        # tests to see whether the list is empty. It needs no parameters and returns a boolean value.
        pass

    def size(self):
        # returns the number of items in the list. It needs no parameters and returns an integer.
        pass

    def append(self, item):
        # adds a new item to the end of the list making it the last item in the collection.
        # It needs the item and returns nothing. Assume the item is not already in the list.
        pass

    def index(self, item):
        # returns the position of item in the list. It needs the item and returns the index.
        # Assume the item is in the list.
        pass

    def insert(self, pos, item):
        # adds a new item to the list at position pos. It needs the item and returns nothing.
        # Assume the item is not already in the list and there are enough existing items
        # to have position pos.
        pass

    def pop(self):
        # removes and returns the last item in the list. It needs nothing and returns an item.
        # Assume the list has at least one item.
        pass

    def grab(self, pos):
        # removes and returns the item at position pos. It needs the position and returns the item.
        # Assume the item is in the list.
        pass


class Element(object):

    def __init__(self, value):
        self.ahead = None
        self.behind = None
        self.item = value