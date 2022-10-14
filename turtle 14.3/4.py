# Напишите программу, которая рисует оптическую иллюзию по образцу.
# https://stepik.org/lesson/502329/step/4?unit=494030

import turtle as t

t.speed(8)


def triangle1():
    for i in range(3):  # Равнобедренный треугольник 1
        t.fd(60)
        t.lt(120)
        t.fd(120)


def three_circles():
    x = 60
    y = [70, -70, 70]  # координаты y кругов
    for i in range(3):  # 3 круга оголо треугольника
        t.fillcolor("black")
        t.penup()
        t.goto(x, y[i])
        t.pendown()
        t.begin_fill()
        t.circle(25)
        t.end_fill()
        x -= 90


def triangle2():
    t.penup()  # Закрашенный перевернутый равнобедренный треугольник 2
    t.goto(60, 95)
    t.pendown()
    t.fillcolor("white")
    t.pencolor("white")
    t.begin_fill()
    t.goto(-30, -55)
    t.goto(-120, 95)
    t.end_fill()


triangle1()
three_circles()
triangle2()
