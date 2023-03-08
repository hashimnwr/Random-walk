from turtle import Turtle, Screen
from random import randint

screen = Screen()

off = True
screen.setup(width=500, height=500)
color = ['indigo', 'blue', 'green', 'grey', 'orange', 'red']
user_choice = screen.textinput(title="Place your contender", prompt=f"Who's gonna win? {color} : ")
y = [75, 45, 15, -15, -45, -75]
all_t = []

for i in range(6):
    new_t = Turtle(shape='turtle')
    new_t.penup()
    new_t.color(color[i])
    new_t.goto((-200, y[i]))
    all_t.append(new_t)


def move():
    return randint(0, 10)


if user_choice:
    off = False

while not off:
    for _ in all_t:
        if _.xcor() > 230:
            off = True
            winner = _.pencolor()
            if winner == user_choice:
                print(f"You win! {winner} did actually win")
            else:
                print(f"You lost! {winner} won")
        _.fd(move())


screen.exitonclick()
