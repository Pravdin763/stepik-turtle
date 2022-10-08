# Напишите программу, которая рисует изображение мишки в соответствии с образцом.
# https://stepik.org/lesson/330014/step/14?unit=313365

import turtle as t

t.speed(10)


t.goto(0, -50)
t.penup()
t.goto(0, -70)
t.pendown()
t.circle(100)
t.circle(50)



t.penup()
t.goto(0, -2)
t.pendown()
t.circle(10)

t.penup()
t.goto(45, 33)
t.pensize(12)
t.dot()

t.penup()
t.goto(-45, 33)
t.dot()
t.pensize(1)

t.penup()
t.goto(85, 100)
t.pendown()
t.circle(35)

t.penup()
t.goto(-85, 100)
t.pendown()
t.circle(35)