from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project

def gen_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_letters = [choice(letters) for _ in range(randint(8, 10))]
    pw_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    pw_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    pw_list = pw_letters + pw_numbers + pw_symbols
    shuffle(pw_list)
    password = "".join(pw_list)
    pass_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    email = email_input.get()
    pw = pass_input.get()
    new_data = {
        website: {
            "email": email,
            "password": pw,
        }
    }

    if website == '' or pw == '':
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty.")
    else:
        try:
            with open("data.json", 'r') as data_file:
                json_data = json.load(data_file)  # read data.json
        except FileNotFoundError:
            with open("data.json", 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            json_data.update(new_data)  # update new_data ---> data.json
            with open("data.json", 'w') as data_file:
                json.dump(json_data, data_file, indent=4)  # write json data --> data.json
        finally:
            website_input.delete(0, END)
            pass_input.delete(0, END)

# ---------------------------- Search Password ------------------------------- #

def search():
    website = website_input.get()
    try:
        with open("data.json", 'r') as data_file:
            json_data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in json_data:
            email = json_data[website]["email"]
            password = json_data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email : {email}\n Password : {password}")
        else:
            messagebox.showinfo(title="No Match Found", message="No details for website exists.")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=img)
canvas.grid(column=0, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "example@gmail.com")

pass_input = Entry(width=21)
pass_input.grid(column=1, row=3)

btn_gen_pass = Button(text="Generate Password", command=gen_pw)
btn_gen_pass.grid(column=2, row=3)

btn_add = Button(text="Add", command=save, width=36)
btn_add.grid(column=1, row=4, columnspan=2)

search_btn = Button(text="Search", command=search, width=15)
search_btn.grid(column=2, row=1)

window.mainloop()
