class Vehicle:
    def show_info(self):
        return "Transport haqida ma'lumot"

class Car(Vehicle):
    def show_info(self):
        return "Bu mashina: 4 g'ildirak, saloni ideal."

class Bike(Vehicle):
    def show_info(self):
        return "Bu velosiped: 2 g'ildirak, pedal bilan yuradi"

mashina = Car()
velik = Bike()

print("Mashina:", mashina.show_info())
print("Velosiped:", velik.show_info())
