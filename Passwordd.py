import tkinter as tk
import random
import string

root = tk.Tk()


def generate_password():
    username = username_entry.get()
    password_length = int(password_length_entry.get())

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))

    result_label.config(text=f"Generated Password for {username}: {password}")



username_label = tk.Label(root, text=" Enter Username:",font=("calibri",12))
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()


password_length_label = tk.Label(root, text="Enter Password Length:",font=("calibri",10))
password_length_label.pack()
password_length_entry = tk.Entry(root)
password_length_entry.pack()


generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()


result_label = tk.Label(root, text="")
result_label.pack()



root.title("Password Generator")
root.geometry("361x280+400+200")

root.mainloop()