# Напишите программу, которая рисует черепашек в соответствии с образцом по кругу


import turtle
turtle.shape('turtle')

turtle.pensize(7)
turtle.stamp()


n = int(input())
c =0

for i in range(n):
  c +=360/n
  turtle.penup()
  turtle.forward(70)
  turtle.pendown()
  turtle.stamp()
  turtle.penup()
  turtle.left(180)
  turtle.forward(70)
  turtle.setheading(c)