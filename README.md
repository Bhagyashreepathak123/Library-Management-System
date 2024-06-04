# Library Management System

A simple Library Management System implemented using Object-Oriented Programming (OOP) principles in Python.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Class Structure](#class-structure)
- [Usage](#usage)
- [Installation](#installation)
- [Example Usage](#example-usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This Library Management System allows for managing a collection of books and registered members. Members can borrow and return books, and the system keeps track of the availability of books.

## Features

- Add books to the library.
- Register members to the library.
- Borrow and return books.
- Check availability of books.

## Class Structure

- **Book**: Represents a book with attributes like title, author, and ISBN.
- **Member**: Represents a library member with attributes like name, member ID, and list of borrowed books.
- **Library**: Manages the collection of books and registered members.
- **Loan**: Represents the loan of a book to a member (for future expansion).

## Usage

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/library-management-system.git
    ```
2. Navigate to the project directory:
    ```bash
    cd library-management-system
    ```
3. Run the main script to start the system:
    ```bash
    python main.py
    ```

### Example Usage

```python
from library import Library, Book, Member

# Create a library instance
library = Library()

# Create books
book1 = Book("The Catcher in the Rye", "J.D. Salinger", "9780316769488")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")

# Add books to the library
library.add_book(book1)
library.add_book(book2)

# Create a member
member1 = Member("Alice Johnson", "M001")

# Register member
library.register_member(member1)

# Member borrows a book
member1.borrow_book(book1)

# Member returns a book
member1.return_book(book1)

# Attempt to borrow an unavailable book
member1.borrow_book(book2)
member1.borrow_book(book2)  # This will show that the book is not available
