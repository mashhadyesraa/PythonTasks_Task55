# PythonTasks_Task55
Library Management System
Create a simple Library Management System using Python. The system should include classes
for Library, Book, and Member. Follow these requirements:
1. Classes and Objects
• Create a Book class with:
o Attributes: title, author, isbn, and available (default True).
o Methods:
▪ __init__: To initialize the attributes.
▪ display_info: To print the book's title, author, ISBN, and availability.

• Create a Member class with:
o Attributes: name, membership_id, and a list borrowed_books.
o Methods:
▪ __init__: To initialize the attributes.
▪ borrow_book: Allows a member to borrow a book if it's available.
▪ return_book: Allows a member to return a borrowed book.

2. Inheritance
• Create a StaffMember class that inherits from Member:
o Additional attribute: staff_id.
o Additional method: add_book: Allows a staff member to add a new book to the
library.

3. Encapsulation
• Use private attributes for sensitive data such as isbn in the Book class and
membership_id in the Member class.
• Add getter and setter methods to access or modify these private attributes when
necessary.
