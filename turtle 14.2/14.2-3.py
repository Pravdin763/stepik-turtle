# Напишите программу, которая рисует прямоугольник с точкой в каждом углу

import turtle

for i in range(2):
  turtle.forward(100)
  turtle.pensize(5)
  turtle.dot()
  turtle.pensize(1)
  turtle.left(90)
  turtle.forward(50)
  turtle.pensize(5)
  turtle.dot()
  turtle.pensize(1)
  turtle.left(90)