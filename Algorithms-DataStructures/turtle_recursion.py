# Algorithms and Data Structures: Recursive drawing
# 03.08.2016
# @totallygloria


import turtle
import random


t = turtle.Turtle()
box = turtle.Screen()


def draw_sprial(tortise, linelength):
    if linelength > 0:
        tortise.forward(linelength)
        tortise.right(25)
        draw_sprial(tortise, int(linelength * .95))

'''
t.penup()
t.goto(-100, 150)
t.pendown()
draw_sprial(t, 100)
box.exitonclick()
'''


def draw_fractal_tree(tortise, branchlength):
    if branchlength > 5:
        tortise.forward(branchlength)
        tortise.right(20)
        draw_fractal_tree(tortise, branchlength - 5)
        tortise.left(40)
        draw_fractal_tree(tortise, branchlength - 5)
        tortise.right(20)
        tortise.backward(branchlength)

'''
draw_fractal_tree(t, 100)
box.exitonclick()
'''


def draw_complex_tree(tortise, branchlength):
    if branchlength > 5:
        tortise.forward(branchlength)
        amt = random.randrange(15, 30)
        tortise.right(amt)
        draw_fractal_tree(tortise, branchlength - (random.randrange(5, 10)))
        tortise.left(amt * 2)
        draw_fractal_tree(tortise, branchlength - (random.randrange(5, 10)))
        tortise.right(amt)
        tortise.backward(branchlength)

'''
t.left(90)
t.up()
t.backward(120)
t.down()
t.pensize(width=1)
t.color("green")
draw_complex_tree(t, 50)
box.exitonclick()
'''