class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactManagementSystem:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}")
            print(f"Phone: {contact.phone_number}")
            print(f"Email: {contact.email}")
            print("-" * 10)

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def delete_contact(self, contact):
        self.contacts.remove(contact)

# Main program
contact_system = ContactManagementSystem()

while True:
    print("Contact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")

        contact = Contact(name, phone_number, email)
        contact_system.add_contact(contact)
        print("Contact added successfully!")

    elif choice == '2':
        contact_system.display_contacts()

    elif choice == '3':
        name = input("Enter name to search: ")
        contact = contact_system.search_contact(name)
        if contact:
            print(f"Name: {contact.name}")
            print(f"Phone: {contact.phone_number}")
            print(f"Email: {contact.email}")
        else:
            print("Sorry..! Contact not found!")

    elif choice == '4':
        name = input("Enter name to delete: ")
        contact = contact_system.search_contact(name)
        if contact:
            contact_system.delete_contact
