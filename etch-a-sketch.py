from turtle import Turtle, Screen

brush = Turtle()
screen = Screen()


def move_forward():
    brush.forward(10)


def move_backward():
    brush.backward(10)


def turn_right():
    brush.right(5)


def turn_left():
    brush.left(5)


def clear_screen():
    # brush.clear()
    # brush.penup()
    # brush.home()
    # brush.penup()
    screen.reset()


screen.listen()
screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=move_backward, key='s')
screen.onkey(fun=turn_left, key='a')
screen.onkey(fun=turn_right, key='d')
screen.onkey(fun=clear_screen, key='c')
screen.exitonclick()
