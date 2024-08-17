#include<stdio.h>
import random
from tkinter import *
from tkinter.ttk import *

def low():
    entry.delete(0, END)
    length = var1.get()
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""
    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(lower)
        return password
    elif var.get() == 0:
        for i in range(0, length):
            password = password + random.choice(upper)
        return password
    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(digits)
        return password
    else:
        print("Please choose an option")

def generate():
    password1 = low()
    entry.insert(10, password1)

def copy1():
    random_password = entry.get()
    root.clipboard_clear()
    root.clipboard_append(random_password)

root = Tk()
var = IntVar()
var1 = IntVar()

root.title("Random Password Generator")
root.configure(bg="#f0f0f0")

style = Style()
style.configure('TLabel', background="#f0f0f0", foreground="#333333", font=("Arial", 12))
style.configure('TButton', font=("Arial", 10), background="#ffffff")
style.configure('TRadiobutton', background="#f0f0f0", foreground="#333333", font=("Arial", 12))
style.configure('TCombobox', font=("Arial", 12))

Random_password = Label(root, text="Password")
Random_password.grid(row=0, column=0, padx=10, pady=10, sticky="W")

entry = Entry(root, width=24, font=("Arial", 14))
entry.grid(row=0, column=1, padx=10, pady=10)

c_label = Label(root, text="Length")
c_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

copy_button = Button(root, text="Copy", command=copy1)
copy_button.grid(row=0, column=2, padx=10, pady=10)

generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=0, column=3, padx=10, pady=10)

radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=1, column=2, padx=10, pady=10, sticky="W")

radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
radio_middle.grid(row=1, column=3, padx=10, pady=10, sticky="W")

radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.grid(row=1, column=4, padx=10, pady=10, sticky="W")

combo = Combobox(root, textvariable=var1, width=5)
combo['values'] = tuple(range(8, 33))
combo.current(0)
combo.grid(column=1, row=1, padx=10, pady=10, sticky="W")

root.mainloop()