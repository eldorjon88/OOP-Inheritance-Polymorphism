class Document:
    def print_preview(self):
        return "Hujjat ko'rinishini chiqarish"

class WordDocument(Document):
    def __init__(self, title):
        self.title = title

    def print_preview(self):
        return f"Word fayli: '{self.title}' - sahifa ko'rinishi"

class PdfDocument(Document):
    def __init__(self, title):
        self.title = title

    def print_preview(self):
        return f"PDF fayli: '{self.title}' - oldindan ko'rish"

word = WordDocument("Referat.docx")
pdf = PdfDocument("Ma'lumotnoma.pdf")

print(word.print_preview())
print(pdf.print_preview())
