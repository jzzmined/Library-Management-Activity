# Library-Management-Activity

## 📚 Library Management System (Python + JSON)
This is a simple console-based Library Management System written in Python.
It allows users to add, remove, search, and display books.
All book data is stored in a JSON file (library_data.json) for persistent storage.

## ⭐ Features 

**✔ Add a Book**

    • Enter Title, Author, and Publication Year.
    • The book is automatically assigned a unique ID.
    • Data is saved to library_data.json.

**✔ Remove a Book**

    • Remove a book by title.
    • If the book exists, it is deleted from the library, and the JSON file is updated.

**✔ Search for a Book**

    • Search using:
      - Title
      - Author
    • Displays:
      - Book ID
      - Title
      - Author
      - Publication Year

**✔ Displays All Books**

     • Shows a list of all books in alphabetical order.
     • Includes ID, Title, Author, and Publication Year.

**✔ Data Persistence**

      • All books are stored in library_data.json.
      • System automatically loads previous data when started.


## 🗂 File Structure

    📁 Library Management System
    │── library_data.json   # Auto-generated storage file
    │── main.py             # Main program (your provided code)
    │── README.md           # Documentation


## ▶ How to Run the Program

1. Make sure Python 3.x is installed.
2. Save the program as main.py.
3. Open a terminal in the folder and run:


       python main.py

4. Choose an option from the menu:


        ====== LIBRARY MENU ======
        1. Add a Book
        2. Remove a Book
        3. Search a Book
        4. Display All Books
        5. Exit


## 💾 JSON Storage Format

The program automatically creates and updates library_data.json with this structure:


    {
    "books": [
        {
            "ID": 1,
            "Title": "Sample Book",
            "Author": "John Doe",
            "Publication Year": 2020
        }
    ],
    "next_id": 2
    }


## 🛠 Technologies Used


    • Python 3
    • JSON for storage
    • OS module for file checking


## 📌 Notes


    • The system is case-insensitive when searching and removing books.
    • Publication Year must be an integer.
    • The library list automatically sorts alphabetically by title.
