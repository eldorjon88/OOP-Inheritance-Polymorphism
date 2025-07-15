class Media:
    def play(self):
        return "Media pleeeer ishga tushdi"

class Song(Media):
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def play(self):
        return f"Qo'shiq boshlandi: '{self.title}' ijrochi: {self.artist}"

class Movie(Media):
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def play(self):
        return f"Film boshlandi: '{self.title}', davomiyligi: {self.duration} daqiqa"

song = Song("Janaga", "Unknown Artist")
movie = Movie("Biror nima", 148)

print(song.play())
print(movie.play())


