import json

FILE = "contacts.json"

def load_contacts():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print("Contact added successfully.")

def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(contacts[name])
    else:
        print("Contact not found.")

def update_contact(contacts):
    name = input("Enter name to update: ").strip()
    if name in contacts:
        contacts[name]["phone"] = input("Enter new phone: ").strip()
        contacts[name]["email"] = input("Enter new email: ").strip()
        save_contacts(contacts)
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    contacts = load_contacts()
    while True:
        print("\n--- Contact Book ---")
        print("1. Add  2. Search  3. Update  4. Delete  5. Exit")
        choice = input("Enter choice: ")
        if choice == "1": add_contact(contacts)
        elif choice == "2": search_contact(contacts)
        elif choice == "3": update_contact(contacts)
        elif choice == "4": delete_contact(contacts)
        elif choice == "5": break
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()
