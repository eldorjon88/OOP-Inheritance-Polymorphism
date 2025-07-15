class Product:
    def get_delivery_method(self):
        return "Mahsulot yetkazib berish usuli noma'lum"

class PhysicalProduct(Product):
    def __init__(self, name):
        self.name = name

    def get_delivery_method(self):
        return f"{self.name} — kuryer orqali yetkaziladi"

class DigitalProduct(Product):
    def __init__(self, name):
        self.name = name

    def get_delivery_method(self):
        return f"{self.name} — internet orqali yuklab olinadi"

book = PhysicalProduct("Python kitobi")
music = DigitalProduct("Janaga musiqasi")

print(book.get_delivery_method())
print(music.get_delivery_method())
