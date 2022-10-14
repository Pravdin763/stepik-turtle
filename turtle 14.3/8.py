# Напишите программу, которая рисует изображение по образцу. Звезды должны быть рассыпаны случайно, иметь разный размер и цвет.
# https://stepik.org/lesson/502329/step/8?unit=494030

import turtle as t
import random as r

t.Screen().bgcolor('black')
t.hideturtle()
t.speed(10)

color = ["#FF0000", "#FFA600", "#FFFF00", "#62FF00", "#89F590", "#69C5FF", "#1E56FC", "#4800FF", "#CC00FF", "#FF5099"]

for i in range(1, 50):
    t.setheading(r.randrange(0, 360, 2))
    t.penup()
    t.goto(r.randrange(-180, 180, 2), r.randrange(-180, 180, 2))
    t.pendown()
    coo = r.choice(color)
    t.fillcolor(coo)
    t.pencolor(coo)
    t.begin_fill()
    size = r.randrange(5, 25, 2)
    for i in range(5):
        t.rt(144)
        t.fd(size)
    t.end_fill()
