from faker import Faker
import json
from rapidfuzz import process, fuzz
import os
import re

fake = Faker()
FILENAME = "contacts.json"

def format_phone(phone_str):
    digits = "".join(filter(str.isdigit, phone_str))
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return phone_str  # Fallback to raw if it's international or weirdly shaped

def format_email(email_str):
    """Cleans and standardizes email casing and spacing."""
    return email_str.strip().lower()

# Initialize the file with dummy data if it doesn't exist
if not os.path.exists(FILENAME):
    contacts = []
    for _ in range(50):
        contacts.append({
            "name": fake.name(),
            "phone": format_phone(fake.phone_number()),
            "email": format_email(fake.email()),
            "address": fake.address().replace("\n", ", ")
        })
    with open(FILENAME, "w") as f:
        json.dump(contacts, f, indent=2)

def load_contacts():
    with open(FILENAME, "r") as f: 
        return json.load(f)

def save_contacts(contacts_list):
    with open(FILENAME, "w") as f: 
        json.dump(contacts_list, f, indent=2)

def find_contact(contacts_list, query, threshold=70):
    if not contacts_list:
        return None
    names = [c["name"] for c in contacts_list]
    result = process.extractOne(query, names, scorer=fuzz.WRatio)
    # rapidfuzz extractOne returns (match, score, index) or similar depending on version. 
    # To be safe across versions, extract elements reliably:
    if result:
        match_name, score = result[0], result[1]
        if score >= threshold:
            return next(c for c in contacts_list if c["name"] == match_name)
    return None

class ContactBook:
    @staticmethod
    def display_all(contacts_list):
        if not contacts_list:
            print("\n No contacts found.")
            return
        print("\n CONTACT LIST")
        for i, c in enumerate(contacts_list, 1):
            print(f"{i}. {c['name']} | {c['phone']} | {c['email']} | {c['address']}")

    @staticmethod
    def add_contact(contacts_list):
        print("\n Add New Contact ")
        name = input("Enter the name: ").strip() 
        
        exist = find_contact(contacts_list, name, threshold=85)
        if exist:
            print(f"A similar name to '{exist['name']}' is already there.")
            confirm = input("Do you still want to proceed? (y/n): ").strip().lower()
            if confirm != 'y':
                print("Action cancelled.")
                return

        phone = input("Enter the phone number: ").strip()
        email = input("Enter the email: ").strip()
        address = input("Enter the address: ").strip()

        contacts_list.append({
            "name": name, 
            "phone": format_phone(phone), 
            "email": format_email(email), 
            "address": address
        })
        save_contacts(contacts_list)
        print(f"Contact '{name}' added successfully!")

    @staticmethod
    def search_contacts(contacts_list):
        print("\n Search Contacts")
        query = input("Enter search query: ").strip()
        names = [c["name"] for c in contacts_list]
        results = process.extract(query, names, scorer=fuzz.WRatio, limit=5)
        
        print("\n Top Matches")
        found = False
        for name, score, _ in results:
            if score >= 60:
                found = True
                c = next(item for item in contacts_list if item["name"] == name)
                print(f"[{int(score)}%] {c['name']} | {c['phone']} | {c['email']}")
        if not found:
            print("No close matching contacts found.")

    @staticmethod
    def update_contacts(contacts_list):
        print("\n Update a Contact")
        query = input("Enter the name of the contact to update: ").strip()
        contact = find_contact(contacts_list, query)
        if not contact:
            print("No matching contact found.")
            return
        
        print(f"Modifying record for: {contact['name']}")
        new_name = input(f"New name (leave blank to keep '{contact['name']}'): ").strip()
        new_phone = input(f"New phone (leave blank to keep '{contact['phone']}'): ").strip()
        new_email = input(f"New email (leave blank to keep '{contact['email']}'): ").strip()
        new_address = input(f"New address (leave blank to keep '{contact['address']}'): ").strip()

        if new_name: contact['name'] = new_name
        if new_phone: contact['phone'] = format_phone(new_phone)
        if new_email: contact['email'] = format_email(new_email)
        if new_address: contact['address'] = new_address

        save_contacts(contacts_list)
        print(f"Updated: {contact['name']}")

    @staticmethod
    def delete_contacts(contacts_list):
        print("\n Delete a Contact")
        query = input("Enter the name of the contact to delete: ").strip()
        contact = find_contact(contacts_list, query)
        if not contact:
            print("No matching contact found.")
            return
        
        confirm = input(f"Are you sure you want to delete '{contact['name']}'? (y/n): ").strip().lower()
        if confirm == 'y':
            contacts_list.remove(contact)
            save_contacts(contacts_list)
            print(f"Deleted contact successfully.")

def main():
    while True: # Keep CLI running inside a loop
        contacts_list = load_contacts() # Read live states on every cycle

        choose = input('''
Welcome to the Contact Book CLI:
(1) Display all contacts
(2) Add a contact
(3) Search contacts (Fuzzy)
(4) Update a contact
(5) Delete a contact
(6) Exit CLI
Choose an option (1-6): ''').strip()

        if choose == "1":
            ContactBook.display_all(contacts_list)
        elif choose == "2":
            ContactBook.add_contact(contacts_list)
        elif choose == "3":
            ContactBook.search_contacts(contacts_list)
        elif choose == "4":
            ContactBook.update_contacts(contacts_list)
        elif choose == "5":
            ContactBook.delete_contacts(contacts_list)
        elif choose == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please type a number between 1 and 6.")

if __name__ == "__main__":
    main()
