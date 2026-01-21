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
```
## 5. Testing Phase
We performed functional testing to verify the system meets all requirements.

### Test Cases Table
| Test Case ID | Action | Input Data | Expected Result | Pass/Fail |
| :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Add a new book | Title: "Python Intro", ID: "101" | System prints "Success" | **PASS** |
| **TC-02** | Display Books | N/A | Lists "Python Intro" as Available | **PASS** |
| **TC-03** | Borrow Book | ID: "101" | Status changes to "Borrowed" | **PASS** |
| **TC-04** | Borrow Invalid Book | ID: "999" | Error: "Book ID not found" | **PASS** |
| **TC-05** | Return Book | ID: "101" | Status changes to "Available" | **PASS** |

### Evidence of Execution
Below is the actual output from the terminal when running `main.py`:

```text
Success: 'Introduction to Software Engineering' added to library.
Success: 'Python for Beginners' added to library.
Success: 'Data Structures in C++' added to library.

--- Current Library Inventory ---
[ID: SE101] Introduction to Software Engineering - Available
[ID: PY200] Python for Beginners - Available
[ID: DS300] Data Structures in C++ - Available
---------------------------------

You have borrowed 'Introduction to Software Engineering'.
