# Напишите программу, которая рисует узор, показанный на рисунке.

import turtle as t

count =30
for i in range(30):
  t.left(90)
  t.forward(count)
  count +=10
