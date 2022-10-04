import turtle


def square(side):
    gradus = 15
    for j in range(3):
        gradus += 15
        turtle.setheading(gradus)
        for i in range(4):
            turtle.forward(side)
            turtle.left(90)


side = int(input())
square(side)