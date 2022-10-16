# Напишите программу, которая рисует изображение правильных многоугольников по образцу. Многоугольники должны иметь разный цвет.
#
# Примечание 1. Доработайте программу, чтобы площадь всех многоугольников была одинаковой.
# Площадь правильного многоугольника вычисляется по формуле
# https://stepik.org/lesson/502329/step/9?unit=494030
# НЕ МОЙ КОД!!!
from turtle import *
from random import randint
from math import tan, sqrt, radians

square = 4000

def draw_figure(n):
    size = sqrt(4 * square * tan(radians(180 / n)) / n)
    fillcolor(tuple((randint(0, 255) for _ in range(3))))
    begin_fill()
    forward(size / 2)
    right(360 / n)
    for i in range(n - 1):
        forward(size)
        right(360 / n)
    forward(size / 2)
    end_fill()

Screen().setup(800, 800)
speed(0)
for x in range(5):
    for y in range(5):
        penup()
        goto(x * 100 - 300, y * 100 - 50)
        pendown()
        draw_figure(randint(3, 8))