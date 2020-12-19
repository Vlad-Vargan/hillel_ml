"""
Телефонний довідник.
Напишіть програму, що буде реалізовувати простий телефонний довідник. При запуску програми довідник порожній. Далі у користувача повинна бути можливість інтерактивно виконувати наступні операції, вводячи їх з клавіатури:
- insert <Name> <Number> - додати в телефонний довідник новий запис про користувача і його номер телефону.
- delete <Name> - видалити з телефонного довідника користувача і його номер телефону.
- get <Name> - дізнатися номер телефону по імені користувача.
<Name> - рядок із символів англійського алфавіту в верхньому або нижньому регістрі без роздільників.
<Number> - рядок з цифр.
Імена не повторюються. Кожному імені може відповідати рівно один номер телефону. Зберігати дані між запусками програми не потрібно.

Вхідні дані:
Набір операцій insert, delete, get з правильними аргументами в довільному порядку.

Вихідні дані:
Результати виконання команд get <Name>:
- Номер телефону користувача з ім'ям <Name> в разі наявності запису про нього.
- "Not found" в іншому випадку.

Вхідні дані:
insert Taras 252617
get Taras
delete Taras
get Taras

Вихідні дані:
252617
Not found

# ООП
# Переробити попереднє завдання з телефонним довідником із застосуванням класу для представленням довідника
"""

import re


class phone_CRM:
    phones = dict()

    @staticmethod
    def check_phone(phone):
        regex = '^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$'
        phone_is_valid = re.search(regex, phone)
        if phone_is_valid:
            print("Valid phone")
        else:
            print("Invalid phone")
        return phone_is_valid


    def insert(self, name, number):
        # insert <Name> <Number> - додати в телефонний довідник 
        # новий запис про користувача і його номер телефону.
        if phone_CRM.check_phone(number):
            phones = self.phones
            if name not in phones:
                phones[name] = number
                print(f"{name}: {number} added")
            else:
                phones[name] = number
                print(f"{name}: {number} rewritten")


    def get(self, name):
        # get <Name> - дізнатися номер телефону по імені користувача.
        phones = self.phones
        if name in phones:
            print(f"{name}: {phones[name]}")
        else:
            print(f"{name} does not exist")


    def delete(self, name):
        # delete <Name> - видалити з телефонного довідника користувача і його номер телефону.
        phones = self.phones
        if name in phones:
            phones.pop(name)
            print(f"{name} was removed")
        else:
            print(f"{name} does not exist in system")


    def __str__(self):
        # Вивести список всіх phones
        return str(self.phones)


new_crm = phone_CRM()

new_crm.insert("vlad", "+38050978597")
new_crm.insert("vlad", "+38050975557")
print(new_crm)

new_crm.get("vlad")
new_crm.get("dimas")
print(new_crm)


new_crm.insert("dimas", "+1111111111")
new_crm.get("dimas")
print(new_crm)


new_crm.delete("vlad")
new_crm.delete("dimas")
new_crm.get("dimas")
print(new_crm)