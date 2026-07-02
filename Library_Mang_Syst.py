class Book:
    def __init__(self,title,author,isbn,available=True):
        self.title= title
        self.author=author
        self.isbn=isbn
        self.available=available

    def display_info(self):
        status=""
        if self.available == True :
            status="Available"
        else:
            status="Borrowed"

        print(f"{self.title} by {self.author} with ISBN: {self.isbn} Status: {status} ")    

class Member:
    def __init__(self,name,membership_id):
        self.name=name
        self.membership_id=membership_id
        self.borrowed_books=[]

    def borrow_book(self, book):
        if book.available:
            book.available=False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"Sorry  {book.title} is unavailable! ")    


    def return_book(self,book):
        if book in self.borrowed_books:
            book.available=True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} does not have this book")


class StaffMember(Member):
    def __init__(self,name,membership_id,staff_id):
        super().__init__(name,membership_id)
        self.staff_id=staff_id 

    def add_book(self,library_list,new_book):
            library_list.append(new_book)
            print(f"staff {self.name} added {new_book.title} to the library")


library=[]
staff1=StaffMember("Esraa","M001","S001")
staff2=StaffMember("Mariam","M002","S002")

book1=Book("Python Principles","John B","12345")
book2=Book("AI Principles","William S","34567")

staff1.add_book(library,book1)
staff1.borrow_book(book1)
book1.display_info()


staff2.add_book(library,book2)
staff2.borrow_book(book2)
book2.display_info()
        
        