class User:
    def get_dashboard(self):
        return "Dashboard ma'lumotlari mavjud emas"

class Student(User):
    def __init__(self, courses):
        self.courses = courses

    def get_dashboard(self):
        return f"Sizning kurslaringiz: {', '.join(self.courses)}"

class Instructor(User):
    def __init__(self, stats):
        self.stats = stats

    def get_dashboard(self):
        return f"Kurs statistikalar: {self.stats}"

student = Student(["Python", "Data Science", "Matematika"])
instructor = Instructor({"Python": "20 talabalar", "Data Science": "15 talabalar"})

print(student.get_dashboard())
print(instructor.get_dashboard())
