class User:
    def access_level(self):
        return "Noma'lum kirish darajasi"

class Admin(User):
    def access_level(self):
        return "Admin: Ruxsat cheklanmagan"

class Guest(User):
    def access_level(self):
        return "Guest: Ruxsat cheklangan"

admin = Admin()
mehmon = Guest()

print("Admin:", admin.access_level())
print("Mehmon:", mehmon.access_level())
