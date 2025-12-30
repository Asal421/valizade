import tkinter as tk
from tkinter import messagebox
import csv
import os

FILE_NAME = "contacts.csv"

contacts = []

def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                contacts.append(row)
        show_contacts(contacts)

def save_contacts():
    with open(FILE_NAME, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(contacts)

def show_contacts(data):
    listbox.delete(0, tk.END)
    for c in data:
        listbox.insert(tk.END, f"{c[0]} - {c[1]}")

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()

    if name == "" or phone == "":
        messagebox.showwarning("خطا", "همه فیلدها را پر کنید")
        return

    contacts.append([name, phone])
    show_contacts(contacts)
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

def search_contact():
    text = entry_search.get()
    result = [c for c in contacts if text in c[0]]
    show_contacts(result)

def delete_contact():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("خطا", "یک مخاطب انتخاب کنید")
        return

    index = selected[0]
    value = listbox.get(index)

    name = value.split(" - ")[0]

    for c in contacts:
        if c[0] == name:
            contacts.remove(c)
            break

    show_contacts(contacts)

def exit_program():
    save_contacts()
    root.destroy()

root = tk.Tk()
root.title("دفترچه تلفن")

tk.Label(root, text="نام:").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="شماره:").grid(row=1, column=0)
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1)

tk.Button(root, text="افزودن", command=add_contact).grid(row=2, column=0, columnspan=2, pady=5)

tk.Label(root, text="جستجو:").grid(row=3, column=0)
entry_search = tk.Entry(root)
entry_search.grid(row=3, column=1)

tk.Button(root, text="جستجو", command=search_contact).grid(row=4, column=0, columnspan=2)

listbox = tk.Listbox(root, width=30)
listbox.grid(row=5, column=0, columnspan=2, pady=10)

tk.Button(root, text="حذف", command=delete_contact).grid(row=6, column=0)
tk.Button(root, text="خروج", command=exit_program).grid(row=6, column=1)

load_contacts()
root.mainloop()
