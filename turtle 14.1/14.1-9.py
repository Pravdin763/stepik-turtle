# Напишите программу, которая рисует снежинку из 1010 ромбов.

import turtle

gradus =0

for j in range(9):
  turtle.setheading(gradus)
  for i in range(2):
    turtle.right(30)
    turtle.forward(80)
    turtle.left(60)
    turtle.forward(80)
    turtle.setheading(180+ gradus)
  gradus +=40

