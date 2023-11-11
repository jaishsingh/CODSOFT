import tkinter as tk
from tkinter import StringVar
import secrets
import string

def generate_password():
    length = int(length_var.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))  
    password_var.set(password)

win = tk.Tk()
win.title("Password Generator")

tk.Label(win, text="Password Length:",background="white").pack(pady=10,padx=100)
length_var = StringVar()
length_entry = tk.Entry(win, textvariable=length_var,background="yellow")
length_entry.pack(pady=10,padx=100)

generate_button = tk.Button(win, text="Generate password", command=generate_password,bg="gray")
generate_button.pack(pady=10,padx=100)

password_var = StringVar()
password_entry = tk.Entry(win, textvariable=password_var, state='readonly')
password_entry.pack(pady=10,padx=100)

win.mainloop()
