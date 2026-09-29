class book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
           self.is_borrowed = True
           print(f"{self.title} has been successfully borrowed")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"{self.title} has been successfully returned")

        else:
            print(f"{self.title} hadnt been borrowed")


book1 = book("Harry Potter", "J K Rowling",)
book2 = book("The Jungle", "Haaland",)
book3 = book("The hunger games", "Mr Beast",)

book1.borrow()
book2.borrow()
book3.borrow()

book1.return_book()
book2.return_book()

print("\nCurrent Books status : ")
print(f"{book1.title} - borrowed and not returned: {book1.is_borrowed}")
print(f"{book2.title} - borrowed and not returned: {book2.is_borrowed}")
print(f"{book3.title} - borrowed and not returned: {book3.is_borrowed}")
