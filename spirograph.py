import turtle
from turtle import Turtle, Screen
from random import choice, randint

brush = Turtle()
screen = Screen()

brush.hideturtle()

i = 0

turtle.colormode(255)
brush.speed('fastest')


def change_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb = (r, g, b)
    return rgb


for angle in range(181):
    brush.color(change_color())
    brush.circle(100)
    brush.right(2)
screen.exitonclick()
