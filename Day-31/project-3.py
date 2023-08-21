# Here i am showing the Day 23 practice project

# Contact Manager
import json

class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'phone': self.phone
        }

def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_contacts(contacts):
    contacts_data = [contact.to_dict() for contact in contacts]
    with open('contacts.json', 'w') as file:
        json.dump(contacts_data, file, indent=4)

def main():
    print("Welcome to the Contact Manager!")

    contacts = load_contacts()

    while True:
        print("\nMenu:")
        print("1. Add a new contact")
        print("2. List all contacts")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            email = input("Enter contact email: ")
            phone = input("Enter contact phone: ")

            new_contact = Contact(name, email, phone)
            contacts.append(new_contact)
            save_contacts(contacts)
            print("Contact added successfully!")
        elif choice == '2':
            if not contacts:
                print("No contacts found.")
            else:
                print("Contacts:")
                for idx, contact in enumerate(contacts, start=1):
                    print(f"{idx}. Name: {contact.name}, Email: {contact.email}, Phone: {contact.phone}")
        elif choice == '3':
            print("Exiting the Contact Manager.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()


