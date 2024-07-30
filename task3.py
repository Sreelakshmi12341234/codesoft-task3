
import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    username = username_entry.get()
    try:
        length = int(length_entry.get())
        if length < 1 or length > 20:
            messagebox.showwarning("Input Error", "Password length must be between 1 and 20!")
            return
    except ValueError:
        messagebox.showwarning("Input Error", "Password length must be a valid integer!")
        return
    
    include_letters = letters_var.get()
    include_digits = digits_var.get()
    include_specials = specials_var.get()
    
    if not (include_letters or include_digits or include_specials):
        messagebox.showwarning("Input Error", "Please select at least one character type!")
        return
    
    characters = ""
    if include_letters:
        characters += string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_specials:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    generated_password.set(password)


root = tk.Tk()
root.title("Password Generator")
root.geometry('400x400')


login_frame = tk.Frame(root, bg='#6fa8dc')  
login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

font_style = ('Helvetica', 12)


tk.Label(login_frame, text="Username:", bg='#6fa8dc', font=font_style).grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(login_frame, font=font_style)
username_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(login_frame, text="Password Length (1-20):", bg='#6fa8dc', font=font_style).grid(row=1, column=0, padx=10, pady=10)
length_entry = tk.Entry(login_frame, font=font_style)
length_entry.grid(row=1, column=1, padx=10, pady=10)

letters_var = tk.BooleanVar()
tk.Checkbutton(login_frame, text="Include Letters", variable=letters_var, bg='#6fa8dc', font=font_style).grid(row=2, column=0, columnspan=2, padx=10, pady=5)

digits_var = tk.BooleanVar()
tk.Checkbutton(login_frame, text="Include Digits", variable=digits_var, bg='#6fa8dc', font=font_style).grid(row=3, column=0, columnspan=2, padx=10, pady=5)

specials_var = tk.BooleanVar()
tk.Checkbutton(login_frame, text="Include Special Characters", variable=specials_var, bg='#6fa8dc', font=font_style).grid(row=4, column=0, columnspan=2, padx=10, pady=5)

generate_button = tk.Button(login_frame, text="Generate Password", command=generate_password, bg='#ffd966', font=font_style)  # Light orange button
generate_button.grid(row=5, column=0, columnspan=2, pady=10)

tk.Label(login_frame, text="Generated Password:", bg='#6fa8dc', font=font_style).grid(row=6, column=0, padx=10, pady=10)
generated_password = tk.StringVar()
password_display = tk.Entry(login_frame, textvariable=generated_password, state='readonly', font=font_style)
password_display.grid(row=6, column=1, padx=10, pady=10)


root.mainloop()
