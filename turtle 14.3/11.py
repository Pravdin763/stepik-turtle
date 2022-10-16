# Компас
# https://stepik.org/lesson/502329/step/11?unit=494030


import turtle as t

t.hideturtle()

t.circle(30)
t.goto(0, 130)
t.write("Север", align='center', font=('Arial', 15, 'normal'))
t.goto(0, -70)
t.write("Юг", align='center', font=('Arial', 15, 'normal'))
t.goto(0, 30)
t.goto(100, 30)
t.write("Восток", align='left', font=('Arial', 15, 'normal'))
t.goto(-100, 30)
t.write("Запад", align='right', font=('Arial', 15, 'normal'))
t.setheading(-90)
t.circle(100)
