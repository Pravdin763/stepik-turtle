# Напишите программу, которая рисует циферблат часов в соответствии с образцом.
# черепашьи часы
import turtle
turtle.shape('turtle')

turtle.pensize(3)
turtle.stamp()


c =0

for i in range(12):
  c +=360/12
  turtle.penup()
  turtle.forward(100)
  turtle.pendown()
  turtle.forward(20)
  turtle.penup()
  turtle.forward(20)
  turtle.pendown()
  turtle.stamp()
  turtle.penup()
  turtle.left(180)
  turtle.forward(140)
  turtle.setheading(c)