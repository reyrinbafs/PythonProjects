from turtle import Turtle, Screen
import pandas as pd

tt = Turtle()
scr = Screen()
img = "blank_states_img.gif"
scr.title("U.S. state Game")

scr.addshape(img)
tt.shape(img)

data = pd.read_csv("50_states.csv")

state_name = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    ans_state = scr.textinput(title=f"{len(guessed_state)}/50 State Correct", prompt="What's another state name?").title()

    if ans_state == "Exit":
        missing_state = [state for state in state_name if state not in guessed_state]
        df = pd.DataFrame(missing_state)
        df.to_csv("state_to_learn")
        break
    if ans_state in state_name:
        guessed_state.append(ans_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        cor = data[data.state == ans_state]
        t.goto(int(cor.x), int(cor.y))
        t.write(ans_state)

