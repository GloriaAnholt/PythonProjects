# Algorithms & Data Structures: Implementing a Stack
# 12.21.15
# @totallygloria

from StackClass import Stack

def int_to_bin(value):
    stack = Stack()
    num = int(value)
    binary_num = ''

    while num > 0:
        stack.push(num % 2)
        num //= 2
    while stack.contains_items():
        binary_num += str(stack.pop())
    return binary_num


if int_to_bin(233) == '11101001':
    print "233 equals", int_to_bin(233)
else:
    print "Doesn't work."


def base_converter():
    stack = Stack()
    digits = '0123456789ABCDEF'
    num = int(raw_input('Enter a number to convert: '))
    base = int(raw_input('Enter a base to convert to: '))
    new_num = ''

    while num > 0:
        stack.push(num % base)
        num //= base

    while stack.contains_items():
        new_num += str(digits[stack.pop()])
    return new_num

base_converter()