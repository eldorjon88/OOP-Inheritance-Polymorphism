import math

class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

aylana = Circle(5)
tortburchak = Rectangle(4, 6)
uchburchak = Triangle(3, 7)

print("Aylana maydoni:", aylana.area())
print("To'rtburchak maydoni:", tortburchak.area())
print("Uchburchak maydoni:", uchburchak.area())
