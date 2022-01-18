import tkinter
from tkinter import messagebox
import random
import pyperclip

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
# Pallet taken from https://colorhunt.co/
FONT_NAME = "Times New Roman"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
               'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters

    random.shuffle(password_list)
    password = ''.join(password_list)
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    site = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # data validation
    if validate(site, email, password):
        # confirmation dialog:
        confirm = messagebox.askokcancel(title=website_entry,
                                         message=f"Your details: \n Email: {email} \n Password: {password}"
                                                 f" \n Do you want to save?")
        # save data to a file
        if confirm:
            with open('data.txt', 'a') as file:
                file.write(f"{site} | {email} | {password}\n")

            clear_entries()


# validate data, return True if all OK
def validate(site, email, password):
    # check if empty
    if len(site) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='Error', message='Empty fields found.')
    else:
        return True


def clear_entries():
    website_entry.delete(0, tkinter.END)
    email_entry.delete(0, tkinter.END)
    password_entry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #

# set up canvas
window = tkinter.Tk()
window.title('Password Manager')
window.config(padx=60, pady=40)

canvas = tkinter.Canvas(height=200, width=200)
logo_img = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# labels
website_label = tkinter.Label(text='Website:', font=(FONT_NAME, 12), )
website_label.grid(column=0, row=1)

email_label = tkinter.Label(text='Email/Username:', font=(FONT_NAME, 12))
email_label.grid(column=0, row=2)

password_label = tkinter.Label(text='Password:', font=(FONT_NAME, 12))
password_label.grid(column=0, row=3)

# entries
website_entry = tkinter.Entry(width=52, justify='left')
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_entry = tkinter.Entry(width=52, justify='left')
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = tkinter.Entry(width=33, justify='left')
password_entry.grid(column=1, row=3)

# buttons
generate_password_button = tkinter.Button(text='Generate Password', justify='center', command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = tkinter.Button(text='Add', width=44, justify='center', command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

# while True
window.mainloop()
