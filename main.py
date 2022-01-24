from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get().title()
    email = email_username_entry.get()
    email_pass = password_entry.get()
    password_data = {
        website: {
            "email": email,
            "password": email_pass
        }
    }

    if website == "" or email_pass == "":
        messagebox.showinfo(title="oops", message="Please don't leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title="hello", message=f"These are the details entered: \nEmail:{email}\n"
                                                              f"password:{email_pass} \n Is it okay to save?")
        if is_ok:
            try:
                with open("password_manager.json", mode="r") as password_manager:
                    data = json.load(password_manager)
                    data.update(password_data)
            except FileNotFoundError:
                with open("password_manager.json", mode="w") as password_manager:
                    json.dump(password_data, password_manager, indent=4)
            else:
                with open("password_manager.json", mode="w") as password_manager:
                    json.dump(data, password_manager, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def find_password():
    user_website = website_entry.get().title()
    try:
        with open("password_manager.json", mode="r") as file:
            user_data = json.load(file)
        website_data_email = user_data[user_website]["email"]
        website_data_pass = user_data[user_website]["password"]
    except KeyError:
        messagebox.showinfo(title="", message="No details for the website exists")
    except:
        messagebox.showinfo(title="", message="No Data File Found")
    else:
        messagebox.showinfo(title=user_website, message=f" email: {website_data_email}\npassword: {website_data_pass}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# website

website_text = Label(text="Website:")
website_text.grid(row=1, column=0)

website_btn = Button(text="Search", width=12, command=find_password)
website_btn.grid(row=1, column=2)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
# website_entry.focus()

# print(hi)
# EMail/Username

email_username = Label(text="Email/Username:")
email_username.grid(row=2, column=0)

email_username_entry = Entry(width=38)
email_username_entry.insert(0, "aogunnola@gmail.com")
email_username_entry.grid(row=2, column=1, columnspan=2)

# Password

password_text = Label(text="Password:")
password_text.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

password_btn = Button(text="Generate Password", highlightthickness=0, width=12, command=generate_pass)
password_btn.grid(row=3, column=2)

# Add

add_btn = Button(text="Add", width=36, command=save_password)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()

print(website_entry.get())
