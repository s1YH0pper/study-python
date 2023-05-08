import turtle

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtle.bgcolor('black')
turtle.speed(0)

for i in range(360):
    turtle.pencolor(colors[i % len(colors)])
    turtle.width(i / 100 + 1)
    turtle.forward(i)
    turtle.left(59)
