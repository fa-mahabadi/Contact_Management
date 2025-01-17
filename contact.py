class Contact:
    all_contact={}
    
    def add_concat(self,name,email,phone):
        Contact.all_contact[name]={'email':email,"phone":phone}
    def delete_contact(self,name):
        if name in Contact.all_contact:
            Contact.all_contact.pop(name)
    def edit_contact(self,name,new_email,new_phone):
        try:
            if name in Contact.all_contact:
                Contact.all_contact[name]={"email":new_email,"phone":new_phone}
            print(Contact.all_contact)
        except:
            print("user not exist")

c=Contact()
c.add_concat("a","a@yahoo.com","123456")
c.add_concat("b","b@yahoo.com","123466")
# c.delete_contact("a")
c.edit_contact("a","c@yahoo.com","123456")
