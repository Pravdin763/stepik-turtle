# Напишите программу для рисования паутины в соответствии с примером. Программа должна считывать количество лучей
# паутины, число nn.
#
# Примечание. Угол заданный каждой парой лучей составляет 360/n   градусов.

import turtle

turtle.pensize(7)
turtle.dot()
turtle.pensize(2)

n = int(input())
c =0

for i in range(n):
  c +=360/n
  turtle.forward(100)
  turtle.pensize(10)
  turtle.stamp()
  turtle.pensize(2)
  turtle.left(180)
  turtle.forward(100)
  turtle.setheading(c)
