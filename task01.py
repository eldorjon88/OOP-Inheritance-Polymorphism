class Animal:
    def speak(self):
        return "Hayvon tovushi"

class Dog(Animal):
    def speak(self):
        return "Vov-vov!"

class Cat(Animal):
    def speak(self):
        return "Miyov!"

it = Dog()
mushuk = Cat()

print("It:", it.speak())
print("Mushuk:", mushuk.speak())
