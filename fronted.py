import tkinter as tk
from tkinter import messagebox
import subprocess

def add_contact():
    name = entry_name.get()
    phone_number = entry_phone.get()
    address = entry_address.get()

    if name and phone_number and address:
        contact_details = f"{name}|{phone_number}|{address}"

        # Read existing contacts from file
        contacts = []
        with open("phonebook.txt", "r") as file:
            for line in file:
                contact = line.rstrip('\n')
                if contact:
                    contacts.append(contact)

        # Check if contact already exists
        if any(contact.startswith(f"{name}|{phone_number}|") for contact in contacts):
            messagebox.showinfo("Contact Exists", "A contact with the same phone number already exists.")
        else:
            # Insert the new contact in sorted order
            index = 0
            for index, contact in enumerate(contacts):
                if contact > contact_details:
                    break
            contacts.insert(index, contact_details)

            # Write the updated contact list back to the file, removing any empty lines
            with open("phonebook.txt", "w") as file:
                file.write('\n'.join(contacts))

            # Clear the entry fields after adding a contact
            entry_name.delete(0, tk.END)
            entry_phone.delete(0, tk.END)
            entry_address.delete(0, tk.END)

            show_contact_added_message()
    else:
        messagebox.showerror("Error", "Please enter all contact details.")
        entry_name.focus_set()



def search_contact():
    name = entry_search.get()

    if name:
        with open("phonebook.txt", "r") as file:
            for line in file:
                contact = line.strip().split("|")
                if contact[0] == name:
                    contact_details = f"Name: {contact[0]}\nPhone Number: {contact[1]}\nAddress: {contact[2]}"
                    messagebox.showinfo("Contact Found", contact_details)
                    break
            else:
                messagebox.showinfo("Contact Not Found", "Contact not found.")

        # Clear the search field after displaying the result
        entry_search.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter a contact name to search.")

# Create the GUI
root = tk.Tk()

label_name = tk.Label(root, text="Name:")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()

label_phone = tk.Label(root, text="Phone Number:")
label_phone.pack()
entry_phone = tk.Entry(root)
entry_phone.pack()

label_address = tk.Label(root, text="Address:")
label_address.pack()
entry_address = tk.Entry(root)
entry_address.pack()

button_add = tk.Button(root, text="Add Contact", command=add_contact)
button_add.pack()

label_search = tk.Label(root, text="Search:")
label_search.pack()
entry_search = tk.Entry(root)
entry_search.pack()

button_search = tk.Button(root, text="Search Contact", command=search_contact)
button_search.pack()

root.mainloop()
