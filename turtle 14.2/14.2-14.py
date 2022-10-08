# Напишите программу, которая рисует изображение мишки в соответствии с образцом.
# https://stepik.org/lesson/330014/step/14?unit=313365

import turtle as t

t.speed(10)


def head():
    t.goto(0, -50)
    t.penup()
    t.goto(0, -70)
    t.pendown()
    t.circle(100)
    t.circle(50)


def moska():
    t.penup()
    t.goto(0, -2)
    t.pendown()
    t.circle(10)


def eyes():
    t.pensize(12)
    for i in range(-45, 46, 90):
        t.penup()
        t.goto(i, 33)
        t.dot()
    t.pensize(1)


def ears():
    for i in range(-85, 86, 170):
        t.penup()
        t.goto(i, 100)
        t.pendown()
        t.circle(35)


head()
moska()
eyes()
ears()
