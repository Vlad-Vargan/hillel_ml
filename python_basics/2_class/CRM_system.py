class CRM:
    # Реалізуйте CRM систему, яка повинна приймати й обробляти запити наступних видів:
    employees = []


    def add(self, new_employee):
        # Додати працівника з іменем <name> у систему.
        # add
        # <name>
        employees = self.employees
        if new_employee not in employees:
            employees.append(new_employee)
            print(f"{new_employee} added")
        else:
            print(f"{new_employee} already exist")


    def find(self, employee):
        # Перевірити чи є працівник з іменем <name> у системі.
        # find
        # <name>
        employees = self.employees
        if employee in employees:
            print(f"{employee} exist")
        else:
            print(f"{employee} does not exist")


    def delete(self, employee):
        # Видалити працівника з іменем <name> із системи.
        # delete
        # <name>
        employees = self.employees
        if employee in employees:
            employees.remove(employee)
            print(f"{employee} was removed")
        else:
            print(f"{employee} does not exist in system")


    def stop(self):
        # Завершити роботу системи.
        # stop
        print("System exit")
        exit()


    def __str__(self):
        # Вивести список всіх працівників.
        # list
        return str(self.employees)


new_crm = CRM()

new_crm.add("Nicola")
new_crm.add("Nicola")
print(new_crm)

new_crm.find("Nicola")
new_crm.find("Peter")
print(new_crm)


new_crm.add("Peter")
new_crm.find("Peter")
print(new_crm)


new_crm.delete("Nicola")
new_crm.delete("Nicola")
new_crm.find("Nicola")
print(new_crm)




new_crm.stop()


