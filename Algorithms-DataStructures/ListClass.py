# Data Structures and Algorithms: List Class
# 02.17.16
# @totallygloria


class List(object):

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def add(self, item):
        # adds a new item to the FRONT of the list. It needs the item and returns nothing.
        # Assume the item is not already in the list.
        new_item = Node(item)
        if self.size == 0:
            self.first = new_item
            self.last = new_item
        else:
            new_item.behind = self.first
            self.first.ahead = new_item
            self.first = new_item
        self.size += 1

    def append(self, item):
        # adds a new item to the end of the list making it the last item in the collection.
        # It needs the item and returns nothing. Assume the item is not already in the list.
        new_item = Node(item)
        if self.size == 0:
            self.first = new_item
            self.last = new_item
        else:
            new_item.ahead = self.last
            self.last.behind = new_item
            self.last = new_item
        self.size += 1

    def pop(self):
        # removes and returns the last item in the list. It needs nothing and returns an item.
        # Assume the list has at least one item.
        if self.size > 1:
            popped = self.last
            new_last = popped.ahead
            new_last.behind = None
            self.last = new_last
            self.size -= 1
            return popped.item
        elif self.size == 1:
            popped = self.last
            self.last = None
            self.first = None
            self.size -= 1
            return popped.item
        return None

    def remove(self, item):
        # removes the item from the list. It needs the item and modifies the list.
        # Assume the item is present in the list.
        current = self.first
        for i in range(self.size):
            if current.item == item and i == 0:
                inback = current.behind
                inback.ahead = None
                self.first = inback
                self.size -= 1
                break
            elif current.item == item and i == (self.size - 1):
                infront = current.ahead
                infront.behind = None
                self.last = infront
                self.size -= 1
                break
            elif current.item == item:
                infront = current.ahead
                inback = current.behind
                infront.behind = inback
                inback.ahead = infront
                self.size -= 1
                break
            else:
                current = current.behind

    def search(self, item):
        # searches for the item in the list. It needs the item and returns a boolean value.
        current = self.first
        for i in range(self.size):
            if current.item == item:
                return True
            else:
                current = current.behind
        return False

    def is_empty(self):
        # tests to see whether the list is empty. It needs no parameters and returns a boolean value.
        if self.size == 0 or (self.first == None and self.last == None):
            return True
        return False

    def size(self):
        # returns the number of items in the list. It needs no parameters and returns an integer.
        return self.size

    def index(self, item):
        # returns the position of item in the list. It needs the item and returns the index.
        # Assume the item is in the list.
        current = self.first
        for i in range(self.size):
            if current.item == item:
                return i
            else:
                current = current.behind
        return None

    def insert(self, pos, item):
        # adds a new item to the list at position pos. It needs the item and returns nothing.
        # Assume the item is not already in the list and there are enough existing items
        # to have position pos.
        if pos == 0 or self.size == 0:  # Case for front / empty list, adds
            self.add(item)
        elif pos >= self.size:   # Case for position longer than the list, appends
            self.append(item)
        else:
            new_item = Node(item)
            current = self.first
            for i in range(pos + 1):
                if i == pos:
                    infront = current.ahead
                    new_item.behind = current
                    new_item.ahead = infront
                    infront.behind = new_item
                    current.ahead = new_item
                    self.size += 1
                else:
                    current = current.behind

    def grab(self, pos):
        # removes and returns the item at position pos. It needs the position and returns the item.
        # Assume the item is in the list.
        # Special case for first item, doesn't need to loop
        if pos == 0 and self.size == 1:   # Clear the list if only one node long
            current = self.first
            self.last = None
            self.first = None
            self.size -= 1
            return current.item
        elif pos == 0 and self.size > 1:    # Reset front if longer than one
            current = self.first
            new_first = current.behind
            new_first.ahead = None
            self.first = new_first
            self.size -= 1
            return current.item
        # Special case for last item, calls pop method
        elif pos == (self.size - 1):
            return self.pop()
        # Otherwise, loop through list until at item, then remove and return item
        current = self.first
        for i in range(pos + 1):
            if i == pos:
                infront = current.ahead
                inrear = current.behind
                infront.behind = inrear
                inrear.front = infront
                self.size -= 1
                return current.item
            else:
                current = current.behind


class Node(object):

    def __init__(self, value):
        self.ahead = None
        self.behind = None
        self.item = value

    def get_next(self):
        return self.behind