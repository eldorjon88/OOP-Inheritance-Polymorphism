class Notification:
    def send(self):
        return "Xabar jo'natildi"

class EmailNotification(Notification):
    def __init__(self, email):
        self.email = email

    def send(self):
        return f"Email yuborildi: {self.email} manzilga"

class SMSNotification(Notification):
    def __init__(self, phone):
        self.phone = phone

    def send(self):
        return f"SMS yuborildi: {self.phone} raqamga"

email = EmailNotification("example@gmail.com")
sms = SMSNotification("+998889302033")

print(email.send())
print(sms.send())
