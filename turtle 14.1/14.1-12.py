# Напишите программу, которая рисует квадраты, чтобы создать узор, показанный на рисунке.

import turtle as t

count =50
for i in range(10):
  for i in range(4):
    t.left(90)
    t.forward(count)
  count +=10