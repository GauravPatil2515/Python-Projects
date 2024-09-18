# Contact Book Application

contacts = {}

def display_menu():
    print("\n=== Contact Book App ===")
    print("1. Create Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count Contacts")
    print("7. Exit")

while True:
    display_menu()
    choice = input("Enter your choice (1-7): ")

    if choice == "1":  # Create Contact
        name = input("Enter contact name: ").capitalize()
        if name in contacts:
            print(f"Contact '{name}' already exists!")
        else:
            age = input("Enter age: ")
            email = input("Enter email: ")
            mobile = input("Enter mobile number: ")
            contacts[name] = {"age": int(age), 'email': email, "mobile": mobile}
            print(f"Contact '{name}' has been created successfully!")

    elif choice == "2":  # View Contact
        name = input("Enter contact name to view: ").capitalize()
        if name in contacts:
            contact = contacts[name]
            print(f"\nName: {name}")
            print(f"Age: {contact['age']}")
            print(f"Email: {contact['email']}")
            print(f"Mobile: {contact['mobile']}\n")
        else:
            print(f"Contact '{name}' not found!")

    elif choice == "3":  # Update Contact
        name = input("Enter contact name to update: ").capitalize()
        if name in contacts:
            age = input("Enter updated age: ")
            email = input("Enter updated email: ")
            mobile = input("Enter updated mobile number: ")
            contacts[name] = {"age": int(age), 'email': email, "mobile": mobile}
            print(f"Contact '{name}' has been updated successfully!")
        else:
            print(f"Contact '{name}' not found!")

    elif choice == "4":  # Delete Contact
        name = input("Enter contact name to delete: ").capitalize()
        if name in contacts:
            del contacts[name]
            print(f"Contact '{name}' has been deleted successfully!")
        else:
            print(f"Contact '{name}' not found!")

    elif choice == "5":  # Search Contact
        name = input("Enter contact name to search: ").capitalize()
        if name in contacts:
            print(f"Contact '{name}' exists in the contact book.")
        else:
            print(f"Contact '{name}' not found!")

    elif choice == "6":  # Count Contacts
        print(f"\nTotal contacts: {len(contacts)}")

    elif choice == "7":  # Exit
        print("Exiting Contact Book App. Goodbye!")
        break

    else:
        print("Invalid choice, please select a valid option (1-7).")
