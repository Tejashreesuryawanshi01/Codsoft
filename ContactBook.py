from tkinter import*
import tkinter as tk
from tkinter import simpledialog

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")
        self.master.geometry("500x500+50+50")
        self.master.configure(bg="pink")

        self.add_button =tk.Button(master,text="Add Contact",bd ='5',command=self.add_contact)
        self.view_button =tk.Button(master,text="View Contact",bd ='5',command=self.view_contacts)
        self.search_button =tk.Button(master,text="Search Contact",bd ='5',command=self.search_contacts)
        self.update_button =tk.Button(master,text="Update Contact",bd ='5',command=self.update_contact)
        self.delete_button =tk.Button(master,text="Delete Contact",bd ='5',command=self.delete_contact)
        
        self.add_button.pack(pady=15)
        self.view_button.pack(pady=15)
        self.search_button.pack(pady=15)
        self.update_button.pack(pady=15)
        self.delete_button.pack(pady=15)

        self.contacts = []

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter Name:")
        phone = simpledialog.askstring("Input", "Enter Phone:")
        email = simpledialog.askstring("Input", "Enter Email:")
        address = simpledialog.askstring("Input", "Enter Address:")

        contact=Contact(name,phone,email,address)
        self.contacts.append(contact)
        print("Contact Added:",contact.__dict__)

    def view_contacts(self):  
        if not self.contacts:
           print("No contacts for display")
        else:
             for contact in self.contacts:
              print("Name:",contact.name,"Phone:",contact.phone,"Email:",contact.email,"Address:",contact.address)

    def search_contacts(self): 

        search_term = simpledialog.askstring("Input", "Enter Name or Phone to Search:")
        results = [contact for contact in self.contacts
                   if search_term.lower() in contact.name.lower() or
                   search_term in contact.phone]
        
        if results:
            print("Search Results:")
            for result in results:
                print(result.__dict__)
        else:
            print("No matching contacts found.")    

    def update_contact(self):
        if not self.contacts:
            print("No contacts to update.")
            return

        name_to_update = simpledialog.askstring("Input", "Enter Name of Contact to Update:")
        matching_contacts = [contact for contact in self.contacts if contact.name.lower() == name_to_update.lower()]    
        
        if not matching_contacts:
            print(f"No contacts found with the name {name_to_update}.")
            return
        
        contact_to_update=matching_contacts[0]
        print("Current Contact Details",contact_to_update.__dict__)

        new_name = simpledialog.askstring("Input", "Enter Name:")
        new_phone = simpledialog.askstring("Input", "Enter Phone:")
        new_email = simpledialog.askstring("Input", "Enter Email:")
        new_address = simpledialog.askstring("Input", "Enter Address:")

        contact_to_update.name=new_name
        contact_to_update.phone=new_phone
        contact_to_update.email=new_email
        contact_to_update.address=new_address

        print("Contact Updated:",contact_to_update.__dict__)

    def delete_contact(self):
        
        def delete_contact(self):
    
         if not self.contacts:
            print("No contacts to delete.")
            return

        name_to_delete = simpledialog.askstring("Input", "Enter Name of Contact to Delete:")
        matching_contacts = [contact for contact in self.contacts if contact.name.lower() == name_to_delete.lower()]

        if not matching_contacts:
            print(f"No contacts found with the name {name_to_delete}.")
            return

        contact_to_delete = matching_contacts[0]
        print("Deleting Contact:", contact_to_delete.__dict__)
        self.contacts.remove(contact_to_delete)
        print("Contact Deleted.")    

if __name__=="__main__":
     root =tk.Tk()
     app = ContactApp(root)
     root.mainloop()
            








         

        




