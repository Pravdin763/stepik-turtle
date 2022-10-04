#  https://stepik.org/lesson/330013/step/7?unit=313364

import turtle

def hexagon(side):
    for i in range(6):
        turtle.forward(side)
        turtle.left(60)

def huexgon(side):
    for i in range(5):
        turtle.forward(side)
        turtle.left(60)

side = int(input())

hexagon(side)
gradus = 240
for i in range(6):
    turtle.setheading(gradus)
    huexgon(side)
    gradus += 60
