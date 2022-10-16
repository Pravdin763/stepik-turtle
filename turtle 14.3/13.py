import turtle as t

size = 36
pen = [4, 1]
for j in range(2):
    for i in range(8):
        t.pensize(pen[j])
        t.fd(size)
        t.rt(360 / 8)
        t.fd(size)
    size -= 3
    t.penup()
    t.rt(90)
    t.fd(7)
    t.lt(90)
    t.pendown()
    t.pencolor("red")
    t.begin_fill()
    t.fillcolor("red")
t.end_fill()

t.penup()
t.goto(0, -105)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.pencolor("white")
t.write("STOP", align='center', font=('Arial', 35, 'bold'))
t.end_fill()
t.hideturtle()


