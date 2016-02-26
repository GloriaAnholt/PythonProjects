# Data Structures and Algorithms: List Class
# 02.24.16
# @totallygloria


class OrderedList(object):

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def add(self, value):
        # adds a new item to the list making sure that the order is preserved. It needs the item
        # and returns nothing. Assume the item is not already in the list.
        new_node = Node(value)
        # If the list is empty, both head and tail are the new node
        if self.size == 0:
            self.first = new_node
            self.last = new_node
        # If the new node is the smallest, put it at the head. If the list is one long, also move the tail
        elif new_node.item <= self.first.item:
            old_first = self.first
            new_node.behind = self.first
            self.first.ahead = new_node
            self.first = new_node
            if self.size == 1:
                self.last = old_first
        # If the new node is the largest, put it at the tail
        elif new_node.item >= self.last.item:
            new_node.ahead = self.last
            self.last.behind = new_node
            self.last = new_node
        # If you get here, the node goes in the middle of the list
        else:
            current = self.first
            for i in range(self.size):
                if new_node.item > current.item:
                    current = current.behind
                elif new_node.item <= current.item:
                    infront = current.ahead
                    infront.behind = new_node
                    new_node.ahead = infront
                    new_node.behind = current
                    current.ahead = new_node
                    break
        self.size += 1

    def remove(self, item):
        # removes the item from the list. It needs the item and modifies the list.
        # Assume the item is present in the list.
        if self.first.item == item:         # If the item is first, remove it and move head
            current = self.first
            current.ahead = None
            self.first = current.behind
            self.size -= 1
        elif self.last.item == item:        # If the item is last, remove and move tail
            current = self.last
            current.behind = None
            self.last = current.ahead
            self.size -= 1
        else:
            current = self.first
            for i in range(self.size):
                if current.item == item:
                    infront = current.ahead
                    inback = current.behind
                    infront.behind = inback
                    inback.ahead = infront
                    self.size -= 1
                    break
                else:
                    current = current.behind
'''
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
'''


class Node(object):

    def __init__(self, value):
        self.ahead = None
        self.behind = None
        self.item = value

    def get_next(self):
        return self.behind