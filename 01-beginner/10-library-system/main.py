import json

filename = "library.json"

class Book():
    def __init__(self, title,author,isbn,price,is_borrowed):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.is_borrowed = is_borrowed = False

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Price: {self.price}, Borrowed: {self.is_borrowed}"

class DigitalBook(Book):
    def __init__(self, title, author, isbn, price, is_borrowed, file_size , file_format):
        super().__init__(title, author, isbn, price, is_borrowed)
        self.file_size = file_size
        self.file_format = file_format

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Price: {self.price}, Borrowed: {self.is_borrowed}, File Size: {self.file_size}MB"


class PhysicalBook(Book):
    def __init__(self, title, author, isbn, price, is_borrowed, page , condition):
        super().__init__(title, author, isbn, price, is_borrowed)
        self.page = page
        self.condition = condition 

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Price: {self.price}, Borrowed: {self.is_borrowed}, Page: {self.page}, Condition: {self.condition}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        self.save_file("library.json")
        

    def remove_book(self, book):
        self.books.remove(book)
        self.save_file("library.json")

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def show_all(self):
        for book in self.books:
            print(book)

    def borrow_book(self, title):
        book = self.search_book(title)
        if book and not book.is_borrowed:
            book.is_borrowed = True
            print(f"You have borrowed {book.title}.")
            self.save_file("library.json")
        else:
            print(f"{title} is not available for borrowing.")

    def return_book(self, title):
        book = self.search_book(title)
        if book and book.is_borrowed:
            book.is_borrowed = False
            print(f"You have returned {book.title}.")
            self.save_file("library.json")
        else:
            print(f"{title} was not borrowed.")

    def save_file(self, filename):
        with open(filename, 'w') as f:
            json.dump([book.__dict__ for book in self.books], f)  

    def load_file(self, filename):
        try:
         with open(filename, 'r') as f:
            data = json.load(f)
            for item in data:
                if 'file_format' in item:
                    book = DigitalBook(item['title'], item['author'], item['isbn'], item['price'], item['is_borrowed'], item['file_size'], item['file_format'])
                else:
                    book = PhysicalBook(item['title'], item['author'], item['isbn'], item['price'], item['is_borrowed'], item['page'], item['condition'])
                self.books.append(book)
        except FileNotFoundError:
          pass  

def menu():
    library = Library()
    library.load_file("library.json")
    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Show All Books")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            price = float(input("Enter book price: "))
            is_borrowed = input("Is the book borrowed? (yes/no): ").lower() == "yes"
            book_type = input("Is it a digital or physical book? (digital/physical): ").lower()

            if book_type == "digital":
                file_size = float(input("Enter file size (MB): "))
                file_format = input("Enter file format (e.g., PDF, EPUB): ")
                book = DigitalBook(title, author, isbn, price, is_borrowed, file_size, file_format)
            elif book_type == "physical":
                page = int(input("Enter number of pages: "))
                condition = input("Enter condition (New/Used): ")
                book = PhysicalBook(title, author, isbn, price, is_borrowed, page, condition)
            else:
                print("Invalid book type.")
                continue

            library.add_book(book)
            print(f"Book '{title}' added to the library.")

        elif choice == "2":
            title = input("Enter the title of the book to remove: ")
            book = library.search_book(title)
            if book:
                library.remove_book(book)
                print(f"Book '{title}' removed from the library.")
            else:
                print(f"Book '{title}' not found in the library.")

        elif choice == "3":
            title = input("Enter the title of the book to search: ")
            book = library.search_book(title)
            if book:
                print(book.__str__())
            else:
                print(f"Book '{title}' not found in the library.")

        elif choice == "4":
            library.show_all()

        elif choice == "5":
            title = input("Enter the title of the book to borrow: ")
            library.borrow_book(title)

        elif choice == "6":
            title = input("Enter the title of the book to return: ")
            library.return_book(title)

        elif choice == "7":
            print("Exiting the library system.")
            break

        else:
            print("Invalid choice. Please try again.")

def main():
    menu()


if __name__ == "__main__":
    main()
    