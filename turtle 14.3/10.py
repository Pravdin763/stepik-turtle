# Шахматная доска
# 10


import turtle as t


x, y = -100, 100
for j in range(5):
  for i in range(5):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    if (i%2==0 and j%2==0) or (i%2!=0 and j%2!=0):
      t.fillcolor("Black")
    else:
      t.fillcolor("white")
    for i in range(4):
      t.rt(90)
      t.fd(50)
      x+=12.5
    t.end_fill()
  y-=50
  x=-100