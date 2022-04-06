class Library:
    college = "SRM"
    def __init__(self, listOfBooks):
        self.books = listOfBooks
        self.book_index = range(len(listOfBooks))
        self.bookAlreadyIssued = [0] * len(listOfBooks)
        self.issuedTo = {}
    
    

    def issueBook(self, student, book):
        if book in self.books and self.bookAlreadyIssued[self.books.index(book)]==0:
            print("Issued")
            self.issuedTo[book] = student.name
            self.bookAlreadyIssued[self.books.index(book)] = 1
        else:
            if book not in self.books:
                print("Sorry this book is not in the library")
            else:
                print("Sorry the book is already issued\nPlease issue some other book")

    def returnBook(self, student, book):
        if book in self.books and self.bookAlreadyIssued[self.books.index(book)]==1:
            print("Book returned successfully")
            self.bookAlreadyIssued[self.books.index(book)]=0
        else:
            if book not in self.books:
                print("Sorry the book you are trying to return does not belong to this library")
            else:
                print("Book already returned")
