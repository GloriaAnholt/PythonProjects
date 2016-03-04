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
        if self.size == 0:          # if there's nothing in the list, don't do anything
            return
        elif self.size == 1:        # if there's one item, and it's the right one, delete head/tail
            if self.first.item == item:
                self.first = None
                self.last = None
        elif self.first.item == item:         # If the item is first, remove it and move head
            self.first = self.first.behind
            self.first.ahead = None
        elif self.last.item == item:        # If the item is last, remove and move tail
            self.last = self.last.ahead
            self.last.behind = None
        else:
            current = self.first
            for i in range(self.size):
                if current.item == item:
                    infront = current.ahead
                    inback = current.behind
                    infront.behind = inback
                    inback.ahead = infront
                    break
                else:
                    current = current.behind
        self.size -= 1

    def search(self, item):
        # searches for the item in the list. It needs the item and returns a boolean value.
        current = self.first
        for i in range(self.size):
            if current.item == item:
                return True
            elif current.item > item:
                break
            else:
                current = current.behind
        return False

    def is_empty(self):
        # tests to see whether the list is empty. It needs no parameters and returns a boolean value.
        if self.size == 0 or (self.first is None and self.last is None):
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
        popped = self.last
        if self.size <= 0:
            return None
        elif self.size == 1:
            self.last = None
            self.first = None
        elif self.size > 1:
            new_last = popped.ahead
            new_last.behind = None
            self.last = new_last
        self.size -= 1
        return popped.item

    def grab(self, pos):
        # removes and returns the item at position pos. It needs the position and returns the item.
        # Assume the item is in the list.
        # Special case for first item, doesn't need to loop
        # Special case for last item, calls pop method
        if pos == (self.size - 1):
            return self.pop()

        current = self.first
        if pos == 0 and self.size == 1:   # Clear the list if it's only one node long
            self.last = None
            self.first = None
        elif pos == 0 and self.size > 1:  # Move head back if list is longer than one
            new_first = current.behind
            new_first.ahead = None
            self.first = new_first
        else:                             # loop through list until at item, remove and return item
            for i in range(pos + 1):
                if i == pos and self.size > 1:
                    infront = current.ahead
                    inrear = current.behind
                    infront.behind = inrear
                    inrear.front = infront
                else:
                    current = current.behind
        self.size -= 1
        return current.item


class Node(object):

    def __init__(self, value):
        self.ahead = None
        self.behind = None
        self.item = value

    def get_next(self):
        return self.behind

