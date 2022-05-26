from random import choice, randint, shuffle
from tkinter import messagebox
from tkinter import *
import pyperclip
import json

WHITE = "white"
BLACK = "black"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    """Generates a random password"""
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
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
    """Saves all the information that is submitted"""
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(
            title="Oops", message="Don't leave any field empty!")

    else:
        try:
            with open("data.json", "r") as data_file:
                # Read old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    """Locates and presents the information that user is looking for"""
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR", message="No Data File Found.")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(
                title="ERROR", message=f"No details for the {website} exists.")


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
website_entry = Entry(
    width=24,
    bg=WHITE,
    fg=BLACK,
    highlightthickness=0,
    insertbackground=BLACK
)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(
    width=38,
    bg=WHITE,
    fg=BLACK,
    highlightthickness=0,
    insertbackground=BLACK
)
email_entry.insert(0, "mytestemail@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(
    width=24,
    bg=WHITE,
    fg=BLACK,
    highlightthickness=0,
    insertbackground=BLACK
)
password_entry.grid(column=1, row=3)

# Buttons
generate_button = Button(
    text="Generate Password",
    width=10,
    highlightbackground=WHITE,
    command=generate_password
)
generate_button.grid(column=2, row=3)

add_button = Button(
    text="Add",
    width=36,
    highlightbackground=WHITE,
    command=save
)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(
    text="Search",
    width=10,
    highlightbackground=WHITE,
    command=find_password
)
search_button.grid(column=2, row=1)


window.mainloop()
