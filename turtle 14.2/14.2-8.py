import turtle as t
import random

color = ['red', 'blue', 'gold', 'green', 'LightSeaGreen']

x = 5
size = 1

for i in range(50):
    t.pencolor(random.choice(color))
    t.pensize(size)
    t.forward(x)
    t.left(45)
    x += 3
    size += 0.5


print("тестим гит без терминала")