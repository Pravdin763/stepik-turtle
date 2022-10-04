import turtle


def hexagon(side):
    for i in range(8):
        turtle.forward(side)
        turtle.left(45)


side = int(input())
hexagon(side)