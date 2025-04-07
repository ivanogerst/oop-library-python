# 📚 Library Management System (Python, OOP)

A simple object-oriented library management system built with Python, designed to demonstrate understanding of core OOP concepts.

This is a non-interactive, console-based simulation.

---

## 🔧 Features

- Add and manage **physical books** and **ebooks**
- Track **availability status**
- Register **patrons** (library users)
- Allow **checkout** and **return** of books
- Display all books and patron data
- Search for books by **title** or **author**
- Clean `main.py` entry point using `if __name__ == "__main__"`

---

## 🧱 Object-Oriented Structure

| Class     | Description                                                |
|-----------|------------------------------------------------------------|
| `Book`    | Represents a physical book with title, author, ID, status  |
| `Ebook`   | Inherits from `Book`, adds file size in MB                 |
| `Patron`  | Represents a library user who can borrow books             |
| `Library` | Stores books and patrons, manages core library operations  |

---


