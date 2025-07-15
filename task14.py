class User:
    def interact(self):
        return "Foydalanuvchi bilan o'zaro aloqada"

class Applicant(User):
    def __init__(self, name):
        self.name = name

    def interact(self):
        return f"{self.name} ishga ariza berdi"

class Employer(User):
    def __init__(self, company):
        self.company = company

    def interact(self):
        return f"{self.company} yangi ish joyini e'lon qildi"

applicant = Applicant("Ali")
employer = Employer("Eldorjon To'ramurodov.")

print(applicant.interact())
print(employer.interact())
