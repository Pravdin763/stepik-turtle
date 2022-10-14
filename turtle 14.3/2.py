#  Напишите программу, которая рисует изображение домика по образцу.
# https://stepik.org/lesson/502329/step/2?unit=494030

import turtle as t

t.fillcolor('brown')
t.begin_fill()
t.forward(30)
t.left(135)
t.forward(120)
t.left(90)
t.forward(120)
t.left(135)
t.forward(30)
t.end_fill()

t.fillcolor('blue')
t.begin_fill()
for i in range(4):
  t.forward(110)
  t.right(90)
t.end_fill()