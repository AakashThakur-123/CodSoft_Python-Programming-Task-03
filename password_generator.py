import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        # Label for Password Length
        self.label1 = tk.Label(self.root, text="Password Length:", font=('Arial', 12))
        self.label1.pack(pady=10)

        # Entry for Password Length
        self.length_entry = tk.Entry(self.root, font=('Arial', 14), width=15)
        self.length_entry.pack(pady=5)

        # Checkbox for Uppercase Letters
        self.uppercase_var = tk.BooleanVar()
        self.uppercase_check = tk.Checkbutton(self.root, text="Include Uppercase Letters", variable=self.uppercase_var, font=('Arial', 12))
        self.uppercase_check.pack(pady=5)

        # Checkbox for Lowercase Letters
        self.lowercase_var = tk.BooleanVar()
        self.lowercase_check = tk.Checkbutton(self.root, text="Include Lowercase Letters", variable=self.lowercase_var, font=('Arial', 12))
        self.lowercase_check.pack(pady=5)

        # Checkbox for Digits
        self.digits_var = tk.BooleanVar()
        self.digits_check = tk.Checkbutton(self.root, text="Include Digits", variable=self.digits_var, font=('Arial', 12))
        self.digits_check.pack(pady=5)

        # Checkbox for Symbols
        self.symbols_var = tk.BooleanVar()
        self.symbols_check = tk.Checkbutton(self.root, text="Include Symbols", variable=self.symbols_var, font=('Arial', 12))
        self.symbols_check.pack(pady=5)

        # Button to Generate Password
        self.generate_btn = tk.Button(self.root, text="Generate Password", font=('Arial', 14), command=self.generate_password)
        self.generate_btn.pack(pady=20)

        # Label to Display Generated Password
        self.password_label = tk.Label(self.root, text="Your Password:", font=('Arial', 14))
        self.password_label.pack(pady=10)

    def generate_password(self):
        length = self.length_entry.get()

        if not length.isdigit() or int(length) < 1:
            messagebox.showerror("Error", "Please enter a valid password length.")
            return

        length = int(length)
        character_pool = ""

        if self.uppercase_var.get():
            character_pool += string.ascii_uppercase
        if self.lowercase_var.get():
            character_pool += string.ascii_lowercase
        if self.digits_var.get():
            character_pool += string.digits
        if self.symbols_var.get():
            character_pool += string.punctuation

        if not character_pool:
            messagebox.showerror("Error", "Please select at least one character type.")
            return

        password = ''.join(random.choice(character_pool) for _ in range(length))
        self.password_label.config(text=f"Your Password: {password}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
