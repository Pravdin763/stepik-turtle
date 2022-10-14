# Напишите программу, которая рисует изображение светофора по образцу.
# https://stepik.org/lesson/502329/step/3?unit=494030

import turtle as t

t.fillcolor("black")
t.begin_fill()
for i in range(2):
    t.fd(70)
    t.rt(90)
    t.fd(200)
    t.rt(90)
t.end_fill()

color = ["red", "yellow", "Green"]

y = -60
for i in range(3):
    t.fillcolor(color[i])
    t.begin_fill()
    t.penup()
    t.goto(35, y)
    t.circle(23)
    t.pendown()
    t.end_fill()
    y -= 60
