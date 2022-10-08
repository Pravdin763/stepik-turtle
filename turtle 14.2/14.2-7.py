import turtle as t

t.shape('turtle')

n = 10
for i in range(20):
  n -=10
  t.stamp()
  t.penup()
  t.forward(n)
  t.right(90)
  t.pendown()
  t.stamp()
  t.penup()
  t.right(90)
  t.forward(n)
  t.setheading(n*3)
