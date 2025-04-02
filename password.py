import tkinter as tk
from tkinter import messagebox

def check_password_strength():
    password = password_entry.get()
    length = len(password)
    
    if length == 0:
        strength_label.config(text="Please enter a password", fg="red")
    elif length < 6:
        strength_label.config(text="Weak", fg="red")
    elif length < 10:
        strength_label.config(text="Moderate", fg="orange")
    else:
        strength_label.config(text="Strong", fg="green")

# Create main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x200")

# Create and place widgets
tk.Label(root, text="Enter Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*", width=25)
password_entry.pack(pady=5)

tk.Button(root, text="Check Strength", command=check_password_strength).pack(pady=5)

strength_label = tk.Label(root, text="", font=("Arial", 12))
strength_label.pack(pady=5)

# Run the application
root.mainloop()
