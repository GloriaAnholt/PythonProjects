# Algorithms and Data Structures: Recursive drawing
# 03.08.2016
# @totallygloria


import turtle
import math



box = turtle.Screen()
#t.penup()
#t.goto(-200, 200)
#t.pendown()


def mid_point(p1,p2):

    mid = [((p1[0] + p2[0]) / 2), ((p1[1] + p2[1]) / 2)]
    return mid


def draw_triangle(depth,p1,p2,p3):

    colormap = ['violet', 'blue', 'green', 'yellow', 'orange', 'red']
    t = turtle.Turtle()
    t.penup()
    t.goto(p1)
    t.pendown()
    t.fillcolor(colormap[depth])
    t.begin_fill()
    t.goto(p2)
    t.goto(p3)
    t.goto(p1)
    t.end_fill()


    if depth > 1:
        q1 = mid_point(p1,p2)
        q2 = mid_point(p1,p3)
        q3 = mid_point(p2,p3)
        draw_triangle(depth-1, q1, p2, q3)
        draw_triangle(depth-1, q2, p1, q1)
        draw_triangle(depth-1, q3, p3, q2)




draw_triangle(5,[-200,-100],[200,-100],[0,250])

box.exitonclick()

