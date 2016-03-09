# Algorithms and Data Structures: Recursive drawing
# 03.08.2016
# @totallygloria


import turtle

t = turtle.Turtle()
box = turtle.Screen()


def koch_standard(tortise, order, size):
    """
       Make turtle draw a Koch fractal of 'order' and 'size'.
       Leave the turtle facing the same direction.
    """

    if order == 0:          # The base case is just a straight line
        tortise.forward(size)
    else:
        koch_standard(tortise, order - 1, size / 3)   # Go 1/3 of the way
        tortise.left(60)
        koch_standard(tortise, order - 1, size / 3)
        tortise.right(120)
        koch_standard(tortise, order - 1, size / 3)
        tortise.left(60)
        koch_standard(tortise, order - 1, size / 3)
'''
t.penup()
t.goto(-200, 100)
t.pendown()
koch_standard(t, 3, 400)
'''


def koch_shapes(tortise, order, size):
    if order == 0:          # The base case is just a straight line
        tortise.forward(size)
    else:
        koch_shapes(tortise, order - 1, size / 4)   # Go 1/3 of the way
        tortise.left(70)
        koch_shapes(tortise, order - 1, size / 4)
        tortise.right(120)
        koch_shapes(tortise, order - 1, size / 4)
        tortise.left(70)
        koch_shapes(tortise, order - 1, size / 4)

'''
koch_shapes(t, 3, 1000)
'''


def koch_snowflake():

    for i in range(3):
        koch_standard(t, 3, 200)
        t.right(120)

'''
t.penup()
t.goto(-100, 100)
t.pendown()
koch_snowflake()
'''

box.exitonclick()
