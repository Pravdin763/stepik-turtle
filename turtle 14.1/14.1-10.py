# Напишите программу, которая рисует лучи звезды, показанной на рисунке.

import turtle

grad = 0
for i in range(12):
    turtle.forward(100)
    turtle.left(180)
    turtle.forward(100)
    grad += 30
    turtle.setheading(grad)

