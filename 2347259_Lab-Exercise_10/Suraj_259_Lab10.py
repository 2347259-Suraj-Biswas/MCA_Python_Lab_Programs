import tkinter as tk
from tkinter import messagebox
import re 
from tkinter import ttk

def validate_name(name):
    if re.match(name_pattern, name) or not name:
        return True
    else:
        messagebox.showerror("Error", "Name should only contain alphabetic characters.")
        return False

def validate_age(age):
    if age.isnumeric() and 18 <= int(age) <= 100:
        return True
    else:
        messagebox.showerror("Error", "Age should be a numeric value between 18 and 100.")
        return False

def validate_contact(contact):
    if re.match(contact_pattern, contact) or not contact:
        return True
    else:
        messagebox.showerror("Error", "Contact number should be a 10-digit numeric value.")
        return False

def validate_email(email):
    if re.match(email_pattern, email) or not email:
        return True
    else:
        messagebox.showerror("Error", "Please provide a valid email address.")
        return False

def submit_form():
    donor_info = {
        "Name": name_entry.get(),
        "Gender": gender_var.get(),
        "Age": age_var.get(),
        "Blood Type": blood_type_var.get(),
        "Contact": contact_entry.get(),
        "Email": email_entry.get()
    }

    if not validate_name(donor_info["Name"]):
        return

    if not validate_age(donor_info["Age"]):
        return

    if not validate_contact(donor_info["Contact"]):
        return

    if not validate_email(donor_info["Email"]):
        return

    if all(donor_info.values()):
        messagebox.showinfo("Success", "Donor registration successful!")
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

root = tk.Tk()
root.title("Blood Bank Donor Registration Form")
root.geometry("300x250")

labels = ["Name", "Age", "Blood Type", "Contact", "Email", "Gender"]

for i, label_text in enumerate(labels):
    label = tk.Label(root, text=label_text)
    label.grid(row=i, column=0)

name_pattern = r"^[A-Za-z]+$"
contact_pattern = r"^\d{10}$"
email_pattern = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$"

name_entry = tk.Entry(root)
age_var = tk.StringVar(root)
age_spinbox = tk.Spinbox(root, from_=18, to=100, textvariable=age_var)
age_spinbox.grid(row=1, column=1)

blood_type_var = tk.StringVar(root)
blood_type_var.set("A+")
blood_type_menu = tk.OptionMenu(root, blood_type_var, "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-")
contact_entry = tk.Entry(root)
email_entry = tk.Entry(root)
entry_fields = [name_entry, age_spinbox, blood_type_menu, contact_entry, email_entry]

for i, entry_field in enumerate(entry_fields):
    entry_field.grid(row=i, column=1)

gender_var = tk.StringVar(root)
gender_var.set("Male")
gender_combobox = ttk.Combobox(root, textvariable=gender_var, values=["Male", "Female"])
gender_combobox.grid(row=5, column=1)

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=len(labels), columnspan=2, pady=10)

root.mainloop()
