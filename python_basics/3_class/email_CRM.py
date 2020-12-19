import re


class email_CRM:
    # Написати програму, що дозволить підтримувати список електронних адрес для розсилки. 
    # Програма повинна дозволяти додавати, перевіряти наявність і видаляти електронні адреси.
    emails = []

    @staticmethod
    def check_email(email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        email_is_valid = re.search(regex, email)
        if email_is_valid:
            print("Valid Email")
        else:
            print("Invalid Email")
        return email_is_valid


    def add(self, new_email):
        # Програма повинна дозволяти додавати
        if email_CRM.check_email(new_email):
            emails = self.emails
            if new_email not in emails:
                emails.append(new_email)
                print(f"{new_email} added")
            else:
                print(f"{new_email} already exist")



    def find(self, email):
        # перевіряти наявність
        if email_CRM.check_email(email):
            emails = self.emails
            if email in emails:
                print(f"{email} exist")
            else:
                print(f"{email} does not exist")


    def delete(self, email):
        # видаляти електронні адреси
        if email_CRM.check_email(email):
            emails = self.emails
            if email in emails:
                emails.remove(email)
                print(f"{email} was removed")
            else:
                print(f"{email} does not exist in system")


    def __str__(self):
        # Вивести список всіх Emails
        return str(self.emails)


new_crm = email_CRM()

new_crm.add("ankitrai326@gmail.com")
new_crm.add("ankitrai326@gmail.com")
print(new_crm)

new_crm.find("ankitrai326@gmail.com")
new_crm.find("my.ownsite@ourearth.org")
print(new_crm)


new_crm.add("my.ownsite@ourearth.org")
new_crm.find("my.ownsite@ourearth.org")
print(new_crm)


new_crm.delete("ankitrai326@gmail.com")
new_crm.delete("ankitrai326@gmail.com")
new_crm.find("ankitrai326@gmail.com")
print(new_crm)
