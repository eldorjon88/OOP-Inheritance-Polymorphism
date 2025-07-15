class Appliance:
    def turn_on(self):
        return "Qurilma ishga tushdi"

    def turn_off(self):
        return "Qurilma o'chirildi"

class TV(Appliance):
    def turn_on(self):
        return "TV yoqildi: tasvir paydo bo'ldi"

    def turn_off(self):
        return "TV o'chirildi: ekran o'chdi"

class Fridge(Appliance):
    def turn_on(self):
        return "Muzlatgich ishga tushdi: sovutmoqda"

    def turn_off(self):
        return "Muzlatgich o'chirildi: sovutish to'xtadi"

tv = TV()
fridge = Fridge()

print("Televizor:")
print(tv.turn_on())
print(tv.turn_off())

print("\nMuzlatgich:")
print(fridge.turn_on())
print(fridge.turn_off())
