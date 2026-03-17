from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

for char in range(nr_letters):
  password_list.append(random.choice(letters))

for char in range(nr_symbols):
  password_list += random.choice(symbols)

for char in range(nr_numbers):
  password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website_data = website_entry.get()
    username_data = username_entry.get()
    password_data = password_entry.get()

    if len(website_data) == 0 or len(username_data) == 0 or len(password_data) == 0:
        messagebox.showerror("Error", "Please enter all fields")

    else:

        is_ok = messagebox.askokcancel(title=website_data, message=f"These are the details entered: \nEmail: {username_data}\nPassword: {password_data}")

        if is_ok:

            with open("data.txt", "a") as f:
                f.write(f"{website_data} | {username_data} | {password_data}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)











# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")

window.config(padx=50, pady=50)
canvas = Canvas(window, width=200, height=200, bg="white")


logo_image = PhotoImage(file="logo.png")
canvas.create_image(0, 0, image=logo_image, anchor="nw")
canvas.grid(row=0, column=1)

Label(window, text="Website: ").grid(row=1, column=0)

website_entry = Entry(window, width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()

Label(window, text="Email/Username: ").grid(row=2, column=0)
username_entry = Entry(window, width=35)
username_entry.grid(row=2, column=1)
username_entry.insert(0, "ymert9712@gmail.com")


Label(window, text="Password: ").grid(row=3, column=0)
password_entry = Entry(window, width=21)
password_entry.grid(row=3, column=1, sticky=W)

generate_password_button = Button(window, text="Generate Password", width=14)
generate_password_button.grid(row=3, column=2, sticky=E)

add_button = Button(window, text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()