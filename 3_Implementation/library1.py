import sys


class Library:
    # deriving a library to the program
    def __init__(self, listofbooks):
        self.books = listofbooks

    # function to display the available books in the library
    # including print function to print the books available.
    def disp_available_books(self):
        print(f"\n{len(self.books)} THE AVAILABLE BOOKS IN THE LIBRARY ARE: ")
        for books in self.books:
            print(" ♦---- " + books)
        print("\n")

    # function to borrow a book from the library
    def borrow_a_book(self, name, bookname):
        if bookname not in self.books:
            # giving a print statement as given below if the book is not available in the library
            print(
                f"{bookname} SORRY THIS BOOK IS NOT AVAILABLE IN OUR LIBRARY RIGHT NOW,"
                f" EITHER TAKEN BY SOMEONE ELSE, WAIT UNTIL HE RETURNED.\n")
            # if the above given function does not satisfied then the else function is implemented
        else:
            track.append({name: bookname})  # giving a print statement as given below
            print("BOOK ISSUED : THANK YOU FOR HIRING A BOOK FROM OUR LIBRARY"
                  " KEEP IT WITH CARE AND RETURN ON TIME.\n")
            self.books.remove(bookname)
        # this is the function to return a book to the library.

    def return_a_book(self, bookname):
        print("BOOK RETURNED : THANK YOU! "
              "KEEP READING! \n")
        self.books.append(bookname)

    # this function helps in taking the input
    # and storing the books name
    # and availability of new books which will be donated by the user
    def donate_a_book(self, bookname):
        print("BOOK DONATED : THANK YOU VERY MUCH, HAVE A GREAT DAY AHEAD.\n")
        self.books.append(bookname)


# Deriving a new class to called student
class Student:
    def __init__(self):
        self.book = None

    def request_a_book(self):  # function to the student class to request a book
        print("I CAN UNDERSTAND THAT, you want to borrow book!")
        # when we enter the name of the book then the data will be uploaded.
        self.book = input("Enter name of the book you want to borrow: ")
        return self.book

    # function to return a book to a library which has been already borrowed.
    def return_a_book(self):
        print("So, you want to return book!")
        name = input("Enter your name: ")
        self.book = input("Enter name of the book you want to return: ")
        if {name: self.book} in track:
            track.remove({name: self.book})
        return self.book

    # function to add data to the donated books by the user.
    def donate_a_book(self):
        print("Okay! you want to donate book!")
        self.book = input("Enter name of the book you want to donate: ")
        return self.book


if __name__ == "__main__":
    library = Library(
        ["KGF chapter 2", "invention", "KGF chapter 1", "indian",
         "macroeconomics",
         "microeconomics"])
    student = Student()
    track = []

    print("\t\t\t\t\t\t\t♦♦♦♦♦♦♦ WELCOME TO THE LIBRARY ♦♦♦♦♦♦♦\n")
    print(
        """CHOOSE THE OPTION IN WHICH WE CAN HELP YOU:-\n
        1. PRESS 1 TO KNOW THE LIST ALL THE BOOKS AVAILABLE IN OUR LIBRARY.\n
        2. PRESS 2 TO BORROW A BOOK.\n
        3. PRESS 3 TO RETURN A BOOK. \n
        4. PRESS 4 TO DONATE A BOOK.\n
        5. PRESS 5 TO TRACK THE STATUS OF THE BOOK.\n
        6. PRESS 6 TO EXIT THE LIBRARY. \n""")
    while True:  # Here we are including the while loop,
        # and it will be executed if the condition satisfies.
        try:
            usr_resp = int(input(" Please Enter your choice: "))

            if usr_resp == 1:
                # If the user press one then it will display the list of books available in the library.
                library.disp_available_books()
            elif usr_resp == 2:
                # If the user respond with number 2,then it opens the option for borrowing a book.
                library.borrow_a_book(
                    input("Enter your name: "), student.request_a_book())
            elif usr_resp == 3:
                # If the user needs to return a book back to the library, then he can press 3.
                library.return_a_book(student.return_a_book())
            elif usr_resp == 4:
                # If a user wish to donate a book to the library, then he can press 4.
                library.donate_a_book(student.donate_a_book())
            elif usr_resp == 5:
                # If a user needs to track a status of the book then he can press 5
                for i in track:
                    for key, value in i.items():
                        holder = key
                        book = value
                        print(f"{book} book is taken/issued by {holder}.")
                print("\n")
                # next line
                if len(track) == 0:
                    print("NO BOOKS ARE ISSUED!. \n")
                # if the user needs to exit the library then user can press 6
            elif usr_resp == 6:  # exit
                print("THANK YOU ! \n")
                sys.exit()
            else:
                print("INVALID INPUT! \n")
        except Exception as e:
            # If there is any error in the code then it will be displayed as cache error.
            print(f"{e}---> INVALID INPUT! \n")
