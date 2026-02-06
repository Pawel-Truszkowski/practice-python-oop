

class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year
        
    def __str__(self) -> str:
        return f'"{self.title}" - {self.author} ({self.year})'
    


book1 = Book("Python dla początkujących", "Jan Kowalski", 2022)
book2 = Book("Czysty Code", "Robert C. Martin", 2023)
book3 = Book("Finansowa forteca", "Marcin Iwuć", 2024)

print(book1)
print(book2)
print(book3)