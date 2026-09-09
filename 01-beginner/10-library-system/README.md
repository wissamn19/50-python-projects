# Mini Library Management System

> OOP, inheritance, file persistence

## Overview
A command-line library management system that handles both digital and physical
books using OOP inheritance. Supports adding, removing, searching, borrowing,
and returning books — with full JSON persistence so the library is saved between
sessions. Built to understand how inheritance works in Python and how to convert
objects to JSON and back.

## Concepts Practiced
- OOP — `Book` parent class with `DigitalBook` and `PhysicalBook` children
- Inheritance — `super().__init__()` to share common attributes
- `__str__` method — clean string representation of objects
- JSON persistence — saving and loading objects using `__dict__`
- Error handling — empty JSON file, corrupted file, file not found
- Interactive menu with `input()` and `while True` loop

## How to Run
```bash
# from this folder
python main.py
```

## Class Structure

```
Book (parent)
├── title, author, isbn, price, is_borrowed
├── DigitalBook (child)
│   └── + file_format, file_size
└── PhysicalBook (child)
    └── + pages, condition

Library
└── add, remove, search, show_all, borrow, return, save, load
```

## 💡 What I Learned

The hardest part of this project was JSON persistence especifically the
save and load logic. Saving was straightforward once I discovered `book.__dict__`,
which converts any object into a dictionary automatically. But loading was trickier:
JSON gives you back plain dictionaries, not objects. I had to check which keys
each dictionary contained to decide whether to recreate it as a `DigitalBook`
or a `PhysicalBook`, then pass the values back into the constructor manually.

The empty JSON file bug was also a real lesson, a previous failed save had
created an empty file, and `json.load()` crashed trying to parse nothing. The
fix was to read the file content first, check if it was empty before parsing,
and add a `JSONDecodeError` exception as a safety net. Now the program handles
corrupted or empty files gracefully instead of crashing.

Inheritance itself was simpler than I expected, `class DigitalBook(Book)` and
`super().__init__()` were enough to share all the common attributes. The real
complexity was in the persistence layer, not the class structure.

---
[← Back to main repo](../../README.md)