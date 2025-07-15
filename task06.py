class Employee:
    def calculate_bonus(self):
        return 0

class Developer(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.10 

class Manager(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.20  

dev = Developer(5000)
man = Manager(7000)

print("Dasturchi bonusi:", dev.calculate_bonus())
print("Menejer bonusi:", man.calculate_bonus())
