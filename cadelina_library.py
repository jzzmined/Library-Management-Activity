import json
import os

library = []
next_id = 1

# LOAD LIBRARY FROM THE FILE
def load_library():
    global library, next_id

    if os.path.exists("library_data.json"):
        try:
            with open("library_data.json","r") as file:
                data = json.load(file)
                library = data.get("books", [])
                next_id = data.get("next_id", 1)
            print("Library data loaded successfully!")
        except:
            print("Error loading library data. Starting fresh.")
    else:
        print("No previous library data found. Starting fresh.")


# SAVE LIBRARY TO FILE
def save_library():

    try:
        data = {
            "books" : library,
            "next_id": next_id
        }
        with open ("library_data.json", "w") as file:
            json.dump(data, file, indent = 4)
    except:
        print("Error saving library datas.")


#ADD A BOOK
def add_book():
    global next_id

    print("\n--ADD A BOOK---")
    title = input("\nEnter book Title: ")
    author = input("Enter author name: ")
    pub_year = int(input("Enter publication year: "))

    book = {
        "ID": next_id,
        "Title" : title,
        "Author": author,
        "Publication Year": pub_year
        }

    library.append(book)
    next_id += 1
    print(f"\nBook '{title}' added successfully with ID: {book['ID']}")
    save_library()

# REMOVE BOOK
def remove_book():
    print("---REMOVE A BOOK---")
    title = input("\nEnter book title to remove: ")

    for book in library:
        if book ["Title"].lower() == title.lower():
            library.remove(book)
            print(f"Book '{title}' (ID: {book['ID']}) remove successfully!")
            save_library()
            return

    print(f"Book '{title}' not found in the library.")

# SEARCH BOOK
def search_book():
    print("\n---SEARCH FOR A BOOK---")
    print("1. Search by Title: "
          "\n2. Search by Author: ")
    choice = input("Choose search option: ")

    if choice == '1':
        search_enter = input("\nEnter book title to search: ")
        search_key =  "Title"
    elif choice == '2':
        search_enter = input("Enter author name to search: ")
        search_key = "Author"
    else:
        print("Invalid option...")
        return

    found_books = []
    for book in library:
         if search_enter.lower() in book [search_key].lower():
             found_books.append(book)

    if found_books:
        print(f"\n{len(found_books)} book(s) found: ")
        for i, book in enumerate(found_books, 1):
            print(f"{i}. [ID: {book['ID']}] {book['Title']} by {book['Author']} ({book['Publication Year']})")

    else:
        print(f"No books found matching '{search_enter}'.")


# DISPLAY BOOKS
def display_books():
    print("\n---LIST OF ALL BOOKS---")

    if not library:
        print("\nNo books in the library.")
        return
    sorted_library = sorted(library, key=lambda  x: x["Title"].lower())
    print("\nList of all books: ")
    for i, book in enumerate (sorted_library, 1):
        print(f"{i}. [ID: {book['ID']}] {book['Title']} by {book['Author']} ({book['Publication Year']})")


# MAIN PROGRAM
def main():
    load_library()
    def display_lib_menu():
     print("""\n ====== LIBRARY MENU ======
1. Add a Book
2. Remove a Book
3. Search a Book
4. Display All Books
5. Exit""")

    while True:
        display_lib_menu()
        choice = input("\nChoose an option(1-5): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            search_book()
        elif choice == '4':
            display_books()
        elif choice == '5':
            print("Thank you for using Library Management System!")
            break
        else:
            print("\n Invalid choice! Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()











