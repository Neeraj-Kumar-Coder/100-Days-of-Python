class Library:
    def __init__(self) -> None:
        self._books = []

    def add_book(self, book: str):
        if book.capitalize() in self._books:
            return
        self._books.append(book.capitalize())

    def get_book(self, book: str):
        if book.capitalize() not in self._books:
            return "Book is NOT present in the library"

        self._books.remove(book.capitalize())
        return "Book Granted!"

    @property
    def number_of_books_in_library(self):
        return len(self._books)


my_library = Library()
my_library.add_book("Introduction to C")
my_library.add_book("Competitve programmers handbook")
my_library.add_book("Play with graphs")
my_library.add_book("Intorduction to algorithms")
print(my_library.number_of_books_in_library)

print(my_library.get_book("introduction to c"))
print(my_library.get_book("introduction to c"))
