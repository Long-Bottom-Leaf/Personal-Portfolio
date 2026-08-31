# Book Model

class Book:

    def __init__(self, title, author, genre, release_date, rating, status):
        self.title = title
        self.author = author
        self.genre = genre
        self.release_date = release_date
        self.rating = rating
        self.status = status

    def __str__(self):
        return(
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Genre: {self.genre}\n"
            f"Release Date: {self.release_date}\n"
            f"Rating: {self.rating}\n"
            f"Status: {self.status}\n"
        )