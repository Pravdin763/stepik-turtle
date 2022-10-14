# Напишите программу, которая рисует изображение радуги по образцу.

# https://stepik.org/lesson/502329/step/5?unit=494030

import turtle as t

t.speed(9)

color = ["#FF0000", "#FFA600", "#FFFF00", "#62FF00", "#89F590", "#69C5FF", "#1E56FC", "#4800FF", "#CC00FF", "#FF5099"]
y = -70
count = 155
for i in range(10):
    t.penup()
    t.goto(0, y)
    t.pendown()
    t.fillcolor(color[i])
    t.begin_fill()
    t.circle(count)
    t.end_fill()
    count -= 15
    y += 15
