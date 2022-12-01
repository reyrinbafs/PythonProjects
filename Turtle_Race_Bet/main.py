from turtle import Turtle, Screen
import random

is_race_on = False
scr = Screen()
color = ['red', 'blue', 'purple', 'yellow', 'green']
user_bet = scr.textinput(title='Make your bet', prompt="which turtle will win the race? color: ")
y_ax = [100, 70, 20, -10, -40]
racer = []

for i in range(0, 4):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_ax[i])
    racer.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in racer:
        turtle.fd(random.randint(0, 5))
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"you've Won! the winner {winning_color}")
            else:
                print(f"you lost. the winner {winning_color}")

scr.setup(width=500, height=400)
scr.exitonclick()
