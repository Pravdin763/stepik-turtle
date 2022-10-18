# Напишите программу, которая по нажатию на левую кнопку мыши рисует звезду в месте клика.
# Фон изображения должен быть черным, при этом звезды могут иметь разные размеры,
# цвета и иметь разное количество сторон.

# https://stepik.org/lesson/502329/step/16?unit=494030

import turtle as t
import random as r

t.Screen().setup(500, 500)
t.Screen().bgcolor('black')
t.speed(0)

size = r.randint(5, 20)
facet = r.randint(4, 12)
color = (r.randrange(256), r.randrange(256), r.randrange(256))


def mouse(x, y):
    star(x, y)


def star(x, y):
    t.setheading(r.randrange(361))
    size = r.randint(5, 20)
    facet = r.randint(4, 12)
    color = (r.randrange(256), r.randrange(256), r.randrange(256))
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(facet):
        t.fd(size)
        t.right(180 - 360 / 2 / facet)
        t.fd(size)
        t.left(180 - 360 / facet * 1.5)
    t.end_fill()


t.Screen().onclick(mouse)
t.Screen().listen()
t.hideturtle()
