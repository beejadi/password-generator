
import random
import string
import tkinter as tk
from tkinter import ttk

def generate_password():
    password_length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_label.config(text="Generated Password: " + password)

# Create the main application window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
length_label = ttk.Label(root, text="Password Length:")
length_label.pack()

length_entry = ttk.Entry(root)
length_entry.pack()

generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_label = ttk.Label(root, text="")
password_label.pack()

# Start the main event loop
root.mainloop()