from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_entry.delete(0, END)
    password_list1 = [choice(LETTERS) for _ in range(randint(8, 10))]
    password_list2 = [choice(SYMBOLS) for _ in range(randint(2, 4))]
    password_list3 = [choice(NUMBERS) for _ in range(randint(2, 4))]
    password_list = password_list1 + password_list2 + password_list3

    shuffle(password_list)

    generated_password = "".join(password_list)

    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) > 0 and len(email) > 0 and len(password) > 0:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            file = open("data.txt", "a")
            file.write(f"\n{website} | {email} | {password}")
            file.close()
            website_entry.delete(0, END), email_entry.delete(0, END), password_entry.delete(0, END)
    else:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3, ipadx=0)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, columnspan=1)

window.mainloop()
