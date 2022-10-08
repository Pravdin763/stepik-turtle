# Напишите программу, которая рисует звезду, показанную на рисунке. Такую звезду можно создать из двух треугольников.
# Однако их невозможно нарисовать непрерывной линией, поэтому перо нужно будет поднять для перехода ко второму треугольнику.

# https://stepik.org/lesson/330014/step/9?unit=313365

import turtle as t

t.goto(50, 0)
t.goto(0, 100)
t.goto(-50, 0)
t.goto(0, 0)
t.penup()

t.goto(0, 65)
t.pendown()
t.goto(-50, 65)
t.goto(0, -35)
t.goto(50, 65)
t.goto(0, 65)

## устанавливает скорость анимации 11 (самую медленную), затем 22, затем 33 и т.д и рисует круги.

for i in range(1, 11):
    t.speed(i)
    t.circle(100 - 10*i)