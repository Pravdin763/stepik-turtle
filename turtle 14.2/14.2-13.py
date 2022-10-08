# Напишите программу, которая рисует изображение символа олимпиады в соответствии с образцом.
# https://stepik.org/lesson/330014/step/13?unit=313365

import turtle as t
import random as r
t.speed(8)

t.pensize(6)
color = ['black', 'Blue', 'Red', 'Yellow', 'Green']
c = 1

t.pencolor(color[0])
t.circle(60)

for i in range(-120, 121, 240):
  t.pencolor(color[c])
  t.penup()
  t.goto(i,0)
  t.pendown()
  t.circle(60)
  c+=1

for i in range(-60, 61, 120):
  t.pencolor(color[c])
  t.penup()
  t.goto(i,-80)
  t.pendown()
  t.circle(60)
  c+=1
