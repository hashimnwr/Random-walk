from turtle import Turtle, Screen, colormode
from random import choice, randint

brush = Turtle()
screen = Screen()

brush.hideturtle()

i = 0

colormode(255)


def change_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb = (r, g, b)
    return rgb


brush.width(7)

angle = [0, 90, 180, 270]
brush.speed('fastest')

while i < 300:
    brush.color(change_color())
    brush.forward(20)
    brush.setheading(choice(angle))
    i += 1

screen.exitonclick()
