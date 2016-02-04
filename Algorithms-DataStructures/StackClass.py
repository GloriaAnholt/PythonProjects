# Algorithms & Data Structures: Implementing a Stack
# 12.21.15
# @totallygloria


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        return self.items

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def contains_items(self):
        return len(self.items) > 0

    def size(self):
        return len(self.items)


def rev_string(input_string):
    stack = Stack()
    new_string = str()

    for char in input_string:
        stack.push(char)

    while stack.contains_items():
        new_string += stack.pop()
    return new_string
