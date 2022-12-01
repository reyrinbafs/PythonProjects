from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# ---------------- FETCH WORD

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    org_data = pd.read_csv("data/french_words.csv")
    to_learn = org_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_time
    window.after_cancel(flip_time)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(front_img, image=f_img)
    flip_time = window.after(3000, func=flip_card)


def correct():
    to_learn.remove(current_card)
    df = pd.DataFrame(to_learn)
    df.to_csv("words_to_learn.csv", index=False)
    next_card()


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(front_img, image=b_img)


# ---------------- UI

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_time = window.after(3000, func=flip_card)
# window.after_cancel()


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
f_img = PhotoImage(file="images/card_front.png")
front_img = canvas.create_image(400, 263, image=f_img)
b_img = PhotoImage(file="images/card_back.png")
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 256, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=1, column=1, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
w_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
w_button.grid(row=2, column=1)

right_img = PhotoImage(file="images/right.png")
r_button = Button(image=right_img, highlightthickness=0, command=next_card)
r_button.grid(row=2, column=2)

next_card()

window.mainloop()
