import pickle


class Contact:
    all_contact = {}

    @classmethod
    def save_contacts(cls):
        """save contact to pickle file"""
        with open("data/contacts.pkl", "wb") as f:
            pickle.dump(cls.all_contact, f)

    @classmethod
    def load_contacts(cls):
        """load contact from pickle file"""
        with open("data/contacts.pkl", "rb") as f:
            cls.all_contact = pickle.load(f)

    @classmethod
    def add_contact(cls, name, email, phone):
        """add new contact"""
        cls.all_contact[name] = {"email": email, "phone": phone}
        cls.save_contacts()

    @classmethod
    def delete_contact(cls, name):
        """delete a contact"""
        if name in cls.all_contact:
            cls.all_contact.pop(name)
            cls.save_contacts()

    @classmethod
    def edit_contact(cls, name, new_email, new_phone):
        """edit existing contact"""
        if name in cls.all_contact:
            cls.all_contact[name] = {"email": new_email, "phone": new_phone}
            cls.save_contacts()
        else:
            print(f"{name} not exist")

    @classmethod
    def diaplay_all_contact(cls):
        """display all contact from file"""
        cls.load_contacts()
        for name, details in cls.all_contact.items():
            email = details["email"]
            phone = details["phone"]
            print(f"Name: {name}, Email: {email}, Phone: {phone}")
