"""
Pornsawan hareram
683040156-9
"""
from P1 import LibraryItem, Book, TextBook, Magazine

e = LibraryItem("aaa", "L001")
e.display_info()

book = Book("Harry Potter", "B001", "J.K. Rowling")
book.set_pages_count(350)

textbook = TextBook("Physics", "T101", "Serway", "Science", 12)
textbook.set_pages_count(500)

mag = Magazine("Time", "M202", 45)

print()
book.display_info()
book.check_out()
book.display_info()
print()

if book.check_out() == False:
    print("Cannot check out, already checked out.")

textbook.check_out()
textbook.display_info()
print()

mag.display_info()
