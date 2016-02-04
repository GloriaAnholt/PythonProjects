# Algorithms & Data Structures: Implementing a Stack
# 12.21.15
# @totallygloria


class Stack():
	
    def __init__(self):
        self.items = []
	
    def push(self, item):
        self.items.append(item)
        return self.items
	
    def pop(self):
        return self.items.pop()
		
    def peek(self):
        return self.items[-1]
		
    def isEmpty(self):
        return len(self.items) == 0
		
    def size(self):
        return len(self.items)


def rev_string(inputString):
	
    stack = Stack()
    new_string = str()
	
    for char in inputString:
        stack.push(char)
	
    while not stack.isEmpty():
        new_string += stack.pop()
    return new_string	


def paren_checker(string):
	
    stack = Stack()
	
    for char in string:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if not stack.isEmpty():
                stack.pop()
            else:
                return 'Unbalanced'
	
    if not stack.isEmpty():
        return 'Unbalanced'
    else:
        return 'Balanced'


def general_checker(string):
	
    stack = Stack()
    opens = '([{<'
    closes = ')]}>'
	
    for char in string:
        if char in opens:
            stack.push(char)
        elif char in closes:
            if stack.isEmpty():
                return "Stack prematurely empty. Unbalanced."
            else:
                prior = stack.pop()
                return match_checker(char,prior) #returns Balanced or Unbalanced
    if stack.isEmpty():
        return 'Balanced'
    else:
        return 'Unbalanced'


def match_checker(char,prior):	
	
    matches = [('(', ')'),('[', ']'),('{', '}'),('<', '>')]
    for opening, closing in matches:
        if char == closing and prior == opening:
            return "Balanced."
    return "Unbalanced."


def int_to_bin(value):
	
    stack = Stack()
    num = int(value)
    binary_num = ''
	
    while num > 0:
        stack.push(num % 2)
        num = num // 2
    while not stack.isEmpty():
        binary_num += str(stack.pop())
    return binary_num


if int_to_bin(233) == '11101001':
    print "233 equals", int_to_bin(233)
else:
    print "Doesn't work."

