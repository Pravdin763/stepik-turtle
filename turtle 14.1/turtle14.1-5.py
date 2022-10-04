import turtle

gradus = -45
for k in range(2):
    gradus += 45
    turtle.setheading(gradus)
    for j in range(4):
        gradus += 90
        turtle.setheading(gradus)
        for i in range(4):
            turtle.forward(100)
            turtle.left(90)
