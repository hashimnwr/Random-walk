import colorgram
from turtle import Turtle, Screen, colormode
from random import choice

brush = Turtle()
screen = Screen()

brush.hideturtle()
brush.speed('fast')
colormode(255)

rgb_colors = []
colors = colorgram.extract('img.jpg', 10)

for each in colors:
    r = each.rgb.r
    g = each.rgb.g
    b = each.rgb.b
    rgb = (r, g, b)
    rgb_colors.append(rgb)

print(rgb_colors)

brush.penup()
brush.setheading(225)
brush.fd(300)
brush.pendown()
brush.setheading(0)


for line in range(10):
    for _ in range(10):
        brush.dot(20, choice(rgb_colors))
        brush.penup()
        brush.fd(50)
        brush.pendown()

    brush.setheading(90)
    brush.pu()
    brush.fd(50)
    brush.setheading(180)
    brush.fd(500)
    brush.setheading(0)
    brush.pd()

screen.exitonclick()
