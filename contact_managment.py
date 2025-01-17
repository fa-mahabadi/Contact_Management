import re
from contact import Contact
from user import User


def main():
    phone_regex = r"^\+98[9]{1}[1-9]{1}[0-9]{8}$|^09[1-9]{1}[0-9]{8}$"
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-z0-9.-]+\.[a-zA-Z]{2,}$"
    print("Welcome to Contact Management System ")
    choice = int(
        input("What you do: (1) create account  (2) change password (3) login : ")
    )
    if choice == 1:
        username = input("Enter username: ")
        password = input("Enter password: ")
        User.create_account(username, password)
        print("Account created successfully.")
    elif choice == 2:
        username = input("Enter username: ")
        User.load_users()
        if username in User.accounts:
            new_password = input("Enter new password: ")
            User.modify_account(username, new_password)
            print("Modify password successfully.")
    elif choice == 3:
        username = input("Enter username: ")
        password = input("Enter password: ")
        User.authentication(username, password)
        print(f"Welcome {username}")
        while True:
            print("1. Add a new contact")
            print("2. Edit an existing contact")
            print("3. Delete a contact")
            print("4. View all contacts")
            print("5. Quit")
            select_menu = int(input("Enter number of menu: "))

            if select_menu == 1:
                name = input("Enter name: ")
                email = input("Enter email: ")
                phone = input("Enter phone: ")
                if re.match(phone_regex, phone):
                    if re.match(email_regex, email):
                        Contact.add_contact(name, email, phone)
                    else:
                        print(f"{email} is invalid")
                else:
                    print(f"{phone} is invalid")

            elif select_menu == 2:
                name = input("Enter your name: ")
                new_email = input("Enter new email: ")
                new_phone = input("Enter new phone: ")
                if re.match(phone_regex, new_phone):
                    if re.match(email_regex, new_email):
                        Contact.edit_contact(name, new_email, new_phone)
                    else:
                        print(f"{new_email} is invalid")
                else:
                    print(f"{new_phone} is invalid")

            elif select_menu == 3:
                name = input("Enter name: ")
                Contact.delete_contact(name)

            elif select_menu == 4:
                Contact.diaplay_all_contact()

            elif select_menu == 5:
                break


if __name__ == "__main__":
    main()
