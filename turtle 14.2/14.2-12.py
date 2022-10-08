# Напишите программу, которая рисует изображение в соответствии с образцом (ёлочку)

import turtle as t
t.speed(7)

t.penup()
t.goto(0, 100)
t.pendown()
t.dot()
for i in range(-120, 120, 20):
  t.pencolor("DeepSkyBlue")
  t.goto(i, -70)
  t.pencolor("blue")
  t.pensize(3)
  t.dot()
  t.pensize(1)
  t.pencolor("DeepSkyBlue")
  t.goto(0, 100)
