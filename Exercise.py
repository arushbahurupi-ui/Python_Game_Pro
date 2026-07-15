class Library():

    def __init__(self, book_name, author, copies, price):
        self.book_name = book_name
        self.author = author
        self.copies = copies
        self.price = price



    def borrow_book(self):
        if self.copies > 0:
            self.copies -= 1
            print(self.book_name, "borrowed successfully.")
            print("Copies left:", self.copies)
        else:
            print("Book is not available.")


    def return_book(self):
        self.copies += 1
        print(self.book_name, " returned successfully.")
        print("Copies available:", self.copies)


    def apply_discount(self, discount_percent):
        discount_amount = self.price * discount_percent / 100
        self.price -= discount_amount
        print("Price after", discount_percent, "% discount:", self.price)



book1 = Library("Harry Potter", "J.K. Rowling", 5, 500)
book1.borrow_book()
book1.return_book()
book1.apply_discount(10)