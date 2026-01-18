class Book:
    def __init__(self, title, book_id):
        self.title = title
        self.id = book_id
        self.is_available = True  # Initially, the book is available

    def __str__(self):
        # Helper to print book details easily
        status = "Available" if self.is_available else "Borrowed"
        return f"[ID: {self.id}] {self.title} - {status}"


class LibrarySystem:
    def __init__(self):
        self.inventory = []  # Matches 'inventory' attribute in Design

    def add_book(self, book_obj):
        self.inventory.append(book_obj)
        print(f"Success: '{book_obj.title}' added to library.")

    def display_inventory(self):
        print("\n--- Current Library Inventory ---")
        if not self.inventory:
            print("Library is empty.")
        else:
            for book in self.inventory:
                print(book)
        print("---------------------------------\n")

    def borrow_book(self, book_id):
        for book in self.inventory:
            if book.id == book_id:
                if book.is_available:
                    book.is_available = False
                    print(f"You have borrowed '{book.title}'.")
                    return
                else:
                    print(f"Error: '{book.title}' is already borrowed.")
                    return
        print("Error: Book ID not found.")

    def return_book(self, book_id):
        for book in self.inventory:
            if book.id == book_id:
                if not book.is_available:
                    book.is_available = True
                    print(f"You have returned '{book.title}'.")
                    return
                else:
                    print(f"Error: '{book.title}' was not borrowed.")
                    return
        print("Error: Book ID not found.")


# --- SDLC Phase: Testing (Main Execution) ---
if __name__ == "__main__":
    # 1. Initialize System
    my_library = LibrarySystem()

    # 2. Add Books (Testing add_book)
    b1 = Book("Introduction to Software Engineering", "SE101")
    b2 = Book("Python for Beginners", "PY200")
    b3 = Book("Data Structures in C++", "DS300")
    
    my_library.add_book(b1)
    my_library.add_book(b2)
    my_library.add_book(b3)

    # 3. Show Initial State (Testing display_inventory)
    my_library.display_inventory()

    # 4. Borrow a Book (Testing borrow_book)
    my_library.borrow_book("SE101")
    
    # 5. Show Updated State
    my_library.display_inventory()

    # 6. Return a Book (Testing return_book)
    my_library.return_book("SE101")
    
    # 7. Final Check
    my_library.display_inventory()