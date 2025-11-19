import re 

class Contact():
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        
cnt = Contact("test_user", +998942314354, "test_email@gmail.com")
contacts = [cnt]

def add_contact(s:list):
    name = input("Enter name: ")
    
    phone_check = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
    phone = input("Enter phone number: ")
    while True:
        if re.match(phone_check, phone):
            break
        else:
            print('something is incorrect, try again')
            phone = input("Enter phone number: ")

    email_check = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
    email = input("enter email: ")
    while True:
        if re.match(email_check, email):
            break
        else:
            print('something is incorrect, try again')
            email = input("Enter email: ")
    
    cnt_ = Contact(name, phone, email)
    contacts.append(cnt_)
    print("Contact added successfully!\n")


def view_contacts(s:list):
    if not contacts:
        print("No contacts added yet.\n")
        return
    count=0
    for item in contacts:
        count += 1
        print(f"{count}. name: {item.name} \n   phone: {item.phone} \n   email: {item.email}")
    print()


def update_contact(s: list):
    if not contacts:
        print("No contacts to update.")
        return
    
    print("Select contact to update:")
    view_contacts(contacts)
    
    try:
        index = int(input("Enter contact number: ")) - 1
        if index < 0 or index >= len(contacts):
            print("Invalid selection.")
            return
    except ValueError:
        print("Invalid input.")
        return
    
    contact = contacts[index]
    print(f"Updating contact: {contact.name}")

    new_name = input(f"Enter new name (press Enter to keep '{contact.name}'): ")
    if new_name.strip():
        contact.name = new_name

    phone_check = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
    new_phone = input(f"Enter new phone (press Enter to keep '{contact.phone}'): ")
    if new_phone.strip():
        while not re.match(phone_check, new_phone):
            print("incorrect phone format, try again.")
            new_phone = input("Enter new phone: ")
        contact.phone = new_phone

    email_check = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
    new_email = input(f"Enter new email (press Enter to keep '{contact.email}'): ")
    if new_email.strip():
        while not re.match(email_check, new_email):
            print("incorrect email, try again.")
            new_email = input("Enter new email: ")
        contact.email = new_email

    print("Contact updated successfully!\n")

def sms_manager(s: list):
    while True:
        print("---- SMS Manager ----")
        print("1. View contacts")
        print("2. Send message")
        print("3. Back to main menu")
        choice = input("Choose action: ")

        if choice == "1":
            view_contacts(contacts)

        elif choice == "2":
            if not contacts:
                print("No contacts to message.\n")
                continue
            
            view_contacts(contacts)
            try:
                idx = int(input("Choose contact number: ")) - 1
                if idx < 0 or idx >= len(contacts):
                    print("Invalid selection.\n")
                    continue
            except ValueError:
                print("Invalid input.\n")
                continue

            contact = contacts[idx]
            msg = input(f"Enter message for {contact.name}: ")
            
            print(f"\nSending message to {contact.name} ({contact.phone})...")
            print(f"Message: {msg}")
            print("Message sent!\n")

        elif choice == "3":
            break

        else:
            print("Invalid choice!\n")


def main_menu():
    while True:
        print("====== MAIN MENU ======")
        print("1. Contact Manager")
        print("2. SMS Manager")
        print("3. Exit")

        choice = input("Choose action: ")

        if choice == "1":
            contact_manager(contacts)
        elif choice == "2":
            sms_manager(contacts)
        elif choice == "3":
            print("Exiting system...")
            break
        else:
            print("Invalid choice!\n")


def contact_manager(s:list):
    while True:
        a = input("1. add contact \n2. view contacts \n3. update contact \n4. back to main menu \nChoose action: ")
        if a == "1":
            add_contact(contacts)
        elif a == "2":
            view_contacts(contacts)
        elif a == "3":
            update_contact(contacts)
        elif a == "4":
            break
        else:
            print("Invalid choice!\n")

main_menu()
