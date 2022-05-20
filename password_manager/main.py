from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

WHITE = "white"
BLACK = "black"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(
            title="Oops", message="Don't leave any field empty!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Details entered: \nEmail: {email}"
                                    f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


# Window configuration
window = Tk()
window.title("Password Generator 🔐")
window.config(padx=50, pady=50, bg=WHITE)


# Canvas configuration
canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", bg=WHITE, fg=BLACK)
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", bg=WHITE, fg=BLACK)
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg=WHITE, fg=BLACK)
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=40, bg=WHITE, fg=BLACK,
                    highlightthickness=0, insertbackground=BLACK)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=40, bg=WHITE, fg=BLACK,
                    highlightthickness=0, insertbackground=BLACK)
email_entry.insert(0, "alphageekdom@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=22, bg=WHITE, fg=BLACK,
                    highlightthickness=0, insertbackground=BLACK)
password_entry.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password",
                        highlightbackground=WHITE, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36,
                    highlightbackground=WHITE, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
