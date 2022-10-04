#https://stepik.org/lesson/330013/step/8?unit=313364

import turtle

g = 0
for j in range(2):
  turtle.setheading(g)
  g +=180
  for i in range(2):
    turtle.forward(50)
    turtle.left(120)