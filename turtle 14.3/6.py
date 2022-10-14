# Напишите программу, которая рисует изображение полумесяца по образцу.
# https://stepik.org/lesson/502329/step/6?unit=494030

import turtle as t

t.Screen().bgcolor('blue')

t.fillcolor("yellow")
t.pencolor("yellow")
t.begin_fill()

t.circle(90)
t.end_fill()
t.goto(25, 0)
t.fillcolor("blue")
t.pencolor("blue")
t.begin_fill()
t.circle(90)
t.end_fill()
