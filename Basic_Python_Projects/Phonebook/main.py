
# Phonebook Application

phonebook = {}

def add_contact(name, contact_no):
    """Add or update a contact in the phonebook."""
    phonebook[name] = contact_no
    return f'Contact {name} updated.'

def search(info):
    """Search for a contact by name or phone number."""
    for name, contact in phonebook.items():
        if info.lower() in name.lower() or info in contact:
            return f'{name}: {contact}'
    return f'No contacts found matching {info}.'    

def delete(info):
    """Delete a contact from the phonebook."""
    for name, contact in list(phonebook.items()):
        if info.lower() in name.lower() or info in contact:
            del phonebook[name]
            return f'Contact {name} deleted.'
    return f'Contact not found.'

def display():
    """Display contacts."""
    for name, contact in phonebook.items():
        print(f'{name}: {contact}')

def main():
    while True:
        print("\nPhonebook Menu")
        print("1. Add/Update Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Display All Contacts")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter name: ")
            number = input("Enter phone number: ")
            add_contact(name, number)
        elif choice == '2':
            info = input("Enter name or contact to search: ")
            search(info)
        elif choice == '3':
            info = input("Enter name or contact to delete: ")
            delete(info)
        elif choice == '4':
            display()
        elif choice == '5':
            print("Exiting phonebook.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()