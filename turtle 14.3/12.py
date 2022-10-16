# Планеты
# https://stepik.org/lesson/502329/step/12?unit=494030

import turtle as t


t.speed(9)

t.hideturtle()

size = [50, 20, 30, 25, 17, 40, 40, 35, 34, 10]

title = ["Солные", "Меркурий", "Венера", "Земля", "Марс", "Юпитер", "Сатурн", "Уран", "Нептун", "Плутон"]

color = ["yellow", "yellow3", "yellow3", "Green", 'red', "yellow3", "yellow3", "cyan", "navy", "yellow3"]

x = -200
for i in range(10):
    t.penup()
    t.goto(x, 0)
    t.pendown()
    t.begin_fill()
    t.fillcolor(color[i])
    t.circle(size[i])
    t.end_fill()
    t.penup()
    t.goto(x, -20)
    t.pendown()
    t.write(title[i], align='center')
    x += size[i] + 50

