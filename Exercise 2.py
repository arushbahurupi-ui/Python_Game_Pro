class Book():

    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_borrowed = False

    def borrow_book(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(self.title, "has been borrowed.")
        else:
            print(self.title, "is already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(self.title, "has been returned.")
        else:
            print(self.title, "was not borrowed.")

    def display_info(self):
        if self.is_borrowed:
            status = "Borrowed"
        else:
            status = "Available"
        print("Title:", self.title)
        print("Author:", self.author)
        print("Book ID:", self.book_id)
        print("Status:", status)
        print("-" * 30)

book1 = Book("Harry Potter", "J.K. Rowling", 101)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 102)
book3 = Book("The Alchemist", "Paulo Coelho", 103)


book1.display_info()
book2.display_info()
book3.display_info()

book1.borrow_book()
book1.borrow_book()

book1.return_book()
book1.return_book()

book1.display_info()
book2.display_info()
book3.display_info()

