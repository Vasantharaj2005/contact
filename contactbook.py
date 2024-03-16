import json

CONTACTS_FILE = "contacts.json"

def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(name, phone, email, address):
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contacts(contacts)

def view_contacts():
    contacts = load_contacts()
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']}: {contact['phone']}")

def search_contact(query):
    contacts = load_contacts()
    found_contacts = []
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query in contact['phone']:
            found_contacts.append(contact)
    return found_contacts

def update_contact(index, name, phone, email, address):
    contacts = load_contacts()
    if 0 < index <= len(contacts):
        contacts[index - 1] = {"name": name, "phone": phone, "email": email, "address": address}
        save_contacts(contacts)
        return True
    return False

def delete_contact(index):
    contacts = load_contacts()
    if 0 < index <= len(contacts):
        del contacts[index - 1]
        save_contacts(contacts)
        return True
    return False

def main():
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(name, phone, email, address)
            print("Contact added successfully!")

        elif choice == "2":
            print("\n--- Contact List ---")
            view_contacts()

        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            found_contacts = search_contact(query)
            if found_contacts:
                print("\n--- Search Results ---")
                for contact in found_contacts:
                    print(f"Name: {contact['name']}, Phone: {contact['phone']}")
            else:
                print("No matching contacts found.")

        elif choice == "4":
            view_contacts()
            index = int(input("Enter the index of contact to update: "))
            name = input("Enter new name: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            if update_contact(index, name, phone, email, address):
                print("Contact updated successfully!")
            else:
                print("Invalid index.")

        elif choice == "5":
            view_contacts()
            index = int(input("Enter the index of contact to delete: "))
            if delete_contact(index):
                print("Contact deleted successfully!")
            else:
                print("Invalid index.")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
