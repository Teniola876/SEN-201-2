# Library Book Tracker,

NAME : AWODIRE TENIOLA ISRAEL,
MATRIC NO : 24/13733,
DEPARTMENT: SOFTWARE - ENGINEERING

## Project Overview
This project is a console-based software application designed to manage the inventory of a small library. It demonstrates the complete Software Development Life Cycle (SDLC), from requirement gathering to implementation and testing.

The system allows a librarian to add books, track their availability, and manage borrowing/returning operations in real-time.

---

## 1. Planning & Requirement Analysis
**Objective:** To solve the problem of manual book tracking by automating the status updates of library books.

**Functional Requirements:**
1.  **Add Book:** The system shall allow the user to input a book title and ID to add it to the library.
2.  **Display Inventory:** The system shall list all books and show whether they are "Available" or "Borrowed".
3.  **Borrow Book:** The system shall allow a user to borrow a book by ID, changing its status to unavailable.
4.  **Return Book:** The system shall allow a user to return a book by ID, changing its status back to available.

---

## 2. System Analysis
**Tools & Environment:**
* **Language:** Python 3.x (Selected for rapid prototyping and readability).
* **Version Control:** Git & GitHub.
* **Paradigm:** Object-Oriented Programming (OOP).
* **Platform:** Console/Terminal Application.

---

## 3. System Design (Nomenclature Definition)
*Note: The class names and method names defined here strictly match the implementation code.*

### Class Diagram Description

#### Class: `Book`
Represents an individual book entity.
* **Attributes:**
    * `title` (String): The name of the book.
    * `id` (String): Unique identifier.
    * `is_available` (Boolean): Status flag (True = Available, False = Borrowed).
* **Methods:**
    * `__str__()`: Returns formatted string of book details.

#### Class: `LibrarySystem`
Manages the collection of books.
* **Attributes:**
    * `inventory` (List): Container for storing `Book` objects.
* **Methods:**
    * `add_book(book_obj)`: Appends a new object to the inventory list.
    * `display_inventory()`: Iterates through the list and prints details.
    * `borrow_book(book_id)`: Searches for ID and updates `is_available` to False.
    * `return_book(book_id)`: Searches for ID and updates `is_available` to True.

---

## 4. Implementation
The project is implemented in a single module `main.py` following the OOP principles defined in the Design phase.

**Key Code Snippet:**
```python
# Matching the Design Nomenclature
class LibrarySystem:
    def __init__(self):
        self.inventory = []

    def borrow_book(self, book_id):
        # Implementation logic matches Requirement #3
        for book in self.inventory:
            if book.id == book_id:
                book.is_available = False

5. TestingTest Plan:We performed "Black Box Testing" to verify that the system functions correctly according to the requirements.Test Case IDActionInput DataExpected ResultPass/FailTC-01Add a new bookTitle: "Python Intro", ID: "101"System prints "Success"PASSTC-02Display BooksN/ALists "Python Intro" as AvailablePASSTC-03Borrow BookID: "101"Status changes to "Borrowed"PASSTC-04Borrow Invalid BookID: "999"Error: "Book ID not found"PASSTC-05Return BookID: "101"Status changes to "Available"PASSEvidence of ExecutionBelow is the log from the terminal showing the program running successfully:PlaintextSuccess: 'Introduction to Software Engineering' added to library.
Success: 'Python for Beginners' added to library.

--- Current Library Inventory ---
[ID: SE101] Introduction to Software Engineering - Available
[ID: PY200] Python for Beginners - Available
---------------------------------

You have borrowed 'Introduction to Software Engineering'.

--- Current Library Inventory ---
[ID: SE101] Introduction to Software Engineering - Borrowed
[ID: PY200] Python for Beginners - Available
---------------------------------

You have returned 'Introduction to Software Engineering'.
6. MaintenanceTo ensure the project remains useful, the following maintenance tasks are planned:Database Integration: Replace the current list-based storage with an SQLite database to ensure data is saved permanently.Error Handling: Improve the code to handle cases where a user inputs numbers instead of text.GUI Update: Build a visual interface using Tkinter or Framer so users don't have to use the terminal.How to Run This ProjectClone the repository:Bashgit clone https://github.com/Teniola876/SEN-201-2.git
Navigate to the directory:Bashcd SEN-201-2
Run the python file:Bashpython main.py