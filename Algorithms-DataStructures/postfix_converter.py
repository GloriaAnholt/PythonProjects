# Algorithms & Data Structures: Implementing a Stack
# 12.28.15
# @totallygloria

from StackClass import Stack
import operator


def postfix_converter(infixstring):
    op_stack = Stack()
    output_list = []
    infix_list = infixstring.split(' ')
    operators = '*/+-'

    for char in infix_list:
        if char == '(':
            op_stack.push(char)
        elif char == ')':
            prior_op = op_stack.pop()
            while prior_op != '(':
                output_list.append(prior_op)
                prior_op = op_stack.pop()
        elif char in operators:
            if op_stack.contains_items() and op_stack.peek() in '*/':
                output_list.append(op_stack.pop())
                op_stack.push(char)
            else:
                op_stack.push(char)
        else:
            output_list.append(char)

    while op_stack.contains_items():
        output_list.append(op_stack.pop())

    return " ".join(output_list)


def test_cases():

    if postfix_converter('A * B + C * D') == 'A B * C D * +':
        print "Check one pass"
    if postfix_converter('( A + B ) * C - ( D - E ) * ( F + G )') == 'A B + C * D E - F G + * -':
        print "Check two pass"
    if postfix_converter('( A + B ) * ( C + D )') == 'A B + C D + *':
        print "Check three pass"
    if postfix_converter('A * B + C * D') == 'A B * C D * +':
        print "Check four pass"


def postfix_evaluator(statement):
    operands_stack = Stack()
    statement_list = statement.split(' ')
    operators_dict = {'*': operator.mul, '/': operator.div,
                      '+': operator.add, '-': operator.sub}

    for char in statement_list:
        if char in operators_dict and operands_stack.size() >= 2:
            b = operands_stack.pop()
            a = operands_stack.pop()
            operands_stack.push(operators_dict[char](a,b))
        else:
            operands_stack.push(float(char))

    return operands_stack.pop()


def postfix_tests():

    print postfix_evaluator('17 10 + 3 * 9 /')
    print postfix_evaluator('7 8 + 3 2 + /')


postfix_tests()
test_cases()
