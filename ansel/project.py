import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database setup
def init_db():
    conn = sqlite3.connect('registrations.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            reg_number TEXT,
            address TEXT,
            email TEXT,
            sex TEXT,
            age INTEGER,
            phone TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Save data to database
def submit_form():
    conn = sqlite3.connect('registrations.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (name, reg_number, address, email, sex, age, phone)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        name_var.get(),
        reg_var.get(),
        address_var.get(),
        email_var.get(),
        sex_var.get(),
        age_var.get(),
        phone_var.get()
    ))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Data submitted successfully!")
    clear_fields()

# Clear form fields after submission
def clear_fields():
    for var in [name_var, reg_var, address_var, email_var, sex_var, age_var, phone_var]:
        var.set("")

# Initialize DB
init_db()

# GUI Setup
app = tk.Tk()
app.title("Student Registration Form")

name_var = tk.StringVar()
reg_var = tk.StringVar()
address_var = tk.StringVar()
email_var = tk.StringVar()
sex_var = tk.StringVar()
age_var = tk.StringVar()
phone_var = tk.StringVar()

fields = [("Name", name_var), ("Registration Number", reg_var), ("Home Address", address_var),
          ("Email Address", email_var), ("Sex", sex_var), ("Age", age_var), ("Phone Number", phone_var)]

for idx, (label, var) in enumerate(fields):
    tk.Label(app, text=label).grid(row=idx, column=0, padx=10, pady=5, sticky='w')
    tk.Entry(app, textvariable=var).grid(row=idx, column=1, padx=10, pady=5)

tk.Button(app, text="Submit", command=submit_form).grid(row=len(fields), column=0, columnspan=2, pady=10)

app.mainloop()
